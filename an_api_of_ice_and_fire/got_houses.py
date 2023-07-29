import requests as rw
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

url_houses = "https://anapioficeandfire.com/api/houses/?page=1&pageSize=50"
request_houses = rw.get(url_houses)
json_houses = request_houses.json()
got_houses = pd.DataFrame(json_houses)

houses_page = 2
while True:
    new_houses_page = "https://anapioficeandfire.com/api/houses/?page={}&pageSize=50".format(str(houses_page))
    new_houses_request = rw.get(new_houses_page)
    new_json_houses = new_houses_request.json()
    if len(new_json_houses) != 0:
        new_got_houses = pd.DataFrame(new_json_houses)
        got_houses = pd.concat([got_houses, new_got_houses], ignore_index=True, axis=0)
        houses_page += 1
    else:
        break

# Número de membros de cada casa
total_members = []
for i in range(len(got_houses)):
    total_members.append(len(got_houses.iloc[i].swornMembers))

# Acrescentar a coluna das contagens ao dataframe
got_houses["totalMembers"] = total_members
got_houses = got_houses.sort_values(by="totalMembers", ascending=False)
print(got_houses)

fig, ax = plt.subplots(figsize=(24,12))
count, houses, pct = plt.pie(got_houses.head(8).totalMembers, labels=got_houses.head(8).name, autopct='%.0f%%')
plt.setp(pct, size=14, weight="bold", color="white")
plt.show()