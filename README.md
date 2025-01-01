# price-comparison-website

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
