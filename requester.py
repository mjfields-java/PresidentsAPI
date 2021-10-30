# Problem description
# Find out if there are any duplicate urls used in the
# json placeholder photo data


import requests

url = 'http://api.duckduckgo.com/?q="presidents of the united states"&format=json'

# get the data about the photos
response = requests.get(url)
json_data = response.json()

# create a list
List1 = []
for data in json_data:
    List1.append(data)

# How many items are in the url list (should be 21)
print(List1)

# How many items are there if we turn that list into a set?
print(len(set(List1)))
List2 = []
for name in response.json():
    List2.append(name)
    # print(List2)
print('RelatedTopics' in response.json())
print(json_data)
List3 = []
resp = requests.get(url)
rsp_data = resp.json()
relatedTopics = rsp_data['RelatedTopics']
# print(*relatedTopics, sep = "\n")
for i in relatedTopics:
    print(i['Result'])
    print('Lincoln' in resp.text)
# print('Lincoln' in "https://duckduckgo.com/Abraham_Lincoln")
