# generated by datamodel-codegen:
#   filename:  pet.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from pydantic import BaseModel


class Pet(BaseModel):
    name: str
    age: int


class Model(BaseModel):
    Pet: Pet
