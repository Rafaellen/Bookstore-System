from flask import Flask, render_template, request, redirect, url_for, flash
from models import create_table, add_book, get_book, update_price, get_book_by_id, remove_book, find_book, export_csv

app = Flask(__name__)
app.secret_key = 'chave_secreta_qualquer'
create_table()


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/books')
def list_books():
    books = get_book()
    return render_template('lista.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_new_book():
    if request.method == 'POST':
        title = request.form['titulo_livro']
        author = request.form['autor_livro']
        year = int(request.form['ano_livro'])
        price = float(request.form['preco_livro'])
        add_book(title, author, year, price)

        return redirect(url_for('list_books'))
    return render_template('add.html')


@app.route('/update/<int:book_id>', methods=['GET', 'POST'])
def update_book_price(book_id):
    if request.method == 'POST':
        new_price = float(request.form['preco_livro'])
        update_price(book_id, new_price)
        return redirect(url_for('list_books'))

    book = get_book_by_id(book_id)
    return render_template('update.html', book=book)


@app.route('/remove/<int:book_id>)', methods=['POST'])
def del_book(book_id):
    remove_book(book_id)
    return redirect(url_for(('list_books')))


@app.route('/search', methods=['GET', 'POST'])
def fd_book():
    if request.method == 'POST':
        author = request.form['autor']
        books = find_book(author)
        return render_template('lista.html', books=books)


@app.route('/export')
def exp_csv():
    export_csv()
    flash('Livros exportados com sucesso para CSV!', 'success')
    return redirect(url_for('list_books'))


if __name__ == '__main__':
    app.run(debug=True)
