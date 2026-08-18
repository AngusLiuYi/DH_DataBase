# -*- coding: utf-8 -*-
"""
raw/ 资料文件规范化重命名脚本（一次性操作，2026-08-18）。
模板: {产品线}-{型号}-{文档类型}_{版本或mdate}.{ext}
- 有版本号: 保留原版本字符串
- 无版本号: 用文件最后修改日期 YYYYMMDD 占位 {mdate} 动态替换
产品线前缀: 音圈电机 / 电缸 / 电爪 / 驱动器 / 通用
"""
import os
import sys
from datetime import datetime

RAW = r"D:\AI\DH_DataBase\raw"

# (旧相对路径, 新文件名)  新文件名含 {mdate} 表示用最后修改日期
MAPPING = [
    # ---- manuals/usage ----
    ("manuals/usage/两段位置限制电流实现力控.pdf",
     "通用-两段位置限制电流实现力控_{mdate}.pdf"),
    ("manuals/usage/天津丰津现场调研.pptx",
     "通用-天津丰津现场调研_{mdate}.pptx"),
    ("manuals/usage/上电自动初始化.mp4",
     "通用-上电自动初始化_{mdate}.mp4"),
    ("manuals/usage/RGD，RGI，RGIC夹爪固件升级手册-.docx",
     "电爪-RGD-RGI-RGIC-夹爪固件升级手册_{mdate}.docx"),
    ("manuals/usage/XJC-608T-F操作说明SOP（2023.10.01）.pdf",
     "通用-XJC-608T-F-操作说明SOP_{mdate}.pdf"),
    ("manuals/usage/IO模式开关_v20240413.mp4",
     "通用-IO模式开关_v20240413.mp4"),
    ("manuals/usage/ECAT盒子固件升级SOP_包括ESI与CFG.docx",
     "驱动器-ECAT盒子-固件升级SOP-包括ESI与CFG_{mdate}.docx"),
    ("manuals/usage/ECAT盒子固件升级SOP_仅升级ESI与CFG.docx",
     "驱动器-ECAT盒子-固件升级SOP-仅升级ESI与CFG_{mdate}.docx"),
    ("manuals/usage/旋转零点校准.docx",
     "通用-旋转零点校准_{mdate}.docx"),
    ("manuals/usage/大寰电缸软重启SOP_v20240819.docx",
     "电缸-通用-软重启SOP_v20240819.docx"),
    ("manuals/usage/产品应用指导手册-电气篇v20241029.pdf",
     "通用-产品应用指导手册-电气篇_v20241029.pdf"),
    ("manuals/usage/力控标定演示视频.mp4",
     "通用-力控标定演示视频_{mdate}.mp4"),
    ("manuals/usage/大寰MCEA电缸操作手册_V4.0.pdf",
     "电缸-MCEA-操作手册_V4.0.pdf"),
    ("manuals/usage/SAC-NF2-柔性力控使用手册_v20260305.docx",
     "通用-SAC-NF2-柔性力控使用手册_v20260305.docx"),
    ("manuals/usage/大寰电机SAC-NP2驱动参数导入导出SOP.pdf",
     "音圈电机-SAC-NP2-驱动参数导入导出SOP_{mdate}.pdf"),
    ("manuals/usage/SAC-NP2 EtherCAT型双轴驱动器-产品操作手册 Ver-M-1.00.12 2025-10-07 #Manual.pdf",
     "驱动器-SAC-NP2-双轴驱动器产品操作手册_Ver-M-1.00.12.pdf"),
    ("manuals/usage/SAC-N2驱动器初次上电SOP.pdf",
     "驱动器-SAC-N2-驱动器初次上电SOP_{mdate}.pdf"),
    ("manuals/usage/鑫精诚力显示器参数修改说明.pdf",
     "通用-鑫精诚力显示器参数修改说明_{mdate}.pdf"),
    ("manuals/usage/大寰电机调试SOP_V1.1.pdf",
     "音圈电机-通用-调试SOP_V1.1.pdf"),
    ("manuals/usage/PGIA.PGEA系列电爪操作手册V3.3.pdf",
     "电爪-PGIA-PGEA-操作手册_V3.3.pdf"),
    ("manuals/usage/PGLS电爪校准偏置值SOP-联赢激光0602.docx",
     "电爪-PGLS-校准偏置值SOP-联赢激光0602_{mdate}.docx"),
    ("manuals/usage/大寰电爪更改抱闸时间SOP_20240820.docx",
     "电爪-通用-更改抱闸时间SOP_20240820.docx"),
    ("manuals/usage/SAC-N2 电机整定参考手册.md",
     "音圈电机-SAC-N2-电机整定参考手册_{mdate}.md"),
    ("manuals/usage/SAC系列驱动器USB升级操作指导文档.md",
     "驱动器-SAC系列-USB升级操作指导文档_{mdate}.md"),
    ("manuals/usage/SAC-N2 EtherCAT应用手册.md",
     "音圈电机-SAC-N2-EtherCAT应用手册_{mdate}.md"),
    ("manuals/usage/SAC-N2 XML文件更新指导手册.md",
     "音圈电机-SAC-N2-XML文件更新指导手册_{mdate}.md"),
    ("manuals/usage/SAC XML文件修改方法.md",
     "驱动器-SAC-XML文件修改方法_{mdate}.md"),

    # ---- manuals/adaptation ----
    ("manuals/adaptation/基恩士KV8000&7500PLC适配DHetherCAT盒子SOP-.pdf",
     "驱动器-ECAT盒子-基恩士KV8000&7500PLC适配SOP_{mdate}.pdf"),
    ("manuals/adaptation/三菱-卓岚-简单CPU通讯配置SOP_v20141119.docx",
     "通用-三菱-卓岚-简单CPU通讯配置SOP_v20141119.docx"),
    ("manuals/adaptation/SAC_2Axis_V1.7.2对象字典.xlsx",
     "驱动器-SAC-2Axis-对象字典_V1.7.2.xlsx"),
    ("manuals/adaptation/SAC-N2-电缸&凌臣PCI系列控制卡工业适配技术样本v_000.docx",
     "电缸-SAC-N2-凌臣PCI系列控制卡工业适配技术样本_v_000.docx"),
    ("manuals/adaptation/SAC-N2-音圈&凌臣PCI系列控制卡工业适配技术样本v_000.docx",
     "音圈电机-SAC-N2-凌臣PCI系列控制卡工业适配技术样本_v_000.docx"),
    ("manuals/adaptation/SAC2-N1-音圈&固高GEN系列控制卡工业适配技术样本v_000.docx",
     "音圈电机-SAC2-N1-固高GEN系列控制卡工业适配技术样本_v_000.docx"),
    ("manuals/adaptation/SAC2-N1-音圈&凌臣PCI系列控制卡工业适配技术样本v_000.docx",
     "音圈电机-SAC2-N1-凌臣PCI系列控制卡工业适配技术样本_v_000.docx"),
    ("manuals/adaptation/SAC-N2-音圈&汇川IMC系列控制卡工业适配技术样本v_000.docx",
     "音圈电机-SAC-N2-汇川IMC系列控制卡工业适配技术样本_v_000.docx"),
    ("manuals/adaptation/SAC-NP4-音圈&汇川IMC系列控制卡工业适配技术样本v_000.docx",
     "音圈电机-SAC-NP4-汇川IMC系列控制卡工业适配技术样本_v_000.docx"),
    ("manuals/adaptation/SAC-NP4-音圈&凌臣PCI系列控制卡工业适配技术样本v_000.docx",
     "音圈电机-SAC-NP4-凌臣PCI系列控制卡工业适配技术样本_v_000.docx"),
    ("manuals/adaptation/固高板卡适配大寰总线产品(电爪、音圈）_v20251019.pptx",
     "通用-固高板卡适配大寰总线产品-电爪-音圈_v20251019.pptx"),

    # ---- manuals/troubleshooting ----
    ("manuals/troubleshooting/电缸报警代码解析_20241111.xlsx",
     "电缸-通用-报警代码解析_20241111.xlsx"),
    ("manuals/troubleshooting/SAC-N2 FAQ.md",
     "音圈电机-SAC-N2-FAQ_{mdate}.md"),

    # ---- manuals/selection ----
    ("manuals/selection/DH_电缸选型手册_中文版_1029.pdf",
     "电缸-通用-选型手册-中文版_1029.pdf"),
]


