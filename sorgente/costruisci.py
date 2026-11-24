# Costruisce index.html da sorgente/pagina.html + font Archivo (incorporato: nessuna richiesta a server esterni).
# Uso:  python3 sorgente/costruisci.py            -> scrive index.html
#       python3 sorgente/costruisci.py ANTEPRIMA  -> scrive anche il frammento per l'anteprima Artifact
import base64
import pathlib
import sys

radice = pathlib.Path(__file__).resolve().parent.parent
pagina = (radice / "sorgente" / "pagina.html").read_text(encoding="utf-8")
font = base64.b64encode((radice / "sorgente" / "archivo-latin.woff2").read_bytes()).decode("ascii")
pagina = pagina.replace("__FONT_BASE64__", font)
if "__FONT_BASE64__" in pagina or "<!--FINE-TESTA-->" not in pagina:
    sys.exit("pagina.html non valida: mancano __FONT_BASE64__ o <!--FINE-TESTA-->")

if len(sys.argv) > 1:
    pathlib.Path(sys.argv[1]).write_text(pagina, encoding="utf-8")

testa, corpo = pagina.split("<!--FINE-TESTA-->", 1)
testa = testa.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
documento = (
    '<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + testa.strip() + "\n</head>\n<body>\n" + corpo.strip() + "\n</body>\n</html>\n"
)
(radice / "index.html").write_text(documento, encoding="utf-8")
print("index.html scritto:", len(documento), "caratteri")
