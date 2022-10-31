# Configuration

CPYTHON_PATH        := cpython   # Current commit for this upstream repo is setted by the submodule
BRANCH              := 3.11
LANGUAGE            := es

# Internal variables
VENV                   := $(shell realpath ./python-docs-es/venv)
OUTPUT_LATEX           := _build/latex
CPYTHON_WORKDIR        := python-docs-es/cpython
OUTPUT_DOCTREE         := $(CPYTHON_WORKDIR)/Doc/build/doctree

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo " pdf        Build the PDF for the Tutorial"
	@echo ""


.PHONY: setup
setup:
	git clone --depth 1 https://github.com/python/python-docs-es/ || true
	# cd python-docs-es && git reset --hard origin/$(BRANCH)
	# cd python-docs-es && git submodule sync
	# cd python-docs-es && git submodule update --init --force --depth 1 $(CPYTHON_PATH)


.PHONY: build
build: setup
	# Remove chapters/files we don't want in the final tutorial
	cat _Makefile >> python-docs-es/Makefile
	sed -i -e 's|build: setup|build: setup tutorial-index|g' python-docs-es/Makefile

	# Remove "treat warnings as errors": there are some files that are not included
	sed -i -e 's|-W --keep-going|--keep-going|g' python-docs-es/Makefile

	cd python-docs-es && git checkout -- conf.py
	cat _conf.py >> python-docs-es/conf.py
	cd python-docs-es && make build


.PHONY: latex
latex: build
	cd python-docs-es && PYTHONWARNINGS=ignore::FutureWarning,ignore::RuntimeWarning $(VENV)/bin/sphinx-build -j auto --keep-going -b latex -d $(OUTPUT_DOCTREE)/tutorial -D language=$(LANGUAGE) . $(OUTPUT_LATEX)


.PHONY: pdf
pdf: latex
	cd python-docs-es/$(OUTPUT_LATEX) && make all-pdf


.PHONY: clean
clean:
	rm -rf $(VENV)
	rm -rf $(OUTPUT_LATEX)
	rm -rf $(OUTPUT_DOCTREE)
	cd python-docs-es && git reset --hard origin/$(BRANCH)
