import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'a4f1e2df2d4e5c4977d62ffbc31bbcb7'
Header = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

def test_status_code():
    response = requests.get(url = f'{URL}trainers', params= {'trainer_id' : 6048})
    assert response.status_code == 200


"""- Проверь, что ответ запрос **GET /trainers** приходит с кодом 200
- Проверь, что в ответе приходит строчка с именем твоего тренера
(Не забудь прописать в **квери** id твоего тренера (`trainer_id`))"""

