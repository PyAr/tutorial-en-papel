# Define the document to build with LaTeX
latex_documents = [
    ('tutorial/index', 'Tutorial-Python_Python-Argentina.tex', u'Tutorial de Python',
     _stdauthor, 'manual'),
]

# Configure PDF building for PRINTED version of the Tutorial
# https://www.sphinx-doc.org/en/master/latex.html
#
# Install `latex-mk` and `texlive-latexextra` and `texlive-fontsextra`
# on the system using its own package manager
latex_elements = {
    'papersize': 'a5paper',
    'sphinxsetup': 'verbatimwithframe=false',
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
    'geometry': r'''\usepackage{geometry}\geometry{ right=20mm, left=10mm }''',
    'hyperref': r'''\usepackage[hidelinks]{hyperref}''',
    'maketitle': r'''
\includepdf[pages=-]{../../tutorial_python_ES/portada/cover-front.pdf}
''',
    'preamble': r'''
\usepackage{pdfpages}
''',
    'passoptionstopackages': r'\PassOptionsToPackage{gray}{xcolor}',
    'fvset': r'''\fvset{fontsize=\footnotesize}''',
    'printindex': r'''
\renewcommand{\indexname}{Índice}
\printindex
\includepdf[pages=-]{../../tutorial_python_ES/portada/cover-back.pdf}
''',
}
latex_show_urls = 'inline'
