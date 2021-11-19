import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import datetime
import requests





# if i want to imput direction and output coordinates
# def geocode(address):
#     params = {"q": address, 'format': 'json'}
#     places = requests.get(f"https://nominatim.openstreetmap.org/search",
#                           params=params).json()
#     return [places[0]['lat'], places[0]['lon']]

# st.write(geocode('new york, central park'))

#DAY part
now=datetime.datetime.now()

d = st.date_input("What day?", datetime.date(now.year, now.month, now.day))
st.write('Day', d)

t = st.time_input('At what time?', datetime.time(now.hour, now.minute, 00))

st.write('Pickup time:', t)

pickup_datetime= f'{d} {t}'

#pickup latitude

latitude_pick= st.text_input('Latitude Pickup', '0')

if float(latitude_pick) > 35 and float(latitude_pick) < 45:
    st.write('The current Latitude is ', latitude_pick)
else:
    st.write('Your latitude is off, should be between 35 and 45', '')

pickup_latitude= latitude_pick
#pickup longitude

longitude_pick = st.text_input('Longitude Pickup', '0')

if float(longitude_pick) > -80 and float(longitude_pick) < -70:
    st.write('The current longitude is ', longitude_pick)
else:
    st.write('Your longitude is off, should be between -70 and -80', '')

pickup_longitude = longitude_pick

#drop latitude

latitude_drop = st.text_input('Latitude drop', '0')

if float(latitude_drop) > 35 and float(latitude_drop) < 45:
    st.write('The current Latitude is ', latitude_drop)
else:
    st.write('Your latitude is off, should be between 35 and 45', '')



dropoff_latitude = latitude_drop

#drop longitude

longitude_drop = st.text_input('Longitude drop', '0')

if float(longitude_drop) > -80 and float(longitude_drop) < -70:
    st.write('The current longitude is ', longitude_drop)
else:
    st.write('Your longitude is off, should be between -70 and -80', '')
dropoff_longitude = longitude_drop

#passanger count


number = st.number_input('Insert a number',1)


st.write('The current number is ', number)

passenger_count=number

params = {
    'key': '',
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude':dropoff_longitude ,
    'dropoff_latitude':dropoff_latitude ,
    'passenger_count':passenger_count}





R = requests.get('https://taxifare.lewagon.ai/predict', params=params).json()
L=R.get('prediction','no prediction')


if st.button('Predict'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write(f'Prediction: {L}')


else:
    st.write('Click me for prediction')



# map

import folium
from streamlit_folium import folium_static



m = folium.Map(location=[40.785165, -73.964107],zoom_start=11)


tooltip = "Click me!"

folium.Marker([latitude_pick,longitude_pick],
              popup="<i>Pickup</i>",
              tooltip=tooltip).add_to(m)

folium.Marker([latitude_drop, longitude_drop],
              popup="<b>Drop</b>",
              tooltip=tooltip).add_to(m)

folium_static(m)


# '''
# # TaxiFareModel front
# '''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')
# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

# url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown(
#         'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
#     )
# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
