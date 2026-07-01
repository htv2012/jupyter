help:
	@echo make lab 
	@echo make py
	@echo make b
	@echo make pt

lab:
	uv run jupyter lab --notebook-dir=notebooks --no-browser

py:
	uv run ipython

b:
	uv run bpython

pt:
	uv run ptpython --config-file config.py

