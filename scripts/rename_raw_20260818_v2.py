# -*- coding: utf-8 -*-
"""
raw/ 资料文件规范化 v2（2026-08-18，最后一次操作原始文件）。
策略(按用户最新指示):
- 文件名主体不动，仅在扩展名前追加 _YYYYMMDD(最后修改日期)，仅限无内部版本号的文件；
  已有 v/V/Ver/_数字 版本号的保持原文件名；文件名末尾孤立 '-' 清理掉。
- 归类移到 MANIFEST.csv: 新增"适配产品线"列(多选, 分号分隔)。
- ECAT盒子 = 485->ECAT 网关, 适配产品线标 电缸;电爪。
"""
import os
import sys
import csv
from datetime import datetime

RAW = r"D:\AI\DH_DataBase\raw"
MANIFEST = os.path.join(RAW, "MANIFEST.csv")
FEED_DATE = "2026-08-18"

# (旧相对路径, 是否有内部版本号, 版本字符串, 类型, 适配产品线(分号分隔))
# 有版本号=True 时文件名保持; False 时追加 _YYYYMMDD
FILES = [
    ("manuals/usage/两段位置限制电流实现力控.pdf", False, "", "手册", "通用"),
    ("manuals/usage/天津丰津现场调研.pptx", False, "", "演示", "通用"),
    ("manuals/usage/上电自动初始化.mp4", False, "", "视频", "通用"),
    ("manuals/usage/RGD，RGI，RGIC夹爪固件升级手册-.docx", False, "", "手册", "电爪"),
    ("manuals/usage/XJC-608T-F操作说明SOP（2023.10.01）.pdf", False, "", "手册", "通用"),
    ("manuals/usage/IO模式开关_v20240413.mp4", True, "v20240413", "视频", "通用"),
    ("manuals/usage/ECAT盒子固件升级SOP_包括ESI与CFG.docx", False, "", "手册", "电缸;电爪"),
    ("manuals/usage/ECAT盒子固件升级SOP_仅升级ESI与CFG.docx", False, "", "手册", "电缸;电爪"),
    ("manuals/usage/旋转零点校准.docx", False, "", "手册", "通用"),
    ("manuals/usage/大寰电缸软重启SOP_v20240819.docx", True, "v20240819", "手册", "电缸"),
    ("manuals/usage/产品应用指导手册-电气篇v20241029.pdf", True, "v20241029", "手册", "通用"),
    ("manuals/usage/力控标定演示视频.mp4", False, "", "视频", "通用"),
    ("manuals/usage/大寰MCEA电缸操作手册_V4.0.pdf", True, "V4.0", "手册", "电缸"),
    ("manuals/usage/SAC-NF2-柔性力控使用手册_v20260305.docx", True, "v20260305", "手册", "通用"),
    ("manuals/usage/大寰电机SAC-NP2驱动参数导入导出SOP.pdf", False, "", "手册", "音圈电机"),
    ("manuals/usage/SAC-NP2 EtherCAT型双轴驱动器-产品操作手册 Ver-M-1.00.12 2025-10-07 #Manual.pdf", True, "Ver-M-1.00.12", "手册", "驱动器"),
    ("manuals/usage/SAC-N2驱动器初次上电SOP.pdf", False, "", "手册", "驱动器"),
    ("manuals/usage/鑫精诚力显示器参数修改说明.pdf", False, "", "手册", "通用"),
    ("manuals/usage/大寰电机调试SOP_V1.1.pdf", True, "V1.1", "手册", "音圈电机"),
    ("manuals/usage/PGIA.PGEA系列电爪操作手册V3.3.pdf", True, "V3.3", "手册", "电爪"),
    ("manuals/usage/PGLS电爪校准偏置值SOP-联赢激光0602.docx", False, "", "手册", "电爪"),
    ("manuals/usage/大寰电爪更改抱闸时间SOP_20240820.docx", True, "20240820", "手册", "电爪"),
    ("manuals/usage/SAC-N2 电机整定参考手册.md", False, "", "文档", "音圈电机"),
    ("manuals/usage/SAC系列驱动器USB升级操作指导文档.md", False, "", "文档", "驱动器"),
    ("manuals/usage/SAC-N2 EtherCAT应用手册.md", False, "", "文档", "音圈电机"),
    ("manuals/usage/SAC-N2 XML文件更新指导手册.md", False, "", "文档", "音圈电机;驱动器"),
    ("manuals/usage/SAC XML文件修改方法.md", False, "", "文档", "驱动器"),

    ("manuals/adaptation/基恩士KV8000&7500PLC适配DHetherCAT盒子SOP-.pdf", False, "", "手册", "电缸;电爪"),
    ("manuals/adaptation/三菱-卓岚-简单CPU通讯配置SOP_v20141119.docx", True, "v20141119", "手册", "通用"),
    ("manuals/adaptation/SAC_2Axis_V1.7.2对象字典.xlsx", True, "V1.7.2", "表格", "驱动器"),
    ("manuals/adaptation/SAC-N2-电缸&凌臣PCI系列控制卡工业适配技术样本v_000.docx", True, "v_000", "手册", "电缸"),
    ("manuals/adaptation/SAC-N2-音圈&凌臣PCI系列控制卡工业适配技术样本v_000.docx", True, "v_000", "手册", "音圈电机"),
    ("manuals/adaptation/SAC2-N1-音圈&固高GEN系列控制卡工业适配技术样本v_000.docx", True, "v_000", "手册", "音圈电机"),
    ("manuals/adaptation/SAC2-N1-音圈&凌臣PCI系列控制卡工业适配技术样本v_000.docx", True, "v_000", "手册", "音圈电机"),
    ("manuals/adaptation/SAC-N2-音圈&汇川IMC系列控制卡工业适配技术样本v_000.docx", True, "v_000", "手册", "音圈电机"),
    ("manuals/adaptation/SAC-NP4-音圈&汇川IMC系列控制卡工业适配技术样本v_000.docx", True, "v_000", "手册", "音圈电机"),
    ("manuals/adaptation/SAC-NP4-音圈&凌臣PCI系列控制卡工业适配技术样本v_000.docx", True, "v_000", "手册", "音圈电机"),
    ("manuals/adaptation/固高板卡适配大寰总线产品(电爪、音圈）_v20251019.pptx", True, "v20251019", "演示", "电爪;音圈电机"),

    ("manuals/troubleshooting/电缸报警代码解析_20241111.xlsx", True, "20241111", "表格", "电缸"),
    ("manuals/troubleshooting/SAC-N2 FAQ.md", False, "", "文档", "音圈电机"),

    ("manuals/selection/DH_电缸选型手册_中文版_1029.pdf", True, "1029", "手册", "电缸"),
]


