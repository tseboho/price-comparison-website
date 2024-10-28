import src.vendor.picknpay
import src.vendor.woolworths

import json

print(
    json.dumps(
        src.vendor.woolworths.product_search(
            user_query="croissant",
            max_n_items=4,
        ),
        indent=4,
        default=str,
    )
)

for x in src.vendor.picknpay.product_search(
    user_query="croissant",
    max_n_items=4,
):
    print(x)
