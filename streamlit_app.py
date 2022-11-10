import streamlit


streamlit.title('My Parents New Healthy Dinner')
streamlit.header('My Breakfast Menu')
streamlit.text('Orange 3 & Blueberry oatmeal')
streamlit.text('Kale, Spinach & Rocket smoothie')
streamlit.text('Hard-Boiled, Free-Range, Egg')

streamlit.header('Build Your Own Smothiee')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
