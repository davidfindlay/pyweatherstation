from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, DateTime

Base = declarative_base()


class Observation(Base):
    __tablename__ = "observations"

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=True)
    dewpoint = Column(Float, nullable=True)
    wind_direction = Column(Integer, nullable=True)
    wind_speed = Column(Float, nullable=True)
    wind_gust = Column(Float, nullable=True)
    rain = Column(Float, nullable=True)
    pressure = Column(Float, nullable=True)
    dt = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Observation(id='%s', dt='%s', temperature='%s', dewpoint='%s', wind_direction='%s', " \
               "wind_speed='%s', wind_gust='%s', rain='%s', pressure='%s')>" \
               % (self.id, self.dt, self.temperature, self.dewpoint, self.wind_direction, self.wind_speed,
                  self.wind_gust, self.rain, self.pressure)
