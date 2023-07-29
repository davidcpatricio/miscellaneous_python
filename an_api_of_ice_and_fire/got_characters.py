import requests as rw
import pandas as pd

# Obter a primeira página de resultados
url_characters = "https://anapioficeandfire.com/api/characters?page=%d&pageSize=50"
request_characters = rw.get(url_characters)
json_characters = request_characters.json()
got_characters = pd.DataFrame(json_characters)

# Agregar os resultados de todas as páginas num único dataframe
characters_page = 2
while True:
    new_characters_page = url_characters.replace('%d', str(characters_page))
    new_characters_request = rw.get(new_characters_page)
    new_json_characters = new_characters_request.json()
    if len(new_json_characters) != 0:
        new_got_characters = pd.DataFrame(new_json_characters)
        got_characters = pd.concat([got_characters, new_got_characters], ignore_index=True, axis=0)
        characters_page += 1
    else:
        break

print(got_characters)