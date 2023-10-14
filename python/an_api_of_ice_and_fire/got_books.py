import requests as rw
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Obter o dataframe com a lista de livros
url_books = "https://anapioficeandfire.com/api/books/?page=%1&pageSize=50"
request_books = rw.get(url_books)
json_books = request_books.json()
got_books = pd.DataFrame(json_books)
# print(got_books)

# Número de personagens em cada livro
character_count = []
for i in range(len(got_books)):
    character_count.append(len(got_books.iloc[i].characters))

# Acrescentar a coluna das contagens ao dataframe
got_books["characterCount"] = character_count
print(got_books)

# Gráfico de barras com o número de personagens por livro
fig, ax = plt.subplots(figsize=(24, 6))
sns.barplot(data=got_books, x="name", y="characterCount")
for item in ax.get_xticklabels():
    item.set_rotation(45)
plt.show()
