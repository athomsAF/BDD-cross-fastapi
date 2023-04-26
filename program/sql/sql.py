import mysql.connector as MC
from typing import List, Tuple, Optional
import time

class ConnectionSQL:
      def __init__(self,user:str, password:str):
            self.USER= user
            self.PASSWORD= password
            try:
                  self.connection = MC.connect(
                        host="localhost",
                        user=self.USER,
                        password=self.PASSWORD,
                        database="project"
                        ) 
                  if(self.connection.is_connected()):
                        self.cursor= self.connection.cursor(buffered=True)
                        print("connection établie avec le compte "+self.USER)
            except MC.Error as error:
                  self.connection=None
                  print(error)
                  self.cursor=None
      def show_table(self) -> Optional[List[Tuple[str]]]:
            # self.cursor.execute(command)
            # self.connection.commit()
            if self.cursor is not None:
            #print all table
                  self.cursor.execute(f"SHOW TABLES;")
                  return self.cursor.fetchall()
            else:
                  return None
      def show_in_table (self,column:str, table:str):
            if self.cursor is not None:
                  #get current time in this format: YYYY-MM-DD
                  self.cursor.execute(f"SELECT {column} FROM {table};")
                  return self.cursor.fetchall()
            else:
                  return None

      def insert_command(self,idclient:int, idshop:int) -> bool:
            if self.cursor is not None:
                  #get current time in this format: YYYY-MM-DD
                  actual_time=time.strftime('%Y-%m-%d')
                  self.cursor.execute(f"INSERT INTO COMMAND (IDCLIENT, IDSHOP,DATE) VALUES ({idclient},{idshop},'{actual_time}');")
                  return True
            else:
                  return False

class Shop:
      # def __init__(self,id :int, name :str, adress :str):
      #       self.id=id
      #       self.name=name
      #       self.adress=adress
      def search_by_adress(self, adress:str,cursor):
            if cursor is not None:
                  cursor.execute(f"SELECT * FROM SHOP WHERE ADRESS='{adress}';")
                  data=cursor.fetchall()
                  self.id=data[0][0]
                  self.name=data[0][1]
                  self.adresse=data[0][2]
                  return(data[0][0])
            else:
                  pass


class Client:
      def define_by_email(self,email :str,cursor):
            cursor.execute(f"SELECT * FROM CLIENT WHERE MAIL='{email}';")
            data=cursor.fetchall()
            self.id=data[0][0]
            self.name=data[0][1]
            self.lastname=data[0][2]
            self.phone=data[0][3]
            self.email=data[0][4]
            self.password=data[0][5]
            self.facrturation_adress=data[0][6]
            self.credit_card=data[0][7]
            return(data[0][0])
