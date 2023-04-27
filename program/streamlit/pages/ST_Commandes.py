import streamlit as st
import mysql.connector as MC
import time
import sys
sys.path.append('../')

#"""------------------COnnection to other file------------------"""
from sql.sql import ConnectionSQL
from api.request import connection_mysql,get_a_column

# st.set_page_config(page_title="Connection to database")

def edit_input_str(input:str):
      return input.replace('"', '').split(".")

flower=str(get_a_column("NAME","FLOWER"))
flower = edit_input_str(flower)

shop=str(get_a_column("ADRESS","SHOP"))
shop=edit_input_str(shop)

st.markdown("# Commandes Demo")
# st.sidebar.header("Connection Demo")
st.write(
    """Test commandes of a user to bdd"""
)
status_text = st.sidebar.empty()
class Connection_page:
      def __init__(self) -> None:
            self.div=st.empty()
            #create a div of self.div
            self.form= self.div.form(key='command', clear_on_submit=True)

      def windows(self) -> None:
            with self.form:
                  self.email = self.form.text_input(label='email',)
                  self.lieu = self.form.selectbox(label='lieu',options=shop)
                  self.product = self.form.selectbox(label='Product', options=flower)
                  self.number = self.form.slider(label='Number', min_value=1, max_value=20, value=1, step=1)
                  submit_button = self.form.form_submit_button(label='Submit')

                  if submit_button:
                        self.command()

      def command(self) :
            pass

      # def connection(self) :
      #       print(connection_mysql(self.user,self.password))
      #       self.form.success("connection réussie") if (connection_mysql(self.user,self.password)==True) else self.form.error("connection échouée")

#adding a single-line text input widget
connection=Connection_page()
connection.windows()