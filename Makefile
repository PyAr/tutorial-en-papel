# Configuration

CPYTHON_PATH        := cpython   # Current commit for this upstream repo is setted by the submodule
BRANCH              := 3.11
LANGUAGE            := es

# Internal variables
VENV                   := python-docs-es/$(shell realpath ./venv)
CPYTHON_WORKDIR        := cpython
OUTPUT_LATEX           := _build/latex

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo " build        Build the PDF for the Tutorial"
	@echo ""


.PHONY: build
build: setup
	cd python-docs-es && git checkout -- conf.py
	cat _conf.py >> python-docs-es/conf.py
	cd python-docs-es && make build
	cd python-docs-es && PYTHONWARNINGS=ignore::FutureWarning,ignore::RuntimeWarning $(VENV)/bin/sphinx-build -j auto -W --keep-going -b latex -d $(OUTPUT_DOCTREE) -D language=$(LANGUAGE) . $(OUTPUT_LATEX)
	cd $(OUTPUT_LATEX) && make all-pdf


.PHONY: setup
setup:
	git clone --depth 1 https://github.com/python/python-docs-es/ || true
	cd python-docs-es && git reset --hard origin/$(BRANCH)
	cd python-docs-es && git submodule sync
	cd python-docs-es && git submodule update --init --force --depth 1 $(CPYTHON_PATH)


.PHONY: clean
clean:
	rm -rf $(VENV)
	rm -rf $(OUTPUT_LATEX)
	rm -rf $(OUTPUT_DOCTREE)
