import requests

url_ddg = "https://api.duckduckgo.com"

presidents_url = 'http://api.duckduckgo.com/?q="presidents of the united states"&format=json'


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]


def test_presidents():
    resp = requests.get(presidents_url)
    rsp_data = resp.json()
    assert 'RelatedTopics' in rsp_data


def test_lincoln():
    resp = requests.get(presidents_url)
    data = resp.json()
    assert 'Lincoln' in data
