# -*- coding: utf-8 -*-
"""生成《技术支持 FAQ TOP20 类问题》HTML 报告。

口径（Fly 2026-08-31 确认）：
  - 【禁】类工单数据有效，全量计入统计，不剔除。
  - 不输出客户维度。
  - 主题聚类只用「问题现象描述」，关键词规则 + 优先级单标签。
输出：build/reports/FAQ-TOP20类问题报告.html
"""
import html
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyze_faq_topics import load_east, load_puyuan, classify  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / 'build' / 'reports' / 'FAQ-TOP20类问题报告.html'
TOP_N = 20


def pick_examples(rows, idx, n=3, lo=12, hi=52):
    """从一类工单里挑 n 条长度适中的现象描述作为典型现象"""
    out, seen = [], set()
    for r in rows:
        d = (str(r[idx['问题现象描述']] or '')).replace('\n', ' ').strip()
        if not (lo <= len(d) <= hi):
            continue
        key = d[:16]
        if key in seen:
            continue
        seen.add(key)
        out.append(d)
        if len(out) >= n:
            break
    return out


def pick_case(rows, idx):
    """挑 1 条有结论的代表工单"""
    def score(r):
        d = str(r[idx['问题现象描述']] or '')
        c = str(r[idx['结论及处理']] or '')
        return (1 if 18 <= len(d) <= 90 else 0) + (1 if 18 <= len(c) <= 120 else 0)
    return max(rows, key=score)


def bar(pct, maxpct, color):
    w = 0 if maxpct == 0 else pct / maxpct * 100
    return ('<div class="bar-track"><div class="bar-fill" style="width:%.1f%%;'
            'background:%s"></div></div>' % (w, color))


