
from sqlalchemy import Column, String, Integer, DateTime, Time, Float

from base import Base



class Measurment(Base):

  __tablename__ = 'measurments'

  id = Column(Integer, primary_key=True)

  buoy_name = Column(String)
  datetime_taken = Column(DateTime)

  sea_state = Column(Integer)
  wave_height = Column(Float)
  wave_direction = Column(Integer)
  wind_speed = Column(Float)
  wind_direction = Column(Integer)
  water_temperature = Column(Float)


  def __init__(self, buoy_name, date_taken, sea_state, wave_height, wave_direction, wind_speed, wind_direction, water_temperature):

    self.buoy_name = buoy_name
    self.date_taken = date_taken
    self.sea_state = sea_state
    self.wave_height = wave_height
    self.wave_direction = wave_direction
    self.wind_speed = wind_speed
    self.wind_direction = wind_direction
    self.water_temperature = water_temperature








