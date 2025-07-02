# Create an account from https://openwethermap.org/

#use Api key from https://openweathermap.org/users/sign_up
# Save the API key in a file named 'apikey.txt' in the same directory as this script.


#we should be able to retrieve the API key from this file in .csv format for climatic fore cast for 30days

#define the API end piont
#url = 

import requests
import pandas as pd


#seet teh api key
API_KEY = '0c3192d3de9f32bfc6beb00bc95ec363'

#cordinates for the location the t you wnat to get the climatic forcast
#for kampala
lat = 0.347596 #latitude for kampala
lon = 32.582520 #longitude for kampala

#define the Api end point
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"

#make the get request
response = requests.get(url)

#check if the request was successful
if response.status_code == 200:
    #parse the json response
    data = response.json()
    
    #convert the data to a pandas dataframe
    df = pd.DataFrame(data['list'])
    
    #print the first 5 rows of the dataframe
    print(df.head())
else:
    print(f"Error: {response.status_code} - {response.text}")
    # Handle the error appropriately, e.g., log it or raise an exception
    # You can also save the error message to a file or notify the user



