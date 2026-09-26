"""Renderiza una muestra de tarjetas del .apkg como HTML para revisarlas visualmente.

Uso: .venv/bin/python preview.py [salida.html] [n_muestras]
"""
import html
import json
import os
import re
import sqlite3
import sys
import tempfile
import zipfile

APKG = sys.argv[4] if len(sys.argv) > 4 else "/tmp/opencode/Ingles-Grammar-B1C2.apkg"
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/opencode/preview.html"
N = int(sys.argv[2]) if len(sys.argv) > 2 else 12
ONLY = sys.argv[3] if len(sys.argv) > 3 else None


def render(tpl, fields, is_back, front_html=None):
    # 1) condicionales {{#campo}}...{{/campo}}  (antes de tocar {{campo}})
    tpl = re.sub(r"\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}",
                 lambda m: m.group(2) if fields.get(m.group(1), "").strip() else "",
                 tpl, flags=re.S)

    def rep(m):
        name = m.group(1).strip()
        if name.lower() == "frontside":
            return front_html or ""
        if name.lower().startswith("cloze:"):
            return cloze_render(fields.get(name.split(":", 1)[1], ""),
                                1 if is_back else 0)
        return fields.get(name, "")
    return re.sub(r"\{\{([^}]+)\}\}", rep, tpl)


def cloze_render(texto, ord_):
    if ord_ == 0:
        return re.sub(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}", r"[...]", texto)
    def rep(m):
        n, body = int(m.group(1)), m.group(2)
        if ":" in body:
            body = body.split("::", 1)[0]
        return f'<span class="cloze">[{body}]</span>' if n == ord_ else body
    return re.sub(r"\{\{c(\d+)::(.*?)\}\}", rep, texto)


def main():
    z = zipfile.ZipFile(APKG)
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.write(z.read([n for n in z.namelist() if n.endswith(".anki2")][0]))
    tmp.close()
    con = sqlite3.connect(tmp.name)
    col = json.loads(con.execute("select models from col").fetchone()[0])

    rows = con.execute(
        "select mid, flds from notes order by random()").fetchall()
    if ONLY:
        want = {int(k) for k, v in col.items()
                if ONLY.lower() in v["name"].lower()}
        rows = [r for r in rows if r[0] in want]
    picks = []
    for mid, flds in rows:
        model = col[str(mid)]
        names = [f["name"] for f in model["flds"]]
        vals = flds.split("\x1f")
        fields = dict(zip(names, vals))
        decks = con.execute(
            "select d.name from cards c join decks d on c.did=d.id "
            "where c.nid=notes.id", ()).fetchall() if False else None
        picks.append((model, fields))
        if len(picks) >= N:
            break

    blocks = []
    for model, fields in picks:
        t = model["tmpls"][0]
        front = render(t["qfmt"], fields, False)
        back = render(t["afmt"], fields, True, front)
        blocks.append(
            f'<section class="demo"><h3>{html.escape(model["name"])}</h3>'
            f'<div class="pane"><div class="lbl">ANVERSO</div>{front}</div>'
            f'<div class="pane back"><div class="lbl">REVERSO</div>{back}</div>'
            "</section>")

    css = col[list(col)[0]]["css"]
    doc = f"""<!doctype html><meta charset="utf-8">
<title>preview</title><style>{css}
body{{margin:0;background:#eee;font-family:system-ui}}
.demo{{background:#fff;margin:18px;padding:14px;border-radius:12px;
      box-shadow:0 1px 4px #0002}}
h3{{font:700 12px/1 monospace;color:#888;letter-spacing:.5px;
   text-transform:uppercase;margin:0 0 10px}}
.pane{{border:1px solid #ddd;border-radius:8px;padding:10px 12px;margin-bottom:8px}}
.pane .lbl{{font:700 10px monospace;color:#aaa;letter-spacing:1px;margin-bottom:6px}}
.raw{{font:11px monospace;color:#888;background:#fafafa;padding:6px;border-radius:6px}}
</style>{''.join(blocks)}"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print("escrito", OUT, len(picks), "muestras")


if __name__ == "__main__":
    main()
