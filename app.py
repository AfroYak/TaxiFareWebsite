import time
import streamlit as st
import requests
from datetime import datetime

from streamlit.type_util import Key

'''
# NY Taxi Fare Tool
'''

url = 'https://tf-model-api-2uq3dmsrxa-ew.a.run.app/predict'


params = {
    "pickup_datetime": "2013-07-06 17:18:00",
    "pickup_longitude": -73.950655,
    "pickup_latitude": 40.783282,
    "dropoff_longitude": -73.984365,
    "dropoff_latitude": 40.769802,
    "passenger_count": 0,
}


col1, col2 = st.columns(2)
pickup_date = str(col1.date_input(
    "Pick-up Date", datetime.strptime('2013-07-06', '%Y-%m-%d'), key=1))
pickup_time = str(col2.time_input(
    'Pick-up Time', datetime.strptime('17:18:00', '%H:%M:%S'), key=2))

params['pickup_datetime'] = ' '.join([pickup_date, pickup_time])

col3, col4 = st.columns(2)
params['pickup_longitude'] = col3.number_input(
    'Pick-up Longitude', value=-73.950655)
params['dropoff_longitude'] = col3.number_input(
    'Drop-off Longitude', value=-73.984365)

params['pickup_latitude'] = col4.number_input(
    'Pick-up Latitude', value=40.783282)
params['dropoff_latitude'] = col4.number_input(
    'Drop-off Latitude', value=40.769802)

params['passenger_count'] = st.slider('Passenger Count', max_value=8)


# st.write(params)


def get_prediction(search_params=None):
    response = requests.get(url, params=params).json()
    return response['prediction']


base_col, main_col, end_col = st.columns([7, 5, 5])

if base_col.button('Get Fare!'):
    fare = get_prediction()
    base_col.empty()
    end_col.write(f'### Fare: ${fare:0.2f}')
