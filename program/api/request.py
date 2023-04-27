import requests
from typing import Optional

rs=requests.session()

def connection_mysql(user:str, password:str) -> bool:
      """Connection to mysql server"""
      url="http://127.0.0.1:8000/connection"
      data={"login":user,"password":password}
      response=requests.post(url,params=data)
      return(response.text=="true")

def get_a_column(column :str, table :str, select=None, table2=None, select2=None, value=None) :
      """Get a column in a table"""
      print(column, table, select, value)
      url="http://127.0.0.1:8000/get_column"
      data={"column":column,"table":table, "select":select, "value":value,"select2":select2, "table2":table2} if select!=None and value!=None else {"column":column,"table":table}
      response=requests.post(url,params=data)
      return (response.text)

def create_a_command(email:str, shop_adresse:str) -> bool:
      """Create a command"""
      url="http://127.0.0.1:8000/create_a_command"
      data={"email":email,"shop_adresse":shop_adresse}
      response=requests.post(url,params=data)
      return(response.text=="true")

def get_all_command() -> Optional[float]:
      """Get all command"""
      url="http://127.0.0.1:8000/get_all_command"
      return float(requests.post(url).text) if requests.post(url).text!="None" else None

def best_client() -> Optional[str]:
      """Get best client"""
      url="http://127.0.0.1:8000/best_client"
      return str(requests.post(url).text) if requests.post(url).text!="None" else None