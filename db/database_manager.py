# Module for establishing application wide SQL Alchemy ORM
import configparser
import logging

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class DatabaseManager:

    def __init__(self):

        # Logging
        self.logger = logging.getLogger('database-manager')

        # Log details of configuration
        self.logger.info("Loaded Database Manager")

        # Read authentication data from root directory auth.ini
        self.auth = configparser.ConfigParser()
        auth_loaded = self.auth.read(['auth.ini'])

        # Read Configuration data from root directory
        self.config = configparser.ConfigParser()
        config_loaded = self.config.read(['config.ini'])

        self.logger.info("Loaded configuration from %s and %s" % (auth_loaded, config_loaded))

        url = "mysql+pymysql://%s:%s@%s:%s/%s" % (self.auth['database']['username'],
                                                  self.auth['database']['password'],
                                                  self.auth['database']['server'],
                                                  self.auth['database']['port'],
                                                  self.auth['database']['db_name'])
        self.engine = create_engine(url,
                                    pool_size=20,
                                    pool_pre_ping=True,
                                    pool_recycle=3600,
                                    pool_reset_on_return='rollback',
                                    max_overflow=0)
        self.session_maker = sessionmaker(bind=self.engine)

    def get_session(self, autoflush=True):

        session = scoped_session(self.session_maker)
        session.configure(autoflush=autoflush)
        return session


# Set up Database Manager
db = DatabaseManager()

config = configparser.ConfigParser(interpolation=None)
config.read(['config.ini'])

dt_fmt = config['database']['datetime_format']