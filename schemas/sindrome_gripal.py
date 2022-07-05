from typing import Optional
from pydantic import BaseModel


class Query(BaseModel):
    uf: str = '*'
    municipio: Optional[str]