def new_name_for(old_rel, has_version):
    old_path = os.path.join(RAW, old_rel)
    dirn, fname = os.path.split(old_path)
    base, ext = os.path.splitext(fname)
    if has_version:
        return fname  # 保持
    # 清理末尾孤立 '-'
    if base.endswith("-"):
        base = base[:-1]
    mdate = datetime.fromtimestamp(os.path.getmtime(old_path)).strftime("%Y%m%d")
    return f"{base}_{mdate}{ext}"


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "dry"
    rows = []
    print(f"MODE={mode}\n=== 文件名映射 ===")
    missing = []
    for old_rel, has_ver, ver, ftype, plines in FILES:
        old_path = os.path.join(RAW, old_rel)
        if not os.path.exists(old_path):
            missing.append(old_rel)
            print(f"[MISSING] {old_rel}")
            continue
        nn = new_name_for(old_rel, has_ver)
        print(f"{os.path.basename(old_path)}\n    -> {nn}")
        rows.append((nn, ftype, ver, "在库", FEED_DATE, plines))
    print(f"\n总计: {len(FILES)} | 缺失: {len(missing)}")

    # MANIFEST 预览
    print("\n=== MANIFEST.csv 预览(新增列: 适配产品线) ===")
    header = ["文件名", "类型", "版本", "状态", "最后投喂日", "适配产品线"]
    print(",".join(header))
    for r in rows:
        print(",".join(r))

    if mode == "exec":
        # 1) 重命名
        for old_rel, has_ver, ver, ftype, plines in FILES:
            old_path = os.path.join(RAW, old_rel)
            if not os.path.exists(old_path):
                continue
            nn = new_name_for(old_rel, has_ver)
            new_path = os.path.join(os.path.dirname(old_path), nn)
            if os.path.abspath(new_path) != os.path.abspath(old_path):
                os.rename(old_path, new_path)
        # 2) 写 MANIFEST
        with open(MANIFEST, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(header)
            for r in rows:
                w.writerow(r)
        print("\n[exec] 重命名完成, MANIFEST.csv 已更新。")


if __name__ == "__main__":
    main()
