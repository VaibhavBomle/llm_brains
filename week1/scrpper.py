from bs4 import BeautifulSoup
import requests

# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def fetch_website_content(url): 

    respose = requests.get(url, headers=headers)
    soup =  BeautifulSoup(respose.content, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]

def fetch_website_links(url):
   response = requests.get(url,headers=headers)
   soup = BeautifulSoup(response.content, 'html.parser')
   links = [soup.get("href" for link in soup.find_all("a"))]
   return [link for link in links if link]


print(fetch_website_content("https://www.wikipedia.org/"))

print("================================")
print(fetch_website_links("https://www.wikipedia.org/"))



