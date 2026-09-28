#!/usr/bin/env python3
"""barra_navegacion.py — agrega a las páginas del libro la etiqueta para celulares y una barra
de vuelta a la portada, al PDF y al otro idioma (auditoría D186: en el teléfono se veían en miniatura
y no había forma de volver). Idempotente: si la barra ya está, no la duplica.
Uso: python3 barra_navegacion.py  (desde publicacion/)
"""
import os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
PAGINAS = {
    "es/Simbiosis_2.0_Marco_Giribaldi.html": ("es", "Simbiosis_2.0_Marco_Giribaldi.pdf", "../en/Symbiosis_2.0_Marco_Giribaldi.html", "English"),
    "en/Symbiosis_2.0_Marco_Giribaldi.html": ("en", "Symbiosis_2.0_Marco_Giribaldi.pdf", "../es/Simbiosis_2.0_Marco_Giribaldi.html", "Español"),
    "history/Simbiosis_1.0_primeros_apuntes.html": ("es", "Simbiosis_1.0_primeros_apuntes.pdf", "Symbiosis_1.0_first_notes.html", "English"),
    "history/Symbiosis_1.0_first_notes.html": ("en", "Symbiosis_1.0_first_notes.pdf", "Simbiosis_1.0_primeros_apuntes.html", "Español"),
}
ESTILO = ('<style>.barra-simbiosis{position:sticky;top:0;z-index:9;display:flex;gap:18px;flex-wrap:wrap;align-items:center;'
          'padding:10px 16px;margin:-8px -8px 16px;background:#0c1113;font:500 14px/1.4 system-ui,sans-serif}'
          '.barra-simbiosis a{color:#9fd49f;text-decoration:none}.barra-simbiosis a:hover{text-decoration:underline}'
          '.barra-simbiosis .marca{color:#eef1ec;font-weight:600}</style>')

for ruta, (lang, pdf, otro, nombre_otro) in PAGINAS.items():
    p = os.path.join(RAIZ, ruta)
    s = open(p, encoding="utf-8").read()
    if 'class="barra-simbiosis"' in s:
        continue
    if 'name="viewport"' not in s:
        s = s.replace("<head>", '<head><meta name="viewport" content="width=device-width, initial-scale=1">', 1)
    volver = "../index.html"
    textos = {"es": ("← Portada", "PDF"), "en": ("← Home", "PDF")}[lang]
    barra = (f'{ESTILO}<nav class="barra-simbiosis" aria-label="Symbiosis"><a class="marca" href="{volver}">{textos[0]}</a>'
             f'<a href="{pdf}">{textos[1]}</a><a href="{otro}">{nombre_otro}</a></nav>')
    s = re.sub(r"(<body[^>]*>)", r"\1" + barra.replace("\\", "\\\\"), s, count=1)
    open(p, "w", encoding="utf-8").write(s)
    print("barra agregada:", ruta)
