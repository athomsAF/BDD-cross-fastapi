from typing import Union, List, Optional, Tuple, Dict
from fastapi import FastAPI 
from pydantic import BaseModel
import sys
sys.path.append('../')

#"""------------------COnnection to other file------------------"""
from sql.sql import ConnectionSQL, Shop, Client


app = FastAPI()


connection_bdd = ConnectionSQL("root","root")
connections : dict={}
connections["root"]=connection_bdd

@app.post("/commit/")
async def commit():
      return type(connection_bdd.connection.commit() if connection_bdd.connection!=None else None)!=None

@app.post("/connection/")
async def connection(login:str, password:str) -> bool:
      connections[login]=ConnectionSQL(login,password)
      return connections[login].connection!=None

@app.post("/create_a_command/")
async def create_a_command(email:str, shop_adresse:str) -> bool:
      idshop=Shop().search_by_adress(shop_adresse,connections["root"].cursor)
      idclient=Client().define_by_email(email,connections["root"].cursor)
      return connection_bdd.insert_command(idclient,idshop) if idshop is not None and idclient is not None else False

@app.post("/get_column/")
async def get_all_column(column :str, table :str, select=None, table2=None,select2=None, value=None) -> Optional[str]:
      if select2==None:
            data=connection_bdd.show_in_table(column, table, select, table2, select2, value )
      else:
            data=connection_bdd.show_in_table(column, table)
      print((list(data)) if data is not None else None)
      data=[str(i[0]) for i in list(data)] if data is not None else None
      return ".".join(data) if data is not None else None

@app.post("/get_all_command/")
async def get_all_command() -> float:
      data=connection_bdd.count_command()
      return float(list(data)[0][0]) if data is not None else 0

@app.post("/best_client/")
async def best_client() -> Optional[str]:
      data=connection_bdd.best_client()
      return " ".join(data[0]) if data is not None else None


@app.get("/test_connection/")
async def test_connection(login:str, password:str) -> bool:
      return ConnectionSQL(login,password).connection!=None

@app.post("/get_all_tables/") 
async def show_tables()-> Optional[List[Tuple[str]]]:
      return (connection_bdd.show_table())