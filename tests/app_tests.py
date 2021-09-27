"""Test out the url functionality."""
import requests


url = 'https://lh3.googleusercontent.com/pw/AM-JKLUQD6yKx4-8wCLJXk8PuWn-GRWJJEKROZJuAV08OOYMfG-8kjYpni2R2SJj1s9JgpYWp7uyOf2oSesLzIxmsbKsfs8iOHGDXjwnp6IlLhltvHDFMoWXFhntq23rYpNhe3oO4m_8us4Wo4Qnd-IBT9WglA=w1992-h1328-no?authuser=0'
url_img = requests.get(url)

with open('static/url_image.jpg', 'wb') as f:
    f.write(url_img.content)

# path = meme.make_meme(img, quote.body, quote.author, dynamic_out=False)