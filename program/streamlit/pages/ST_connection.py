import streamlit as st
import mysql.connector as MC
from streamlit_extras.switch_page_button import switch_page
import time
import sys
sys.path.append('../../')

#"""------------------COnnection to other file------------------"""
from programm.sql.sql import ConnectionSQL




# st.set_page_config(page_title="Connection to database")

st.markdown("# Connection Demo")
# st.sidebar.header("Connection Demo")
st.write(
    """Test connection of a user to bdd"""
)
status_text = st.sidebar.empty()
class Connection_page:
      def __init__(self):
            self.div=st.empty()
            #create a div of self.div
            self.form= self.div.form(key='connection', clear_on_submit=True)

      def windows(self):
            with self.form:
                  self.user = self.form.text_input(label='User', label_visibility='visible')
                  self.password = self.form.text_input(label='Password', type="password",label_visibility='visible')
                  submit_button = self.form.form_submit_button(label='Submit')

                  if submit_button:
                        self.connection()

      def connection(self):
            self.connection_user=ConnectionSQL(self.user,self.password)
            connection.connection_user.insert_command_show_table()


#adding a single-line text input widget
connection=Connection_page()
connection.windows()



#displaying the entered text

      



# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
# st.button("Re-run")