from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Database model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(20), nullable=False)

# Home page — list all students
@app.route('/')
def home():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Add a student
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    grade = request.form['grade']
    new_student = Student(name=name, grade=grade)
    db.session.add(new_student)
    db.session.commit()
    return redirect('/')

# Delete a student
@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

# Edit student (show edit form)
@app.route('/edit/<int:id>')
def edit_student(id):
    student = Student.query.get(id)
    return render_template('edit.html', student=student)

# Update student (handle form submission)
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    student = Student.query.get(id)
    student.name = request.form['name']
    student.grade = request.form['grade']
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

