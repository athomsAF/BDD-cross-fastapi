import streamlit as st
import mysql.connector as MC
import time
import sys
import pandas as pd
import numpy as np
sys.path.append('../')

#"""------------------COnnection to other file------------------"""
from sql.sql import ConnectionSQL
from api.request import connection_mysql,get_a_column, get_all_command

# st.set_page_config(page_title="Connection to database")

def edit_input_str(input:str):
      return input.replace('"', '').split(".")

mail=str(get_a_column("MAIL","CLIENT"))
mail = edit_input_str(mail)


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
                  self.mail=self.form.selectbox(label='Mail', options=mail)
                  submit_button = self.form.form_submit_button(label='Submit')
                  if submit_button:
                        self.command()

      def command(self) :
            date=get_a_column("DATE","COMMAND","IDCLIENT","CLIENT", "MAIL" ,self.mail)
            date=edit_input_str(date)
            date=[i.split("-")[1] for i in date]
            dataset = [int(x) for x in date]

            # Create a pandas series with the dataset
            data_series = pd.Series(dataset)

            # Create a pandas dataframe with a count of the number of iterations of each number from 1 to 12 for each month
            chart_data= pd.DataFrame({'count': data_series.groupby(data_series).size()}).reset_index()
            for i in range(1,13):
                  if i not in chart_data["index"].values:
                        print(i)

            self.form.line_chart(chart_data)
            self.form.write(f"Nombre de commande fait par le client: {get_all_command()}")
            if  get_all_command() !=None and get_all_command() >=5: #type: ignore
                  self.form.write ("le client est un client or")
            elif get_all_command() !=None and get_all_command() >=1: #type: ignore
                  self.form.write('le client est un client bronze')
            else:
                  self.form.write("le client n'a pas de statut particulier")
      # def connection(self) :
      #       print(connection_mysql(self.user,self.password))
      #       self.form.success("connection réussie") if (connection_mysql(self.user,self.password)==True) else self.form.error("connection échouée")

#adding a single-line text input widget
connection=Connection_page()
connection.windows()