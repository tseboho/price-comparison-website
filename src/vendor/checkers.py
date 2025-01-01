import requests

from src.obj import ItemSearchResult


def product_search(user_query: str, max_n_items: int) -> list[ItemSearchResult]:
    """
    TODO
    """

    response = requests.get(
        "https://www.checkers.co.za/search/all",
        params={
            "q": user_query,
        },
        # cookies=cookies,
        headers={
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            # Requests sorts cookies= alphabetically
            # 'cookie': f"anonymous-consents=%5B%5D; checkersZA-preferredStore=57861; cookie-notification=NOT_ACCEPTED; _gcl_au=1.1.1078152908.1733516554; cookie-promo-alerts-popup=true; webp_supported=true; _tt_enable_cookie=1; _ttp=7mUQVmvqtm3oCpmUUWpn43Nk-Qc.tt.2; _fbp=fb.2.1733516555632.425449188482098936; JSESSIONID=Y4-b6264870-34ec-44df-8963-0cacf3db0243; _gcl_gs=2.1.k1{i1735287089$u123273817;} _gcl_aw=GCL.1735287107.Cj0KCQiAvbm7BhC5ARIsAFjwNHvjQDpRIGKjcZIkx812rlacTVzLxmLweVjC3ZjrJGfTFyvvY-F741oaAm2QEALw_wcB; _gcl_dc=GCL.1735287107.Cj0KCQiAvbm7BhC5ARIsAFjwNHvjQDpRIGKjcZIkx812rlacTVzLxmLweVjC3ZjrJGfTFyvvY-F741oaAm2QEALw_wcB; _clck=brxw5x%7C2%7Cfs2%7C0%7C1801; _gac_UA-41901849-1=1.1735287114.Cj0KCQiAvbm7BhC5ARIsAFjwNHvjQDpRIGKjcZIkx812rlacTVzLxmLweVjC3ZjrJGfTFyvvY-F741oaAm2QEALw_wcB; _ga_KRLJETD70M=GS1.1.1735720343.4.0.1735720343.60.0.0; _ga=GA1.3.121653827.1733516555; _gid=GA1.3.1955401637.1735720344; _gat_UA-137468022-1=1; _uetsid=edd03880c81a11efb477fbfa70b9359c; _uetvid=d43b77b0b40f11ef9464fb386d1d40ef; __gads=ID=3a7a7df565850012:T=1733516555:RT=1735720345:S=ALNI_MbBtPikFLLnnvXFtXzlz14LGQvs_g; __gpi=UID=00000fb30d228a38:T=1733516555:RT=1735720345:S=ALNI_MaaTRctSgAQXEhLVV20ZjvnoNhWnw; __eoi=ID=1d858b3b967aaa5a:T=1733516555:RT=1735720345:S=AA-AfjZFNqireUAEbEw7ZzCGERUA; AWSALB=EPn2ix9J7ZcK7q7tg3XcVLhwdB5pn2ufnOPK9r9r4P50NFN3Rtm1emeBeTjcO3WoCP5mBfM3I1gbYLfd3ARrAGOSMdZUSaMM1wlLn/P6H77KIWGOkU39dl6uFpve; AWSALBCORS=EPn2ix9J7ZcK7q7tg3XcVLhwdB5pn2ufnOPK9r9r4P50NFN3Rtm1emeBeTjcO3WoCP5mBfM3I1gbYLfd3ARrAGOSMdZUSaMM1wlLn/P6H77KIWGOkU39dl6uFpve; _ga_SY8LS918MZ=GS1.3.1735720345.2.0.1735720346.59.0.0",
            "priority": "u=0, i",
            "referer": "https://www.checkers.co.za/",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        },
    )

    print(response)
