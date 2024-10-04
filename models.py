import sqlite3
import csv
import shutil
from config import DB_PATH, EXPORT_DIR, BACKUP_DIR
from datetime import datetime


def connect():
    db_conn = sqlite3.connect(DB_PATH)
    return db_conn


def create_table():
    db_connect = connect()
    x = db_connect.cursor()
    x.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano_publicacao INTEGER,
        preco REAL
    );
    """)
    db_connect.commit()
    db_connect.close()


def add_book(title, author, year, price):
    db_connect = connect()
    x = db_connect.cursor()
    x.execute("INSERT INTO books (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)",
              (title, author, year, price))
    db_connect.commit()
    db_connect.close()
    print(f"Added book: {title}, {author}, {year}, {price}")


def get_book():
    db_connect = connect()
    x = db_connect.cursor()
    x.execute("SELECT * FROM books")
    books = x.fetchall()
    db_connect.close()
    return books


def update_price(book_id, new_price):
    db_connect = connect()
    x = db_connect.cursor()
    x.execute("UPDATE books SET preco = ? WHERE id = ?", (new_price, book_id))
    db_connect.commit()
    db_connect.close()


def get_book_by_id(book_id):
    db_connect = connect()
    x = db_connect.cursor()
    x.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = x.fetchone()
    db_connect.close()
    return book


def export_csv():
    get_books = get_book()
    with open(EXPORT_DIR / 'livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        w = csv.writer(csvfile)
        w.writerow(['ID', 'titulo', 'Autor', 'Ano de Publicação', 'Preço'])
        w.writerow(get_books)


def db_backup():
    datetime_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    bck = BACKUP_DIR / f"bck_livraria_{datetime_now}.db"
    shutil.copy(DB_PATH, bck)


def remove_book(book_id):
    db_connect = connect()
    x = db_connect.cursor()
    x.execute("DELETE FROM books WHERE id = ?", (book_id,))
    db_connect.commit()
    db_connect.close()


def find_book(author):
    db_connect = connect()
    x = db_connect.cursor()
    x.execute("SELECT * FROM books WHERE autor LIKE ?", ('%' + author + '%',))
    books = x.fetchall()
    db_connect.close()
    return books


def export_csv():
    books = get_book()
    with open(EXPORT_DIR / 'livros.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['ID', 'Título', 'Autor', 'Ano de Publicação', 'Preço'])
        writer.writerows(books)
