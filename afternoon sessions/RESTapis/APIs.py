# Introduction to API
# API stands for Application Programming Interface
# API is a set of rules that allows different software applications to communicate with each other
# APIs are used to access the functionality of a software application or service
# APIs can be used to access data, perform actions, or integrate with other services



#understanding APIs:#1. APIs are like a contract between two software applications
#   - They define how the applications will interact with each other
#   - APIs specify the methods, parameters, and data formats
#2. APIs can be thought of as a bridge between different software systems
#   - They allow applications to share data and functionality
#   - APIs enable developers to build applications that can work together
#3. APIs can be used to access data from a remote server or service
#   - They allow applications to retrieve, create, update, or delete data
#   - APIs can be used to interact with databases, web services, or other applications  
#4. APIs can be categorized into different types based on their functionality
#   - RESTful APIs, SOAP APIs, GraphQL APIs, etc.   
#5. APIs can be accessed using different protocols such as HTTP, HTTPS, or WebSocket
#   - The most common protocol for web APIs is HTTP/HTTPS
#   - APIs can also use other protocols like gRPC, MQTT, or AMQP    


#understanding RESTful APIs:
#REST stands for Representational State Transfer
#RESTful APIs are a type of web API that follows the principles of REST
#RESTful APIs use HTTP methods to perform operations on resources
#Resources are identified by URLs (Uniform Resource Locators)
#RESTful APIs use standard HTTP methods such as GET, POST, PUT, DELETE, and PATCH
#1. GET: Retrieve data from a resource
#2. POST: Create a new resource
#3. PUT: Update an existing resource
#4. DELETE: Delete a resource
#5. PATCH: Partially update a resource  


#key principles of RESTful APIs:
#1. Stateless: Each request from the client to the server must contain all the information needed
#   to understand and process the request. The server does not store any client context between requests
#2. Client-Server Architecture: The client and server are separate entities that communicate over a network
#   - The client is responsible for the user interface and user experience
#   - The server is responsible for processing requests and managing data
#3. Uniform Interface: RESTful APIs have a consistent and standardized way of interacting with resources
#   - This includes using standard HTTP methods, status codes, and data formats (usually JSON or XML)
#4. Resource-Based: RESTful APIs are centered around resources, which are identified by URLs
#   - Each resource can have multiple representations (e.g., JSON, XML)
#5. Cacheable: Responses from the server can be cached by the client to improve performance
#   - This allows clients to reuse previously fetched data without making additional requests  
#6. Layered System: RESTful APIs can be composed of multiple layers, such as load balancers, proxies, and servers
#   - Each layer can have its own responsibilities and can be added or removed without affecting the overall system
#7. Code on Demand (optional): Servers can provide executable code to clients,
#   allowing clients to extend their functionality dynamically



#example of a RESTful API end point:
#POST /api/users - Create a new user
#GET /api/users - Retrieve a list of users
#GET /api/users/{id} - Retrieve a specific user by ID
#PUT /api/users/{id} - Update a specific user by ID
#DELETE /api/users/{id} - Delete a specific user by ID

# APIs can be categorized into different types based on their functionality and usage
#1. Web APIs: These are APIs that are accessed over the internet using HTTP/HTTPS
#   - They are commonly used to interact with web services and applications.
#   - Examples include RESTful APIs, SOAP APIs, and GraphQL APIs.
#2. Library APIs: These are APIs that are provided by programming libraries or frameworks
#   - They allow developers to use pre-defined functions and methods to perform specific tasks.     
#   - Examples include the Python Standard Library, Java API, and .NET Framework API.
#3. Operating System APIs: These are APIs that provide access to the underlying operating system functionality
#   - They allow applications to interact with the OS for tasks like file management, process control
#   - Examples include Windows API, POSIX API, and Android API. 
#4. Hardware APIs: These are APIs that allow software applications to interact with hardware devices
#   - They provide access to hardware features and functionalities.
#   - Examples include USB API, Bluetooth API, and Camera API.
#5. Database APIs: These are APIs that allow applications to interact with databases
#   - They provide methods for querying, updating, and managing data in databases.
#   - Examples include SQL API, MongoDB API, and Firebase API.
#6. Cloud APIs: These are APIs provided by cloud service providers to access their services
#   - They allow applications to leverage cloud resources and functionalities.
#   - Examples include AWS API, Google Cloud API, and Azure API.

#cosuming APIs in python:
#python provides several libraries to interact with APIs such as requests, http.client, urllib, and 'urllib2'
#the most popular library is requests, which is a simple and easy-to-use library for making HTTP requests
#requests library is not included in the standard library, so you need to install it

#live Demo: using requests library to consume APIs
import requests

#example API endpoint
#using Get method ro retrieve data from a public API
url = "https://jsonplaceholder.typicode.com/posts"
#check  if the request was successful
response = requests.get(url)
print(f"Response status code: {response.status_code}")
print('response.json()', response.json())