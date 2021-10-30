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
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Lincoln" in resp.text


def test_washington():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Washington" in resp.text


def test_adams():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Adams" in resp.text


def test_jefferson():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Jefferson" in resp.text


def test_madison():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Madison" in resp.text


def test_Monroe():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Monroe" in resp.text


def test_Jackson():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Jackson" in resp.text


def test_buren():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Buren" in resp.text


def test_harrison():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Harrison" in resp.text


def test_tyler():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Tyler" in resp.text


def test_polk():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Polk" in resp.text


def test_taylor():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Taylor" in resp.text


def test_fillmore():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Fillmore" in resp.text


def test_Pierce():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Pierce" in resp.text


def test_Buchanan():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Buchanan" in resp.text


def test_johnson():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Johnson" in resp.text


def test_grant():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Grant" in resp.text


def test_hayes():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Hayes" in resp.text


def test_garfield():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Garfield" in resp.text


def test_arthur():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Arthur" in resp.text


def test_cleveland():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Cleveland" in resp.text


def test_mckinley():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "McKinley" in resp.text


def test_roosevelt():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Roosevelt" in resp.text


def test_taft():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Taft" in resp.text


def test_wilson():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Wilson" in resp.text


def test_harding():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Harding" in resp.text


def test_coolidge():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Coolidge" in resp.text


def test_hoover():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Hoover" in resp.text


def test_lincoln():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Lincoln" in resp.text


def test_truman():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Truman" in resp.text


def test_eisenhower():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Eisenhower" in resp.text


def test_kennedy():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Kennedy" in resp.text


def test_nixon():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Nixon" in resp.text


def test_ford():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Ford" in resp.text


def test_carter():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Carter" in resp.text


def test_reagan():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Reagan" in resp.text


def test_bush():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Bush" in resp.text


def test_clinton():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Clinton" in resp.text


def test_obama():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Obama" in resp.text


def test_trump():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Trump" in resp.text


def test_biden():
    resp = requests.get(presidents_url)
    data = resp.json()
    relatedtopics = data['RelatedTopics']
    for i in relatedtopics:
        print(i['FirstURL'])
        assert "Biden" in resp.text
