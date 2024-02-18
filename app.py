from flask import Flask, request, render_template, redirect
import sqlite3
import csv
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Change this to your desired upload folder path

def get_db_connection():
    conn = sqlite3.connect('WorkoutPlan.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('home.html', title="Fitness Tracker", users=users)

@app.route('/add-user')
def add_user():
    return render_template('add_user.html', title="Add User")

@app.route('/add-user-submit', methods=['POST'])
def add_user_submit():
    conn = get_db_connection()
    cursor = conn.cursor()
    data = request.form
    cursor.execute("INSERT INTO users (name, age, weight, height, fitness_goals, experience) VALUES (?, ?, ?, ?, ?, ?)", (data['name'], data['age'], data['weight'], data['height'], data['fitness_goals'], data['experience']))
    conn.commit()
    conn.close()
    return "User added successfully"

@app.route('/exercises')
def exercises():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exercises")
    exercises = cursor.fetchall()
    conn.close()
    return render_template('exercises.html', title="Exercises", exercises=exercises)

@app.route('/add-exercise')
def add_exercise():
    return render_template('add_exercise.html', title="Add Exercise")

@app.route('/add-exercise-submit', methods=['POST'])
def add_exercise_submit():
    conn = get_db_connection()
    cursor = conn.cursor()
    data = request.form
    cursor.execute("INSERT INTO exercises (name, description, muscle_group, difficulty) VALUES (?, ?, ?, ?)", (data['name'], data['description'], data['muscle_group'], data['difficulty']))
    conn.commit()
    conn.close()
    return "Exercise added successfully"

@app.route('/import-exercises')
def import_exercises():
    filepath = os.path.join('static', 'exercises.csv')  # Path to your CSV file

    with open(filepath, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        conn = get_db_connection()
        cursor = conn.cursor()

        for row in csv_reader:
            cursor.execute("INSERT INTO exercises (name, description, muscle_group, difficulty) VALUES (?, ?, ?, ?)",
                           (row['name'], row['description'], row['muscle_group'], row['difficulty']))

        conn.commit()
        conn.close()

    return "Exercises imported successfully"


if __name__ == '__main__':
    app.run(debug=True)

