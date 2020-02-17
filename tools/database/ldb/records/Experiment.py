
from sqlalchemy import Column, Integer, String

from . import Base

class Experiment(Base):
    """
    Represents all information on a single experiment in the
    database.
    """

    __tablename__ = "experiments"

    id      = Column(Integer, primary_key=True)
    name    = Column(String)
