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

fruits_to_show = my_fruit_list.loc[fruits_selected]



# Display the table on the page.
