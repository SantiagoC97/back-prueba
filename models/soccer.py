from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Soccer(Base):
    __tablename__ = 'Inventario FIFA'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    overview = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    position = Column(String, nullable=False)
