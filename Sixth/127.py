import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    try:
        print(f"Fetching content from {url}...")
        response = requests.get(url)
        print(f"Received response with status code: {response.status_code}")
        response.raise_for_status()  # Check if the request was successful
        response.encoding = 'utf-8'  # Ensure the response encoding is set to utf-8
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

if __name__ == "__main__":
    url = "http://127.0.0.1/index.html"  # 或者 "http://127.0.0.1:8080/index.html" 如果你使用的是端口 8080
    content = fetch_content(url)
    if content:
        print("Fetched content:")
        soup = BeautifulSoup(content, 'html.parser')
        with open("fetched_content.html", "w", encoding="utf-8") as file:
            file.write(soup.prettify())
