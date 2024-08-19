from pydantic import Field
from store.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    name: str = Field(description="Descrição do Produto")
    price: float = Field(description="Preço do Produto")
    quantity: int = Field(description="Quantidade do Produto")
    status: bool = Field(description="Status do Produto")
