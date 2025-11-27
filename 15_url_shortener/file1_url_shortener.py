import requests

def shorten_url(url):
    api = "https://tinyurl.com/api-create.php"
    res = requests.get(api, params={"url": url})
    return res.text
