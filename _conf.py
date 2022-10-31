# Define the document to build with LaTeX
latex_documents = [
    ('tutorial/index', 'Tutorial-Python_Python-Argentina.tex', u'Tutorial de Python',
     _stdauthor, 'manual'),
]

# Configure PDF building for PRINTED version of the Tutorial
# https://www.sphinx-doc.org/en/master/latex.html
latex_elements = {
    'papersize': 'a5paper',
    'sphinxsetup': 'verbatimwithframe=false, verbatimhintsturnover=false',
    'fontpkg': r'''
\setmainfont{FreeSerif}[
  Extension      = .otf,
  UprightFont    = *,
  ItalicFont     = *Italic,
  BoldFont       = *Bold,
  BoldItalicFont = *BoldItalic,
  Scale          = 0.9
]
\setsansfont{FreeSans}[
  Extension      = .otf,
  UprightFont    = *,
  ItalicFont     = *Oblique,
  BoldFont       = *Bold,
  BoldItalicFont = *BoldOblique,
  Scale          = 0.9
]
\setmonofont{FreeMono}[
  Extension      = .otf,
  UprightFont    = *,
  ItalicFont     = *Oblique,
  BoldFont       = *Bold,
  BoldItalicFont = *BoldOblique,
  Scale          = 0.9
]
''',
    'geometry': r'''\usepackage{geometry}\geometry{ right=10mm, left=20mm }''',
    'hyperref': r'''\usepackage[hidelinks]{hyperref}''',
    'maketitle': r'''
\includepdf[pages=-]{../../../extra-pages/cover-front.pdf}

\newpage

\section*{Comentarios iniciales}
\addcontentsline{toc}{section}{Comentarios iniciales}

\sphinxAtStartPar
En reiteradas oportunidades Python Argentina
tradujo al castellano y editó en papel el «Tutorial de
Python» para mayor difusión de nuestro lenguaje.

\sphinxAtStartPar
Hoy dicho tutorial, que no es otra cosa que el
presente material, se entronca en el esfuerzo de
numerosas personas hispanoparlantes de todo el
mundo que han colaborado para traducir y
disponibilizar en español la totalidad de la
documentación (¡no sólo el tutorial!).

\sphinxAtStartPar
Con mucha alegría esperamos que este material
rompa barreras idiomáticas y sea una puerta de
entrada para todas aquellas personas de buena
voluntad que se quieran sumergir e iniciar en el
fascinante mundo del lenguaje de programación
Python.

\sphinxAtStartPar
Para mayor información visitar:
\sphinxurl{https://github.com/python/python-docs-es}
''',
    'preamble': r'''
\usepackage{pdfpages}
\newif\ifsphinxverbatimwithminipage \sphinxverbatimwithminipagetrue
''',
    'passoptionstopackages': r'\PassOptionsToPackage{gray}{xcolor}',
    'fvset': r'''\fvset{fontsize=\footnotesize}''',
    'printindex': r'''
\includepdf[pages=-]{../../../extra-pages/cover-back.pdf}
''',
}
latex_show_urls = 'inline'

# Not sure if this is required or not
latex_docclass = {
    'manual': 'book'
}

# Override appendices to remove license, about, etc
latex_appendices = [] # ['glossary']
