# Configuration

CPYTHON_PATH        := cpython   # Current commit for this upstream repo is setted by the submodule
BRANCH              := 3.11
LANGUAGE            := es

# Internal variables
OUTPUT_LATEX           := _build/latex
OUTPUT_DOCTREE         := _build/doctree
CPYTHON_WORKDIR        := python-docs-es/cpython
CPYTHON_DOC            := python-docs-es/cpython/Doc

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo " pdf        Build the PDF for the Tutorial"
	@echo ""


.PHONY: fix-paths
fix-paths: setup
	# NOTE: copied from `python-docs-es` to avoid hacking their Makefile
	# FIXME: Relative paths for includes in 'cpython'
	# See more about this at https://github.com/python/python-docs-es/issues/1844
	sed -i -e 's|.. include:: ../includes/wasm-notavail.rst|.. include:: ../../../../includes/wasm-notavail.rst|g' $(CPYTHON_DOC)/**/*.rst
	sed -i -e 's|.. include:: ../distutils/_setuptools_disclaimer.rst|.. include:: ../../../../distutils/_setuptools_disclaimer.rst|g' $(CPYTHON_DOC)/**/*.rst
	sed -i -e 's|.. include:: ./_setuptools_disclaimer.rst|.. include:: ../../../_setuptools_disclaimer.rst|g' $(CPYTHON_DOC)/**/*.rst
	sed -i -e 's|.. include:: token-list.inc|.. include:: ../../../token-list.inc|g' $(CPYTHON_DOC)/**/*.rst
	sed -i -e 's|.. include:: ../../using/venv-create.inc|.. include:: ../using/venv-create.inc|g' $(CPYTHON_DOC)/**/*.rst
	sed -i -e 's|.. include:: ../../../using/venv-create.inc|.. include:: ../../using/venv-create.inc|g' $(CPYTHON_DOC)/**/*.rst
	sed -i -e 's|.. include:: /using/venv-create.inc|.. include:: ../../../../using/venv-create.inc|g' $(CPYTHON_DOC)/**/*.rst


.PHONY: setup
setup:
	git clone --depth 1 https://github.com/python/python-docs-es/ || true
	cd python-docs-es && git pull

  # Sync CPython Git submodule
	cd python-docs-es && git submodule sync
	cd python-docs-es && git submodule update --init --force --depth 1

	cd python-docs-es && git checkout -- conf.py
	cat _conf.py >> python-docs-es/conf.py


.PHONY: adapts-chapters
adapt-chapters: setup
	# TODO: figure it out how to include the initial page:
	# https://github.com/cacrespo/tutorial_python_ES/issues/8#issuecomment-1298318203
	# sed -i -e 's|appetite.rst|initial.rst\n   appetite.rst|g' $(CPYTHON_DOC)/tutorial/index.rst

	# Remove this chapters because we don't want them in the printed version
	sed -i -e 's|interactive.rst||g' $(CPYTHON_DOC)/tutorial/index.rst
	sed -i -e 's|floatingpoint.rst||g' $(CPYTHON_DOC)/tutorial/index.rst
	sed -i -e 's|appendix.rst||g' $(CPYTHON_DOC)/tutorial/index.rst

	cp _contents.rst $(CPYTHON_DOC)/contents.rst


.PHONY: apply-patches
apply-patches: setup
	cd python-docs-es/cpython && git apply ../../patches/*


.PHONY: venv
venv: setup
	cd python-docs-es && make venv


.PHONY: latex
latex: setup venv fix-paths adapt-chapters apply-patches
	cd python-docs-es && PYTHONWARNINGS=ignore::FutureWarning,ignore::RuntimeWarning venv/bin/sphinx-build -j auto --keep-going -b latex -d $(OUTPUT_DOCTREE) -D language=$(LANGUAGE) . $(OUTPUT_LATEX)


.PHONY: pdf
pdf: latex
	# Remove empty footnotes
	# FIXME: this should be done via Sphinx properly
	sed -i -e 's|\\subsubsection\*{Notas al pie}||g' python-docs-es/$(OUTPUT_LATEX)/Tutorial-Python_Python-Argentina.tex
	cd python-docs-es/$(OUTPUT_LATEX) && make all-pdf


.PHONY: clean
clean:
	rm -rf python-docs-es/venv
	rm -rf python-docs-es/$(OUTPUT_LATEX)
	rm -rf python-docs-es/$(OUTPUT_DOCTREE)
	rm -rf $(CPYTHON_DOC)/build/doctree
	cd python-docs-es && git reset --hard origin/$(BRANCH)
	cd python-docs-es/cpython && git reset --hard b3cafb6
