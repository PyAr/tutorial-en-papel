# tutorial_python_ES
Versión del Tutorial Oficial de Python en español con ajustes para facilitar la impresión "en papel".

El proceso consiste en exportar los archivos LaTex del bloque del tutorial, modificar algunas cuestiones generales (tamaño de la hoja, márgenes, colores, etc.) y luego generar un archivo `pdf` donde impactamos retoques finales.

# Paso a paso para construir el material
## Generar archivos 'base'
1. Crear una copia local del [repositorio oficial de la documentación](https://github.com/python/python-docs-es).
2. Modificar en `conf.py` la entrada 'latex_documents':
̣
```python
latex_documents = [
    ('tutorial/index', 'python-docs-es.tex', u'Documentación de Python en Español',
     _stdauthor, 'manual'),
]
```
3. Hacer un build local
```bash
make build
```
y luego ejecutar
```bash
sphinx-build -j auto -W --keep-going -b latex -d cpython/Doc/build/doctree/tutorial -D language=es . tutorial_latex
```
Si todo fue bien, en la ruta `.../tutorial_latex` tendremos todos los archivos necesarios para continuar el proceso (los mismos que están en este repositorio).

## Ajustes en archivos '.tex'
### python-docs-es.tex
Añadir / modificar:
- `\documentclass[a5paper,10pt,spanish]{sphinxmanual}` tamaño de la hoja

- `
\usepackage{geometry}
\geometry{
 right=20mm
 }` margen para imprimir 

- `\title{Tutorial de Python}
\release{3.10}` información que se replica en los encabezados 

- `\usepackage[gray]{xcolor}` el coloreado pasa a escala de grises. Se puede utilizar _[monochrome]_ para que directamente todo quede en negro.
- `\fvset{fontsize=\footnotesize}` achica el tamaño de fuente en los bloques de sintaxis.
- En las lineas 24 y ss. se definen los tres tipos de letras que se usan en todo el documento. Incluir el parámetro `Scale=0.9` en cada una para achicar el tamaño.

Eliminar:
- todas las entradas `\subsubsection*{Notas al pie}` 
- Entradas desde la linea 5678 en adelante (capítulos 14 y ss.) y finalizar el archivo con:
```
(...)
\renewcommand{\indexname}{Índice}
\printindex
\end{document}
```
Las notas no se pierden y el índice se renderiza automáticamente.

---
### sphinx.sty

`\DeclareBoolOption[false]{verbatimwithframe}` cambiar a `false` para quitar recuadro en bloque de sintaxis

`\newif\ifsphinxverbatimwithminipage   \sphinxverbatimwithminipagetrue` cambiar a `true` para evitar quiebre de página en bloques de código.

Cambiar `\fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}` por `\fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\rightmark}}}` (es decir, queda dos veces la misma linea en todo el bloque). De este modo, evitamos que algunos pie de página se corrompan por tener un nombre de capitulo largo. 

