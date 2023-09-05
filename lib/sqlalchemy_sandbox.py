#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """
    Represents a student.
    """
    __tablename__ = 'students'
    
    id = Column(Integer(), primary_key=True, doc="Unique student identifier")
    name = Column(String(), doc="Student's name")

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}')"

def create_database():
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_database()
