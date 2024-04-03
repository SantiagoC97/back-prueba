from schemas.soccer import Soccer
from models.soccer import Soccer as SoccerModel

class  SoccerService():
    def __init__(self, db):
        self.db = db
    
    def get_soccers(self):
        return self.db.query(SoccerModel).all()

    def get_soccer(self, id:int):
        return self.db.query(SoccerModel).filter(SoccerModel.id == id).first()
    
    def get_soccers_by_position(self, position:str):
        return self.db.query(SoccerModel).filter(SoccerModel.position == position).all()
    
    def  create_soccer(self, soccer:Soccer):
        new_soccer = SoccerModel(**soccer.model_dump())
        self.db.add(new_soccer)
        self.db.commit()

    def update_soccer(self, soccer: SoccerModel, data:Soccer):
        soccer.id = soccer.id
        soccer.name = soccer.name
        soccer.overview = soccer.overview
        soccer.age = soccer.age
        soccer.rating = soccer.rating
        soccer.position = soccer.position
        self.db.commit()        

    def delete_soccer(self, soccer: SoccerModel):
        self.db.delete(soccer)
        self.db.commit()