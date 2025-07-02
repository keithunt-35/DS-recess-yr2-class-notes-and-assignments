#basic Get request using requests library
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')  # Replace with the desired API endpoint

print(f'Status Code: {response.status_code}')  # Check if the request was successful
#print(f'Response Headers: {response.headers}')  # Print the response headers

# task: use the request library to print the file in the terminal
print(f'Response Content: {response.text}')  # Print the response content