import requests
from bs4 import BeautifulSoup
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Baad mein replace karna

url = "https://www.reuters.com/business/economics/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find_all('h3')  # Class adjust karna pad sakta hai
articles = [h.text.strip() for h in headlines[:5]]

prompt = f"Write a 300-word economics blog based on: {articles}"
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=300
)
blog_post = response.choices[0].text.strip()

with open("blog.txt", "w", encoding="utf-8") as file:
    file.write(blog_post)

print("Blog saved to blog.txt")