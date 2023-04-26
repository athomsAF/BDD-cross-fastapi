import mysql.connector as MC
from typing import List, Tuple, Optional

class ConnectionSQL:
      def __init__(self,user:str, password:str):
            self.USER= user
            self.PASSWORD= password
            try:
                  self.connection= MC.connect(
                        host="localhost",
                        user=self.USER,
                        password=self.PASSWORD,
                        database="project"
                        )
                  if(self.connection.is_connected()):
                        self.cursor= self.connection.cursor()
                        print("connection établie avec le compte "+self.USER)
            except MC.Error as error:
                  self.connection=None
                  print(error)
                  self.cursor=None
      def insert_command_show_table(self) -> Optional[List[Tuple[str]]]:
            # self.cursor.execute(command)
            # self.connection.commit()
            if self.cursor is not None:
            #print all table
                  self.cursor.execute(f"SHOW TABLES;")
                  return self.cursor.fetchall()
            else:
                  return None