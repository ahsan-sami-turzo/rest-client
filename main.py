import http.client
import json

# Create a connection
conn = http.client.HTTPConnection("localhost", 9091)

# Send a GET request
conn.request("GET", "/")

# Get the response
response = conn.getresponse()

# Read the response
data = response.read()

# Decode the response
cities = json.loads(data)

# Print the cities
for city in cities:
    print(city)

# Close the connection
conn.close()
