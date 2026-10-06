from datetime import date
from uuid import UUID, uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Items API")


class Item(BaseModel):
    nome: str = Field(max_length=25)
    valor: float
    data: date

    @field_validator("data")
    @classmethod
    def validar_data(cls, valor: date) -> date:
        if valor > date.today():
            raise ValueError("a data não pode ser superior à data atual")
        return valor


class ItemResponse(Item):
    uuid: UUID


@app.post("/items", response_model=ItemResponse, status_code=201)
def criar_item(item: Item) -> ItemResponse:
    return ItemResponse(**item.model_dump(), uuid=uuid4())
