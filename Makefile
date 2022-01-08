VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
run: $(VENV)/bin/activate
dump: ./entrypoint.sh
clean:
  rm -rf __pycache__
  rm -rf $(VENV)
build: run dump clean
