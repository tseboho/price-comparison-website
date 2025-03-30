# price-comparison-website

## Required Packages

To run this program, you need to install the following packages:

```bash
pip install -r requirements.txt
```

Note: The `uv` command is a shorthand for `uvicorn`, which is used to run ASGI applications.

## Running the app

Launch as a web app:

```bash
uv run fastapi run --port 8000 main.py
# then navigate in browser to http://0.0.0.0:8000/
```

A manual search on the command line:

```bash
item="romany creams"
uv run python -m src.dev.cli_product_search woolworths "${item}" 5
uv run python -m src.dev.cli_product_search picknpay "${item}" 5
uv run python -m src.dev.cli_product_search checkers "${item}" 5
```
