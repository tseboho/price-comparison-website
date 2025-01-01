import fastapi
import fastapi.responses
import fastapi.staticfiles

app = fastapi.FastAPI()

app.mount(
    "/static",
    fastapi.staticfiles.StaticFiles(directory="static"),
    name="static",
)


@app.get("/", response_class=fastapi.responses.HTMLResponse)
def index():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        html: str = file.read()
    return fastapi.responses.HTMLResponse(content=html)


@app.get("/product-search")
def product_search(
    query: str = fastapi.Query(None, description="Product search keywords")
):
    return {
        "checkers": query,
        "picknpay": query,
        "woolworths": query,
    }
