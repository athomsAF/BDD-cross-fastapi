import requests

rs=requests.session()

def connection_mysql(user:str, password:str) -> bool:
      """Connection to mysql server"""
      url="http://127.0.0.1:8000/connection"
      data={"login":user,"password":password}
      response=requests.post(url,params=data)
      return(response.text=="true")

def get_a_column(column:str, table:str):
      """Get a column in a table"""
      url="http://127.0.0.1:8000/get_column"
      data={"column":column,"table":table}
      response=requests.post(url,params=data)
      return (response.text)

def create_a_command(email:str, shop_adresse:str) -> bool:
      """Create a command"""
      url="http://127.0.0.1:8000/create_a_command"
      data={"email":email,"shop_adresse":shop_adresse}
      response=requests.post(url,params=data)
      
      
      return(response.text=="true")