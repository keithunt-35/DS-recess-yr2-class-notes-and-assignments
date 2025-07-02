#post means to create new data

#basic post request using requests library
import requests 

#example API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'  # Replace with the desired API endpoint

#data to be sent in the post request
data = {    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

#sending a post request
response = requests.post(url, json=data)  # Use json=data to send data as JSON

#print the status code of the response
print(f'Status Code: {response.status_code}')  # Check if the request was successful
#print the response headers
print(f'Response Headers: {response.headers}')  # Print the response headers