from pydantic import BaseModel, Field
from typing import Optional

class Soccer(BaseModel):
    id: Optional[int] = Field(default=1, le=99)
    name: str = Field(default="Nombre del jugador", min_length=3, max_length=60)
    overview: str = Field(default="Habilidades del jugador", min_length=3, max_length=500)
    age: int = Field(default=0, le=40)
    rating: float = Field(default=99, ge=0, le=99)
    position: str = Field(default="Posicion del jugador", min_length=3, max_length=60)
    
    # Configuracion de la documentacion
    class Config:
        model_config = {
        "json_schema_extra": {
                "examples": [
                    {
                        "id": 7,
                        "name": "Cristiano Ronaldo",
                        "overview": "Uso de ambas piernas, regate y cabeceo",
                        "age": 38,
                        "rating": 92,
                        "position": "Falso 9"
                    }
                ]
            }
        }

