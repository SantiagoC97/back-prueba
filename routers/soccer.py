from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Path, Query, Depends

from schemas.soccer import Soccer
from config.database import Session
from services.soccer import SoccerService
from middlewares.jwt_bearer import JWTBearer
from models.soccer import Soccer as SoccerModel

soccer_router = APIRouter()

@soccer_router.get("/soccer/{id}", tags=['soccer'], response_model=Soccer, status_code=200)
def get_soccer(id: int = Path(ge=1, le=2000)) -> Soccer:
    db = Session()
    result = SoccerService(db).get_soccer(id)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Footballer not found"}, status_code=404)
    return result

@soccer_router.get("/soccer/", tags=['soccer'], response_model=List[Soccer])
def get_soccers_by_position(position: str = Query(min_length=3, max_length=15)) -> List[Soccer]:
    db = Session()
    result = SoccerService(db).get_soccers_by_position(position)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Footballer not found"}, status_code=404)
    return result

@soccer_router.post("/soccer", tags=['soccer'], response_model=dict, status_code=201)
def create_soccer(soccer: Soccer) -> dict:
    db = Session()
    SoccerService(db).create_soccer(soccer)
    return JSONResponse(content={"message": "Footballer created successfully"}, status_code=201)

@soccer_router.put("/soccer/{id}", tags=['soccer'], response_model=dict, status_code=200)
def update_soccer(id: int, soccer: Soccer) -> dict:
    db = Session()
    soccer = SoccerService(db).get_soccer(id)
    if not soccer:
        response = JSONResponse(content={"message": "Footballer not found"}, status_code=404)
    else:
        SoccerService(db).update_soccer(soccer)
        response = JSONResponse(content={"message": "Footballer updated successfully"}, status_code=200)
    return response

@soccer_router.delete("/soccer/{id}", tags=['soccer'], response_model=dict, dependencies=[Depends(JWTBearer())])
def delete_soccer(id: int) -> dict:
    db = Session()
    soccer = SoccerService(db).get_soccer(id)
    if not soccer:
        response = JSONResponse(content={"message": "Footballer not found"}, status_code=404)
    else:
        SoccerService(db).delete_soccer(soccer)
        response = JSONResponse(content={"message": "Footballer deleted successfully"})
    return response

@soccer_router.get("/soccer", tags=['soccer'], response_model=List[Soccer], status_code=200)#, dependencies=[Depends(JWTBearer())])
def get_soccers() -> List[Soccer]:
    db = Session()
    result = SoccerService(db).get_soccer()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))