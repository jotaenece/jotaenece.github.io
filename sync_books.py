import feedparser
import yaml
import os

BASE_URL  = "https://www.goodreads.com/review/list_rss/187136448?key=IZS-tyd_bZWmjQADbrUx3aw1bmtX4ElCJTCnvnAY5aoIoi9c&shelf="
READ_URL    = BASE_URL + "read"
READING_URL = BASE_URL + "currently-reading"

def sync_goodreads():
    os.makedirs('_data', exist_ok=True)

    # ── Libros leídos ──────────────────────────────────────────
    feed = feedparser.parse(READ_URL)
    books = []
    for entry in feed.entries:
        books.append({
            "title":  entry.title,
            "author": entry.get("author_name", "Desconocido"),
            "link":   entry.link,
            "rating": entry.get("user_rating", "0"),
            "review": entry.summary,
            "image":  entry.get("book_large_image_url", ""),
        })

    with open('_data/lecturas_goodreads.yml', 'w', encoding='utf-8') as f:
        yaml.dump(books, f, allow_unicode=True)

    # ── Leyendo ahora ──────────────────────────────────────────
    # Preserva el progreso manual si el libro no ha cambiado.
    leyendo_path = '_data/leyendo_ahora.yml'
    existing = {}
    if os.path.exists(leyendo_path):
        with open(leyendo_path, 'r', encoding='utf-8') as f:
            existing = yaml.safe_load(f) or {}

    reading_feed = feedparser.parse(READING_URL)
    if reading_feed.entries:
        entry    = reading_feed.entries[0]
        new_title = entry.title
        current = {
            "title":    new_title,
            "author":   entry.get("author_name", "Desconocido"),
            "link":     entry.link,
            "image":    entry.get("book_large_image_url", ""),
            # Mantiene el progreso si el libro no cambió; si cambió, empieza en 0
            "progress": existing.get("progress", 0) if existing.get("title") == new_title else 0,
        }
    else:
        # Sin libro en curso: conserva el estado existente o vacía
        current = existing if existing else {
            "title": "", "author": "", "link": "", "image": "", "progress": 0
        }

    with open(leyendo_path, 'w', encoding='utf-8') as f:
        yaml.dump(current, f, allow_unicode=True)

if __name__ == "__main__":
    sync_goodreads()
