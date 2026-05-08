# Day 29: 30 Days of python programming

from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/api/v1/students', methods=['GET'])
def students():
    student_list = [
        {
            'name': 'Rayan',
            'country': 'Madagascar',
            'city': 'Antananarivo',
            'skills': ['Python', 'Flask', 'DBT', 'Apache Airflow']
        },
        {
            'name': 'David',
            'country': 'UK',
            'city': 'London',
            'skills': ['Python', 'MongoDB']
        },
        {
            'name': 'John',
            'country': 'Sweden',
            'city': 'Stockholm',
            'skills': ['Java', 'C#']
        },
        {
            'name': 'Joe',
            'country': 'Doe',
            'city': 'Australia',
            'skills': ['C', 'Rust', 'C++']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
