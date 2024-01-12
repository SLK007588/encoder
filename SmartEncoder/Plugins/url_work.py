from config import Config
import requests

def short_me(token: str) -> str:
    short_url = requests.get(Config.URL + token, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})

    if short_url.json()['status'] == "success":
        return short_url.json()['shortenedUrl']

    return None
