import requests
import json





def add_quotes(payload):
    res = requests.post("http://0.0.0.0:8685/quotes",json.dumps(payload))
    return res

def get_quotes():
    res = requests.get("http://0.0.0.0:8685/quotes")
    return res

def get_quote_by_id(quote_id):
    res = requests.get("http://0.0.0.0:8685/quotes/{}".format(quote_id))
    return res

def update_quotes(quotes_id,payload):
    res = requests.put("http://0.0.0.0:8685/quotes/{}".format(quotes_id),json.dumps(payload))
    return res

def delete_quotes(quotes_id):
    res = requests.delete("http://0.0.0.0:8685/quotes/{}".format(quotes_id))
    return res


def test_api():
    payload = {"content": "lorem ipsum dolor sit amet"}
    res = add_quotes(payload)

    # Test status code
    # test if input == stored
    # test if response contains Id

    assert res.status_code == 200
    assert res.json()['content'] == payload["content"]
    assert "id" in res.json(), "should contain id"

    quotes_id = res.json()["id"]

    res = get_quote_by_id(quotes_id)
    assert res.status_code == 200
    assert res.json()['content'] == payload["content"]

    payload = {"content": "lorem ipsum dolor sit amet"}
    res = add_quotes(payload)
    all_quotes = get_quotes()

    assert res.status_code == 200
    quotes = [i["content"] for i in all_quotes.json()]
    count = quotes.count("lorem ipsum dolor sit amet")
    assert count == 1, "Quotes shouldn't have duplicate"

    payload = {"content" : "amet sit dolor ipsum lorem"}
    res = update_quotes(quotes_id,payload)

    assert res.status_code == 200
    assert res.json()['content'] == payload["content"]
    assert "id" in res.json(), "should contain id"

    res = delete_quotes(quotes_id)
    assert res.status_code == 200
