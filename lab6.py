import sqlite3
from pydantic import BaseModel, Field
from datetime import datetime


#Замість self(init) Basemodel
class Block(BaseModel):
    id: str = Field(pattern=r"^0x[0-9a-fA-F]{8}$")
    view: int = Field(ge=0)
    desc: str = Field(min_length=1, max_length=50)
    img: str = Field(min_length=1, max_length=100)

    @staticmethod
    def get_all(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM BLOCKS")
        rows = cur.fetchall()
        return [Block(id=row[0], view=row[1], desc=row[2], img=row[3]) for row in rows]


#Person
class Person(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(min_length=1, max_length=50)
    addr: str = Field(min_length=1, max_length=100)

    @staticmethod
    def get_all(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM PERSONS")
        rows = cur.fetchall()
        return [Person(id=row[0], name=row[1], addr=row[2]) for row in rows]


#Source
class Source(BaseModel):
    id: int = Field(ge=0)
    ip_addr: str = Field(min_length=1, max_length=100)
    country_code: str = Field(min_length=2, max_length=2)

    @staticmethod
    def get_all(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM SOURCES")
        rows = cur.fetchall()
        return [Source(id=row[0], ip_addr=row[1], country_code=row[2]) for row in rows]


#Vote
class Vote(BaseModel):
    block_id: str = Field(pattern=r"^0x[0-9a-fA-F]{8}$")
    voter_id: int = Field(ge=0)
    timestamp: datetime 
    source_id: int = Field(ge=0)

    @staticmethod
    def get_all(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM VOTES")
        rows = cur.fetchall()
        return [Vote(block_id=row[0], voter_id=row[1], timestamp=row[2], source_id=row[3]) for row in rows]



if __name__ == "__main__":
    conn = sqlite3.connect("lab3.db")

    blocks = Block.get_all(conn)
    print("Blocks:", blocks)

    votes = Vote.get_all(conn)
    print("Votes:", votes)

    conn.close()