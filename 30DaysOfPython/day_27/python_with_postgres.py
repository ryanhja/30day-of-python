from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from dotenv import load_dotenv
import psycopg2

load_dotenv()

app = Flask(__name__)

db_host = getenv("DB_HOST")
db_port = getenv("DB_PORT")
db_name = getenv("DB_NAME")
db_user = getenv("DB_USER")
db_password = getenv("DB_PASSWORD")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    age = db.Column(db.Integer)


students = [
    Student(name='David', country='UK', city='London', age=34),
    Student(name='John', country='Sweden', city='Stockholm', age=28),
    Student(name='Sami', country='Finland', city='Helsinki', age=25),
]

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        if not Student.query.first():
            db.session.add_all(students)
            db.session.commit()

        students = Student.query.all()
        for student in students:
            print(f"{student.name} ({student.age} ans) - {student.city}, {student.country}")

    app.run(host='0.0.0.0', port=3000, debug=True)
