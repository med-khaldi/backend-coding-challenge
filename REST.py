import json
import requests
from collections import Counter

Counter()
# Variables
m = []   # Liste of a all  the languages used
n = []   # Liste of all the users
z = {}   # The list of repos using the language


#Get the JSON file  from github
request = requests.get("https://api.github.com/search/repositories?q=created:")
f = request.text

data = json.loads(f)
for l in data['items'] :
    for i,k in l.items():
        if i == 'language':
            m.append(k)
    for i,k in l.items() :
        if i == 'full_name':
            n.append(k)
c = Counter(m) # Number of repos using this language
p = zip(m,n)
t = tuple(p)

for i in t:
    if i[0] in z.keys():
        z[i[0]].append(i[1])
    else:
        z[i[0]] = [i[1]]

# code below create a file json 
with open ("Result.json", "w") as outfile:
    json.dump(z, outfile)
    json.dump(c, outfile)




