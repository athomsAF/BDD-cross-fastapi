import streamlit as st
import mysql.connector as MC
import time
import sys
sys.path.append('../')

#"""------------------COnnection to other file------------------"""
from sql.sql import ConnectionSQL
from api.request import connection_mysql
# st.set_page_config(page_title="Connection to database")

st.markdown("# Connection Demo")
# st.sidebar.header("Connection Demo")
st.write(
    """Test connection of a user to bdd"""
)
status_text = st.sidebar.empty()
class Connection_page:
      def __init__(self) -> None:
            self.div=st.empty()
            #create a div of self.div
            self.form= self.div.form(key='connection', clear_on_submit=True)

      def windows(self) -> None:
            with self.form:
                  self.user = self.form.text_input(label='User', label_visibility='visible')
                  self.password = self.form.text_input(label='Password', type="password",label_visibility='visible')
                  submit_button = self.form.form_submit_button(label='Submit')

                  if submit_button:
                        self.connection()

      def connection(self) :
            print(connection_mysql(self.user,self.password))
            self.form.success("connection réussie") if (connection_mysql(self.user,self.password)==True) else self.form.error("connection échouée")

#adding a single-line text input widget
connection=Connection_page()
connection.windows()