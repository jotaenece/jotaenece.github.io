import feedparser
import yaml
import os

# 1. Tu URL de RSS de Goodreads
RSS_URL = "https://www.goodreads.com/review/list_rss/187136448?key=IZS-tyd_bZWmjQADbrUx3aw1bmtX4ElCJTCnvnAY5aoIoi9c&shelf=read"

def sync_goodreads():
    feed = feedparser.parse(RSS_URL)
    books = []

    for entry in feed.entries:
        # Extraemos la data limpia
        book = {
            "title": entry.title,
            "author": entry.author_name if 'author_name' in entry else "Desconocido",
            "link": entry.link,
            "rating": entry.user_rating if 'user_rating' in entry else "0",
            "review": entry.summary, # Goodreads mete la reseña y la foto aquí
            "image": entry.book_large_image_url if 'book_large_image_url' in entry else ""
        }
        books.append(book)

    # 2. Guardamos en la carpeta _data para que Jekyll lo lea
    os.makedirs('_data', exist_ok=True)
    with open('_data/lecturas_goodreads.yml', 'w', encoding='utf-8') as f:
        yaml.dump(books, f, allow_unicode=True)

if __name__ == "__main__":
    sync_goodreads()
