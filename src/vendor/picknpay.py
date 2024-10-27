import requests

from src.obj import ItemSearchResult


def product_search(user_query: str, max_n_items: int) -> list[ItemSearchResult]:
    """
    TODO
    """

    response = requests.post(
        url="https://www.pnp.co.za/pnphybris/v2/pnp-spa/products/search",
        params={
            "query": user_query,
            "pageSize": max_n_items,
            "storeCode": "WC44",
            "lang": "en",
            "curr": "ZAR",
        },
        headers={
            "Content-Type": "application/json",
            "origin": "https://www.pnp.co.za",
            "referer": f"https://www.pnp.co.za/search/{requests.utils.quote(user_query)}",
            "User-Agent": "Please let me in",
        },
    )

    items_info_raw = response.json()
    # items_info_raw: list[dict] = response.json()["contents"][0]["mainContent"][0][
    #     "contents"
    # ][0]["records"]
    # if len(items_info_raw) > max_n_items:
    #     items_info_raw = items_info_raw[:max_n_items]
    #
    # items_info: list[dict] = [
    #     {
    #         "item_title": item["attributes"]["p_displayName"],
    #         "item_image_url": item["attributes"]["p_externalImageReference"],
    #         "item_prices": item["startingPrice"],
    #     }
    #     for item in items_info_raw
    # ]
    return items_info
