import requests

api_key = 'be49600b-3dbb-4bab-9534-8981baf43053'
word = 'kentang'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)