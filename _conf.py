# Define the document to build with LaTeX
latex_documents = [
    (
        'tutorial/index',
        'Tutorial-Python_Python-Argentina.tex',
        u'Tutorial de Python',
        _stdauthor,
        'manual'
    ),
]

# Configure PDF building for PRINTED version of the Tutorial
# https://www.sphinx-doc.org/en/master/latex.html
latex_elements = {
    'papersize': 'a5paper',
    'sphinxsetup': 'verbatimwithframe=false, verbatimhintsturnover=false',
    'pointsize': '9pt',
    'fontpkg': r'''
\usepackage[familydefault]{Rosario}
\setmonofont{Fira Code}
\usepackage[T1]{fontenc}
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
% Make the code inside the paragraphs to be gray
\protected\def\sphinxcode#1{\textcolor{gray}{\texttt{#1}}}

\usepackage{pdfpages}
\newif\ifsphinxverbatimwithminipage \sphinxverbatimwithminipagetrue
''',
    'passoptionstopackages': r'\PassOptionsToPackage{gray}{xcolor}',
    'fvset': r'''\fvset{fontsize=\footnotesize}''',
    'printindex': r'''
\includepdf[pages=-]{../../../extra-pages/cover-back.pdf}
''',
}
latex_show_urls = 'footnote'

# Not sure if this is required or not
latex_docclass = {
    'manual': 'book'
}

# Override appendices to remove license, about, etc
latex_appendices = [] # ['glossary']


# Use intersphinx to resolve links to content not included in the tutorial.
# See:
# https://github.com/PyAr/tutorial-en-papel/issues/18
# https://github.com/PyAr/tutorial-en-papel/issues/25#issuecomment-1311679864
#
# Doc: https://www.sphinx-doc.org/en/master/usage/quickstart.html#intersphinx
extensions.append('sphinx.ext.intersphinx')
intersphinx_mapping = {'python': ('https://docs.python.org/es/3', None)}
