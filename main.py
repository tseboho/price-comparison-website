import src.vendor.woolworths

import json

print(
    json.dumps(
        src.vendor.woolworths.product_search(
            user_query="full cream yoghurt",
            max_n_items=4,
        ),
        indent=4,
        default=str,
    )
)
