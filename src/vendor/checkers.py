import requests

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    # 'cookie': 'anonymous-consents=%5B%5D; checkersZA-preferredStore=57861; cookie-notification=NOT_ACCEPTED; JSESSIONID=Y59-0c37c90c-cdb9-4cb6-a8d5-05bce11a8532; _gcl_au=1.1.1078152908.1733516554; cookie-promo-alerts-popup=true; webp_supported=true; _ga_KRLJETD70M=GS1.1.1733516554.1.0.1733516554.60.0.0; _tt_enable_cookie=1; _ttp=7mUQVmvqtm3oCpmUUWpn43Nk-Qc.tt.2; __gads=ID=3a7a7df565850012:T=1733516555:RT=1733516555:S=ALNI_MbBtPikFLLnnvXFtXzlz14LGQvs_g; __gpi=UID=00000fb30d228a38:T=1733516555:RT=1733516555:S=ALNI_MaaTRctSgAQXEhLVV20ZjvnoNhWnw; __eoi=ID=1d858b3b967aaa5a:T=1733516555:RT=1733516555:S=AA-AfjZFNqireUAEbEw7ZzCGERUA; AWSALB=fmx5bH6UIaMe/S2Pv0xJJZ++5AIuYTI80Q5HlgJxn4Ff2jYwc1cMDigFjXgQZc5jE90/IjHuQy2KZB1hDvtMI3mSpL6BEnpq/RT0NORNn1P6OP1K5Z2fj6cBfKAW; AWSALBCORS=fmx5bH6UIaMe/S2Pv0xJJZ++5AIuYTI80Q5HlgJxn4Ff2jYwc1cMDigFjXgQZc5jE90/IjHuQy2KZB1hDvtMI3mSpL6BEnpq/RT0NORNn1P6OP1K5Z2fj6cBfKAW; _fbp=fb.2.1733516555632.425449188482098936; _clck=szbwqb%7C2%7Cfrh%7C0%7C1801; _clsk=w7qvpj%7C1733516556823%7C1%7C1%7Cl.clarity.ms%2Fcollect; _ga=GA1.3.121653827.1733516555; _gid=GA1.3.1157782289.1733516557; _dc_gtm_UA-41901849-1=1; _gat_UA-137468022-1=1; _ga_SY8LS918MZ=GS1.3.1733516575.1.0.1733516576.59.0.0; _uetsid=d43b56e0b40f11ef8f17737ee5635795',
    "priority": "u=0, i",
    "referer": "https://www.checkers.co.za/",
    # "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Please Let me In",
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

response = requests.get(
    "https://www.checkers.co.za/search/all",
    params={
        "q": "2L milk",
    },
    # cookies=cookies,
    headers={
        # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        # "accept-language": "en-US,en;q=0.9",
        # 'cookie': 'anonymous-consents=%5B%5D; checkersZA-preferredStore=57861; cookie-notification=NOT_ACCEPTED; JSESSIONID=Y59-0c37c90c-cdb9-4cb6-a8d5-05bce11a8532; _gcl_au=1.1.1078152908.1733516554; cookie-promo-alerts-popup=true; webp_supported=true; _ga_KRLJETD70M=GS1.1.1733516554.1.0.1733516554.60.0.0; _tt_enable_cookie=1; _ttp=7mUQVmvqtm3oCpmUUWpn43Nk-Qc.tt.2; __gads=ID=3a7a7df565850012:T=1733516555:RT=1733516555:S=ALNI_MbBtPikFLLnnvXFtXzlz14LGQvs_g; __gpi=UID=00000fb30d228a38:T=1733516555:RT=1733516555:S=ALNI_MaaTRctSgAQXEhLVV20ZjvnoNhWnw; __eoi=ID=1d858b3b967aaa5a:T=1733516555:RT=1733516555:S=AA-AfjZFNqireUAEbEw7ZzCGERUA; AWSALB=fmx5bH6UIaMe/S2Pv0xJJZ++5AIuYTI80Q5HlgJxn4Ff2jYwc1cMDigFjXgQZc5jE90/IjHuQy2KZB1hDvtMI3mSpL6BEnpq/RT0NORNn1P6OP1K5Z2fj6cBfKAW; AWSALBCORS=fmx5bH6UIaMe/S2Pv0xJJZ++5AIuYTI80Q5HlgJxn4Ff2jYwc1cMDigFjXgQZc5jE90/IjHuQy2KZB1hDvtMI3mSpL6BEnpq/RT0NORNn1P6OP1K5Z2fj6cBfKAW; _fbp=fb.2.1733516555632.425449188482098936; _clck=szbwqb%7C2%7Cfrh%7C0%7C1801; _clsk=w7qvpj%7C1733516556823%7C1%7C1%7Cl.clarity.ms%2Fcollect; _ga=GA1.3.121653827.1733516555; _gid=GA1.3.1157782289.1733516557; _dc_gtm_UA-41901849-1=1; _gat_UA-137468022-1=1; _ga_SY8LS918MZ=GS1.3.1733516575.1.0.1733516576.59.0.0; _uetsid=d43b56e0b40f11ef8f17737ee5635795',
        # "priority": "u=0, i",
        # "referer": "https://www.checkers.co.za/",
        # "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        # "sec-ch-ua-mobile": "?0",
        # "sec-ch-ua-platform": '"Windows"',
        # "sec-fetch-dest": "document",
        # "sec-fetch-mode": "navigate",
        # "sec-fetch-site": "same-origin",
        # "sec-fetch-user": "?1",
        # "upgrade-insecure-requests": "1",
        # "user-agent": "Please Let me In",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    },
)

print(response)