def build_html():
    hdr, idx, data = load_east()
    total = len(data)
    banned = [r for r in data if str(r[idx['问题类型']] or '').startswith('【禁】')]

    main = Counter()
    by_topic = defaultdict(list)
    unclassified = []
    for r in data:
        m = classify(str(r[idx['问题现象描述']] or ''))
        if m is None:
            unclassified.append(r)
        else:
            main[m] += 1
            by_topic[m].append(r)

    top = main.most_common(TOP_N)
    maxpct = top[0][1] * 100 / total
    ts = [str(r[idx['实际服务时间']])[:10] for r in data if r[idx['实际服务时间']]]
    span = '%s ~ %s' % (min(ts), max(ts))
    top3 = sum(v for _, v in top[:3])
    covered = sum(v for _, v in top)

    # 官方问题类型
    official = Counter(str(r[idx['问题类型']]) for r in data).most_common()
    off_max = official[0][1]

    # 噗元交叉验证
    phdr, pidx, pdata = load_puyuan()
    pmain = Counter()
    for r in pdata:
        m = classify(str(r[pidx['问题（提问者填写）']] or ''))
        pmain[m or '未分类'] += 1
    ptop = [(k, v) for k, v in pmain.most_common(8) if k != '未分类']

    # 结论里用到的动态数值
    shake_n = main.get('抖动/异响/噪音', 0)
    shake_param = sum(1 for r in by_topic.get('抖动/异响/噪音', [])
                      if str(r[idx['本次问题部件']] or '') == '客户参数设置不当')
    fw_n = main.get('固件/软件BUG/升级', 0)
    ban_pct = len(banned) * 100 / total

    colors = ['#D85A30'] * 3 + ['#378ADD'] * 5 + ['#85B7EB'] * 12
    e = html.escape

    rows_html = []
    for i, (k, v) in enumerate(top):
        pct = v * 100 / total
        rs = by_topic[k]
        pl = Counter(str(r[idx['执行器产品线']] or '未标') for r in rs).most_common(3)
        rt = Counter(str(r[idx['本次问题部件']] or '未标') for r in rs).most_common(3)
        ex = pick_examples(rs, idx)
        case = pick_case(rs, idx)
        c_d = (str(case[idx['问题现象描述']] or '')).replace('\n', ' ').strip()
        c_c = (str(case[idx['结论及处理']] or '')).replace('\n', ' ').strip()
        c_r = str(case[idx['本次问题部件']] or '—')
        c_m = str(case[idx['执行器型号1']] or '—')

        rows_html.append(f'''
    <tr>
      <td class="rank">{i + 1}</td>
      <td class="cat">
        <div class="cat-name">{e(k)}</div>
        <div class="bar">{bar(pct, maxpct, colors[i])}</div>
        <ul class="ex">{''.join('<li>%s</li>' % e(x) for x in ex)}</ul>
        <details>
          <summary>代表工单</summary>
          <div class="case">
            <p><span class="tag">现象</span>{e(c_d[:150])}</p>
            <p><span class="tag">结论</span>{e(c_c[:180])}</p>
            <p><span class="tag">根因</span>{e(c_r)}　<span class="tag">型号</span>{e(c_m[:48])}</p>
          </div>
        </details>
      </td>
      <td class="num">{v}</td>
      <td class="num">{pct:.1f}%</td>
      <td class="sub">{'<br>'.join('%s %d' % (e(a), b) for a, b in pl)}</td>
      <td class="sub">{'<br>'.join('%s %d' % (e(a), b) for a, b in rt)}</td>
    </tr>''')

    off_html = ''.join(
        '<tr><td>%s</td><td class="num">%d</td><td class="num">%.1f%%</td>'
        '<td class="bwrap"><div class="off-fill" style="width:%.1f%%"></div></td></tr>'
        % (e(k), v, v * 100 / total, v / off_max * 100)
        for k, v in official)

    p_html = ''.join(
        '<tr><td>%s</td><td class="num">%d</td><td class="num">%.1f%%</td></tr>'
        % (e(k), v, v * 100 / len(pdata)) for k, v in ptop)

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>技术支持 FAQ TOP20 类问题</title>
<style>
  :root {{
    --bg: #ffffff; --surface: #f7f7f5; --line: #e3e2dd;
    --text: #23231f; --muted: #6b6a64; --accent: #185FA5;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 32px 28px 64px; background: var(--bg); color: var(--text);
    font-family: system-ui, -apple-system, "Segoe UI", "Microsoft YaHei", sans-serif;
    font-size: 14px; line-height: 1.7;
  }}
  .wrap {{ max-width: 1180px; margin: 0 auto; }}
  h1 {{ font-size: 24px; font-weight: 600; margin: 0 0 6px; }}
  .meta {{ color: var(--muted); font-size: 13px; margin-bottom: 24px; }}
  h2 {{ font-size: 17px; font-weight: 600; margin: 36px 0 12px;
        padding-bottom: 8px; border-bottom: 1px solid var(--line); }}
  .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; }}
  .card {{ background: var(--surface); border-radius: 8px; padding: 14px 16px; }}
  .card .l {{ font-size: 12px; color: var(--muted); }}
  .card .v {{ font-size: 24px; font-weight: 600; margin-top: 2px; }}
  .card .s {{ font-size: 12px; color: var(--muted); }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 8px; }}
  th, td {{ text-align: left; padding: 10px 10px; vertical-align: top;
            border-bottom: 1px solid var(--line); }}
  th {{ font-size: 12px; font-weight: 600; color: var(--muted);
        background: var(--surface); white-space: nowrap; }}
  td.num {{ text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }}
  td.rank {{ font-size: 13px; color: var(--muted); width: 28px; padding-top: 14px; }}
  td.cat {{ min-width: 380px; }}
  td.sub {{ font-size: 12px; color: var(--muted); white-space: nowrap; }}
  .cat-name {{ font-weight: 600; }}
  .bar-track {{ width: 100%; max-width: 300px; height: 8px; background: #ecebe7;
                border-radius: 4px; margin: 6px 0 8px; overflow: hidden; }}
  .bar-fill {{ height: 100%; border-radius: 4px; }}
  ul.ex {{ margin: 0 0 6px; padding-left: 18px; color: var(--muted); font-size: 13px; }}
  ul.ex li {{ margin-bottom: 2px; }}
  details summary {{ cursor: pointer; font-size: 12px; color: var(--accent);
                     list-style: none; outline: none; }}
  details summary::-webkit-details-marker {{ display: none; }}
  details summary::before {{ content: "▸ "; }}
  details[open] summary::before {{ content: "▾ "; }}
  .case {{ background: var(--surface); border-radius: 6px; padding: 10px 12px;
           margin-top: 8px; font-size: 13px; }}
  .case p {{ margin: 4px 0; }}
  .tag {{ display: inline-block; min-width: 34px; font-size: 11px; color: #fff;
          background: #888780; border-radius: 3px; padding: 0 5px; margin-right: 6px;
          text-align: center; }}
  .bwrap {{ width: 22%; }}
  .off-fill {{ height: 8px; background: #85B7EB; border-radius: 4px; }}
  .note {{ background: var(--surface); border-left: 3px solid #EF9F27;
           border-radius: 0 6px 6px 0; padding: 12px 16px; font-size: 13px; margin: 12px 0; }}
  .find {{ background: var(--surface); border-radius: 8px; padding: 4px 20px 12px;
           margin: 12px 0; }}
  .find li {{ margin: 10px 0; }}
  code {{ background: #f0efec; border-radius: 3px; padding: 1px 5px; font-size: 12px; }}
  footer {{ margin-top: 40px; padding-top: 16px; border-top: 1px solid var(--line);
            font-size: 12px; color: var(--muted); }}
  @media print {{ body {{ padding: 0; }} details {{ display: none; }} }}
</style>
</head>
<body>
<div class="wrap">

<h1>技术支持 FAQ TOP20 类问题</h1>
<div class="meta">
  数据源：<code>raw/fae-qa/华东工单提取仅技术服务&amp;高价值FAQ_20260820.xlsx</code>　·
  统计日期：2026-08-31　·　生成脚本：<code>scripts/gen_faq_report.py</code>
</div>

<div class="cards">
  <div class="card"><div class="l">统计基数</div><div class="v">{total}</div>
    <div class="s">全量工单，含【禁】标记 {len(banned)} 条</div></div>
  <div class="card"><div class="l">时间跨度</div><div class="v" style="font-size:16px;">{span}</div>
    <div class="s">按实际服务时间</div></div>
  <div class="card"><div class="l">前三类合计</div><div class="v">{top3 * 100 / total:.1f}%</div>
    <div class="s">{top3} 条</div></div>
  <div class="card"><div class="l">TOP20 覆盖</div><div class="v">{covered * 100 / total:.1f}%</div>
    <div class="s">未分类 {len(unclassified)} 条（{len(unclassified) * 100 / total:.1f}%）</div></div>
</div>

<h2>统计口径</h2>
<div class="note">
  <b>【禁】类工单按正常数据统计。</b>「问题类型」列带【禁】前缀的类别（客户应用使用 840 /
  简易咨询 213 / 产品选型 37 等，合计 {len(banned)} 条），是分类体系更新细化后停止新登记使用，
  <b>数据本身有效</b>，本次全部计入统计，未做剔除。<br>
  分类方法：关键词规则聚类，只取「问题现象描述」字段，按优先级归入唯一类别（主标签）。
  同一工单若涉及多主题只计一次，因此<b>占比之和为 100%，不等于"提及率"</b>。
</div>

<h2>TOP20 类问题</h2>
<table>
  <thead>
    <tr><th>#</th><th>问题类别 / 典型现象</th><th class="num">条数</th>
        <th class="num">占比</th><th>主产品线</th><th>主要根因</th></tr>
  </thead>
  <tbody>{''.join(rows_html)}
  </tbody>
</table>

<h2>三条关键结论</h2>
<div class="find"><ol>
  <li><b>前三类吃掉 {top3 * 100 / total:.0f}%</b>：初始化/回零（{top[0][1]} 条）、
      力控/夹持力（{top[1][1]} 条）、报警代码（{top[2][1]} 条）。
      做知识库或新人培训，先啃这三类覆盖率最高。</li>
  <li><b>抖动单当调参单接。</b>抖动/异响类 {shake_n} 条里，根因是"客户参数设置不当"的有
      {shake_param} 条（{shake_param * 100 / shake_n:.0f}%），是该类第一大根因——
      先问增益/刚性/惯量参数，别先怀疑硬件。</li>
  <li><b>真硬件/固件问题占比很低。</b>固件 BUG 类只有 {fw_n} 条
      （{fw_n * 100 / total:.1f}%），"电机/编码器/硬件损坏"未进 TOP20。
      绝大多数是配置与用法问题，远程可解，最适合做成自助 Q&amp;A。</li>
</ol></div>

<h2>官方「问题类型」字段对照（同基数 {total} 条）</h2>
<p style="font-size:13px;color:var(--muted);margin:6px 0 0;">
  工单系统原始分类共 {len(official)} 类。粒度粗，且已停止新登记的【禁】类仍占
  {ban_pct:.1f}%，不建议直接拿来做知识库分类。</p>
<table>
  <thead><tr><th>问题类型</th><th class="num">条数</th><th class="num">占比</th><th>分布</th></tr></thead>
  <tbody>{off_html}</tbody>
</table>

<h2>交叉验证：噗元 FAQ（{len(pdata)} 条，2025-04-24）</h2>
<p style="font-size:13px;color:var(--muted);margin:6px 0 0;">
  独立数据源，排序与华东工单高度一致（初始化、力控同为前二），说明分类口径站得住。</p>
<table>
  <thead><tr><th>问题类别</th><th class="num">条数</th><th class="num">占比</th></tr></thead>
  <tbody>{p_html}</tbody>
</table>

<footer>
  复现方式：<code>python scripts/gen_faq_report.py</code>（生成 HTML）、
  <code>python scripts/analyze_faq_topics.py --all</code>（控制台明细，含噗元交叉验证）。<br>
  关键词表在 <code>scripts/analyze_faq_topics.py</code> 顶部 <code>RULES</code> 列表，顺序即优先级，改动后重跑即可。<br>
  表中"典型现象""代表工单"均为工单原文摘录，未做脱敏，便于回溯到原工单。
</footer>

</div>
</body>
</html>
'''


if __name__ == '__main__':
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_html(), encoding='utf-8')
    print('已生成：%s' % OUT)
