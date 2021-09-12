# streamlit_app.py
from datetime import datetime

import pandas as pd
import streamlit as st
import mysql.connector
import plotly.graph_objects as go

# Initialize connection.
# Uses st.cache to only run once.
@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()
c = conn.cursor()

#CRIAÇÃO DA TABELA DOGS
def create_table_dogs():
    c.execute('CREATE TABLE IF NOT EXISTS dogstable(name TEXT, breed TEXT)')

#INSERINDO DADOS NA TABELA DOGS
def add_data_dogs(name, breed):
    c.execute('INSERT INTO dogstable(name, breed) VALUES (%s, %s)', (name, breed))
    conn.commit()

#VISUALIZANDO DADOS DA TABELA DOGS
def view_all_dogs():
    c.execute('SELECT * FROM dogstable')
    data = c.fetchall()
    return data

###################################################################################################################################

#CRIAÇÃO DA TABELA CARS
def create_table_cars():
    c.execute('CREATE TABLE IF NOT EXISTS carstable(make TEXT, model TEXT, color TEXT, year TEXT)')

#INSERINDO DADOS NA TABELA CARS
def add_data_cars(make, model, color, year):
    c.execute('INSERT INTO carstable(make, model, color, year) VALUES (%s, %s, %s, %s)', (make, model, color, year))
    conn.commit()

#VISUALIZANDO DADOS DA TABELA DOGS
def view_all_cars():
    c.execute('SELECT * FROM carstable')
    data = c.fetchall()
    return data

###################################################################################################################################

#CRIAÇÃO DA TABELA CARS
def create_table_games():
    c.execute('CREATE TABLE IF NOT EXISTS gamestable(name TEXT, studio TEXT, launch_year TEXT)')

#INSERINDO DADOS NA TABELA CARS
def add_data_games(name, studio, launch_year):
    c.execute('INSERT INTO gamestable(name, studio, launch_year) VALUES (%s, %s, %s)', (name, studio, launch_year))
    conn.commit()

#VISUALIZANDO DADOS DA TABELA DOGS
def view_all_games():
    c.execute('SELECT * FROM gamestable')
    data = c.fetchall()
    return data

def main():
    st.title("Trab Python")

    menu = ["Dogs", "Cars", "Games"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Dogs":
        st.subheader("Dogs")
        create_table_dogs()
        dog_name = st.text_input("Enter Dog Name", max_chars=20)
        dog_breed = st.text_input("Enter Breed Name", max_chars=20)
        if st.button("Add"):
            add_data_dogs(dog_name, dog_breed)
            st.success("Data included")

        result = view_all_dogs()
        with st.expander("View All Data"):
            df = pd.DataFrame(result, columns=['Name', 'Breed'])
            st.dataframe(df)

    elif choice == "Cars":
        st.subheader("Cars")
        create_table_cars()
        car_make = st.text_input("Enter Car Make", max_chars=20)
        car_model = st.text_input("Enter Car Model", max_chars=20)
        car_color = st.text_input("Enter Car Color", max_chars=20)
        car_year = st.text_input("Enter Car Year", max_chars=4)
        if st.button("Add"):
            add_data_cars(car_make, car_model, car_color, car_year)
            st.success("Data included")

        result = view_all_cars()
        with st.expander("View All Data"):
            df = pd.DataFrame(result, columns=['Make', 'Model', 'Color', 'Year'])
            st.dataframe(df)

    elif choice == "Games":
        st.subheader("Games")
        create_table_games()
        game_name = st.text_input("Enter Game Name", max_chars=30)
        game_studio = st.text_input("Enter Game Studio", max_chars=30)
        game_launch_year = st.text_input("Enter Game Launch Year", max_chars=4)
        if st.button("Add"):
            add_data_games(game_name, game_studio, game_launch_year)
            st.success("Data included")

        result = view_all_games()
        with st.expander("View All Data"):
            df = pd.DataFrame(result, columns=['Name', 'Studio', 'Launch Year'])
            st.dataframe(df)


main()