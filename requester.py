# Problem description
# Find out if there are any duplicate urls used in the
# json placeholder photo data


import requests

url = 'http://api.duckduckgo.com/?q="presidents of the united states"&format=json'

# get the data about the photos
response = requests.get(url)
json_data = response.json()

# create a list
RelatedTopics = []
for name in json_data:
    RelatedTopics.append(name['url'])

# How many items are in the url list (Should be 5000 since we have 5000 photos in our dataset)?
print(len(RelatedTopics))

# How many items are there if we turn that list into a set?
print(len(set(RelatedTopics)))
