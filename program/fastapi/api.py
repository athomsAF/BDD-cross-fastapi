from typing import Union, List, Optional, Tuple
from fastapi import FastAPI 
from pydantic import BaseModel
import sys
sys.path.append('../')

#"""------------------COnnection to other file------------------"""
from programm.sql.sql import ConnectionSQL


app = FastAPI()

connection_bdd = ConnectionSQL("root","root")

@app.get("/")
async def read_root():
      return {"Hello": "World"}

@app.get("/test_connection/")
async def test_connection(login:str, password:str) -> bool:
      return ConnectionSQL(login,password).connection!=None

@app.post("/get_all_tables/") 
async def show_tables()-> Optional[List[Tuple[str]]]:
      return (connection_bdd.insert_command_show_table())