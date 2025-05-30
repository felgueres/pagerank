.PHONY: env install shell

VENV = learning

env:
	python3 -m venv $(VENV)

install: env
	$(VENV)/bin/python -V
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

shell:
	@zsh -c "source $(VENV)/bin/activate && zsh"