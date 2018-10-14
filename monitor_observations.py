import datetime
import pandas as pd
import numpy as np

from db.database_manager import DatabaseManager, db
from sqlalchemy import and_

from models.raw_wind import RawWind
from models.raw_rain import RawRain
from models.observation import Observation


class MonitorObservations:

    def __init__(self):

        print("Starting")
        self.obs_data = None

    def monitor_observations(self):

        last_run = None

        while True:

            # If there is no previous run, just run through anyway
            curtime = datetime.datetime.now()
            if last_run is not None:
                if (curtime - last_run).total_seconds() < 60:
                    continue

            last_run = curtime

            # Prepare observation data for the previous minute
            minute_obs = (curtime - datetime.timedelta(minutes=1)).replace(second=0)
            minute_store = minute_obs + datetime.timedelta(minutes=1)

            wind_df = self.get_wind_df(minute=minute_obs)
            wind_direction = self.average_wind_direction(wind_df=wind_df)
            wind_speed = self.average_wind_speed(wind_df=wind_df)
            wind_gust = self.max_wind_gust(wind_df=wind_df)
            rain = self.current_rain(minute=minute_obs)

            obs = Observation(dt=minute_store,
                              wind_direction=wind_direction,
                              wind_speed=wind_speed,
                              wind_gust=wind_gust,
                              rain=rain)

            try:

                session = db.get_session()
                session.add(obs)
                session.commit()

            except Exception as e:

                print("Unable to add observation due to exception %s" % e)

    def current_rain(self, minute):

        session = db.get_session()
        last_rain = session.query(RawRain).order_by(RawRain.dt.desc()).first()
        session.close()

        return round(last_rain.rain, 1)

    def get_wind_df(self, minute):

        # Find most common wind direction during the samples in that minute
        minute_plus_one = self.get_minute_plus_one(minute)
        session = db.get_session()
        samples = session.query(RawWind).filter(and_((minute <= RawWind.dt),
                                                     (RawWind.dt < minute_plus_one))).all()
        session.close()

        # Convert sample RawWind objects to dataframe as per
        # https://stackoverflow.com/questions/34997174/how-to-convert-list-of-model-objects-to-pandas-dataframe
        wind_df = pd.DataFrame.from_records([s.to_dict() for s in samples])

        return wind_df

    def average_wind_direction(self, wind_df):

        wind_direction_mode = int(wind_df['wind_direction'].mode()[0].item())

        return wind_direction_mode

    def average_wind_speed(self, wind_df):

        wind_speed_mean = round(wind_df['wind_speed'].mean().item(), 1)

        return wind_speed_mean

    def max_wind_gust(self, wind_df):

        last_three_speeds = []
        max_three_second_mean = 0

        for index, row in wind_df.iterrows():

            last_three_speeds.append(row['wind_speed'])

            if len(last_three_speeds) > 3:

                last_three_speeds.pop(0)

                last_three_speeds_series = pd.Series(last_three_speeds)
                mean_speed = last_three_speeds_series.mean().item()

                if mean_speed > max_three_second_mean:
                    max_three_second_mean = mean_speed

        return round(max_three_second_mean, 1)

    def get_minute_plus_one(self, minute):
        return minute + datetime.timedelta(minutes=1)


if __name__ == "__main__":
    obsmon = MonitorObservations()
    obsmon.monitor_observations()
