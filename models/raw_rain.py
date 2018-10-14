from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, DateTime

Base = declarative_base()


class RawRain(Base):

    __tablename__ = "raw_rain"

    id = Column(Integer, primary_key=True)
    dt = Column(DateTime, nullable=False)
    rain = Column(Float, nullable=False)

    def __repr__(self):
        return "<RawRain(id='%s', dt='%s', rain='%s')>" \
               % (self.id, self.dt, self.rain)
