import streamlit as st
import mysql.connector as MC
import time
import sys
sys.path.append(' ../')

#"""------------------COnnection to other file------------------"""
from sql.sql import ConnectionSQL
from api.request import best_client
# st.set_page_config(page_title="Connection to database")
def edit_input_str(input:str):
      return input.replace('"', '')
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

      def windows(self) -> None:
            with self.div:
                  self.div.write(f"Le mailleur client est {edit_input_str(str(best_client()))}")



#adding a single-line text input widget
connection=Connection_page()
connection.windows()