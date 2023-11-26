from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()
p=os.getenv('password')

print(p)


engine = create_engine(f'postgresql://user:1mispac{p}@postgresserver/app_database1')
session = sessionmaker()
Base = declarative_base()