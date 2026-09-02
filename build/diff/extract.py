import pdfplumber, sys, os, io, json

files = {
 "v33": r"D:/AI/DH_DataBase/raw/manuals/使用手册/标准使用手册/PGIA.PGEA系列电爪操作手册V3.3.pdf",
 "v34": r"D:/AI/DH_DataBase/raw/manuals/使用手册/标准使用手册/PGIA.PGEA系列操作手册V3.4.pdf",
}
out = {}
for k, p in files.items():
    pages = []
    with pdfplumber.open(p) as pdf:
        for i, pg in enumerate(pdf.pages, 1):
            t = pg.extract_text() or ""
            pages.append({"page": i, "text": t})
    out[k] = pages
    print(k, "pages:", len(pages), "chars:", sum(len(x["text"]) for x in pages))

os.makedirs(r"D:/AI/DH_DataBase/build/diff", exist_ok=True)
with open(r"D:/AI/DH_DataBase/build/diff/extracted.json","w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=1)
for k in out:
    with open(rf"D:/AI/DH_DataBase/build/diff/{k}.txt","w",encoding="utf-8") as f:
        for p in out[k]:
            f.write(f"\n===== PAGE {p['page']} =====\n{p['text']}\n")
