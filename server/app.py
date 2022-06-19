from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:12345@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# enable CORS
CORS(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    isRead = db.Column(db.Boolean)

    def __init__(self, title, author, text, isRead):
        self.title = title
        self.author = author
        self.text = text
        self.isRead = isRead


class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'text', 'isRead')


book_schema = BookSchema()
books_schema = BookSchema(many=True)


@app.route('/get', methods=['GET'])
def get_books():
    all_books = Books.query.all()
    results = books_schema.dump(all_books)
    return jsonify(results)


@app.route('/get/<id>/', methods=['GET'])
def book_details(id):
    book = Books.query.get(id)
    return book_schema.jsonify(book)


@app.route('/add', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    text = request.json['text']
    isRead = request.json['isRead']

    books = Books(title, author, text, isRead)
    db.session.add(books)
    db.session.commit()
    return book_schema.jsonify(books)


@app.route('/update/<id>/', methods=['PUT'])
def update_book(id):
    book = Books.query.get(id)

    title = request.json['title']
    author = request.json['author']
    text = request.json['text']
    isRead = request.json['isRead']

    book.title = title
    book.author = author
    book.text = text
    book.isRead = isRead

    db.session.commit()
    return book_schema.jsonify(book)


@app.route('/delete/<id>/', methods=['DELETE'])
def delete_book(id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return book_schema.jsonify(book)


if __name__ == '__main__':
    app.run()
