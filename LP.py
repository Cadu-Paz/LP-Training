from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def __init__(self):
        self.students = []

    def post(self):
        data = request.get_json()
        new_student = {
            'id': len(self.students) + 1,
            'name': data['name'],
            'age': data['age'],
            'height': data['height'],
            'initial_weight': data['initial_weight'],
            'current_weight': data['current_weight'],
            'goal': data['goal']
        }
        self.students.append(new_student)
        return new_student, 201

    def put(self, id):
        data = request.get_json()
        for student in self.students:
            if student['id'] == int(id):
                student.update(data)
                return student, 200
        return {'message': 'Student not found'}, 404

class Exercise(Resource):
    def __init__(self):
        self.exercises = []

    def post(self):
        data = request.get_json()
        new_exercise = {
            'name': data['name'],
            'weight': data['weight'],
            'repetitions': data['repetitions'],
            'sets': data['sets']
        }
        self.exercises.append(new_exercise)
        return new_exercise, 201

api.add_resource(Student, '/student', '/student/<int:id>')
api.add_resource(Exercise, '/exercise')

if __name__ == '__main__':
    app.run(debug=True)