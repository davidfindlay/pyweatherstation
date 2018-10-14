from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, DateTime

Base = declarative_base()


class RawWind(Base):

    __tablename__ = "raw_wind"

    id = Column(Integer, primary_key=True)
    dt = Column(DateTime, nullable=False)
    wind_direction = Column(Integer, nullable=True)
    wind_speed = Column(Float, nullable=True)

    def __repr__(self):
        return "<RawWind(id='%s', dt='%s', wind_speed='%s', wind_direction='%s')>" \
               % (self.id, self.dt, self.wind_speed, self.wind_direction)

    def to_dict(self):
        return {
            'id': self.id,
            'dt': self.dt,
            'wind_direction': self.wind_direction,
            'wind_speed': self.wind_speed
        }
