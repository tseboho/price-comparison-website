from pydantic import BaseModel, ConfigDict


class ItemSearchResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    item_title: str
    item_image_url: str
    price_cents: int