def resolve_new_name(old_rel, new_tpl):
    old_path = os.path.join(RAW, old_rel)
    if "{mdate}" in new_tpl:
        mtime = os.path.getmtime(old_path)
        mdate = datetime.fromtimestamp(mtime).strftime("%Y%m%d")
        new_tpl = new_tpl.replace("{mdate}", mdate)
    return new_tpl


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "dry"
    print(f"MODE={mode}\n")
    conflicts = []
    missing = []
    for old_rel, new_tpl in MAPPING:
        old_path = os.path.join(RAW, old_rel)
        if not os.path.exists(old_path):
            missing.append(old_rel)
            print(f"[MISSING] {old_rel}")
            continue
        new_name = resolve_new_name(old_rel, new_tpl)
        new_path = os.path.join(os.path.dirname(old_path), new_name)
        flag = ""
        if os.path.exists(new_path) and os.path.abspath(new_path) != os.path.abspath(old_path):
            conflicts.append(new_name)
            flag = "  <== CONFLICT"
        print(f"{old_rel}\n    -> {new_name}{flag}")
        if mode == "exec" and not conflicts:
            os.rename(old_path, new_path)
    print(f"\n总计: {len(MAPPING)} 条映射 | 缺失: {len(missing)} | 冲突: {len(conflicts)}")
    if conflicts:
        print("冲突文件(未执行):", conflicts)


if __name__ == "__main__":
    main()
