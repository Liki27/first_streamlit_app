import streamlit


streamlit.title('My Parents New Healthy Dinner')
streamlit.header('My Breakfast Menu')
streamlit.text('Orange 3 & Blueberry oatmeal')
streamlit.text('Kale, Spinach & Rocket smoothie')
streamlit.text('Hard-Boiled, Free-Range, Egg')

streamlit.header('Build Your Own Smothiee')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)# Just write the data of the screen

#take the json version version of the response and normalise it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as the table
streamlit.dataframe(fruityvice_normalized)




# Display the table on the page.
