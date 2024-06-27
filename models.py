from sqlalchemy import Column, Integer, String

from database import Base


class Otdels(Base):
    __tablename__ = 'otdels'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Category(Base):
    __tablename__ = 'category'

    ...


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, index=True)
    password = Column(String, index=True)
    fio = Column(String, index=True)
