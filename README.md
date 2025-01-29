Example of a modern Python package with a command line interface.

We can test the package installation in virtual environment as follows:

Install locally:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install .
```

Install from Git:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install git+https://github.com/CSCfi/pypackage@v0.1.0
```
