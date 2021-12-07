import sqlalchemy as db
from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from pathlib import Path

Base = declarative_base()

def init_db(filename='tags.db', path=Path.home(), backend='sqlite:///', debug=False):
    engine = db.create_engine(f'{backend}{path}/{filename}', echo=debug)
    Base.metadata.create_all(engine)
    return engine.connect()

def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class Files(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_hash = Column(String, nullable=False, unique=True)
    tags = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    def add_tags(self, tags):
        self.tags = tags