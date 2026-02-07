import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from core.config import DB_USER, DB_NAME, DB_PORT, DB_PASS, DB_HOST

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

database = databases.Database(DATABASE_URL)# agar database.connect() metodini chaqirsam ulanadi

Base = declarative_base()
metadata = sqlalchemy.MetaData()
