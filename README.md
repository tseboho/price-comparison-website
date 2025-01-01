# price-comparison-website

A manual search on the command line:
```bash
item="romany creams"
uv run python -m src.dev.cli_product_search woolworths "${item}" 5
uv run python -m src.dev.cli_product_search picknpay "${item}" 5
uv run python -m src.dev.cli_product_search checkers "${item}" 5
```
