import sqlite3

# Connect to the fitness tracker database
con = sqlite3.connect("WorkoutPlan.db")
cur = con.cursor()

# Fetching and printing all users
print("Users:")
res = cur.execute("SELECT * FROM users")
print(res.fetchall())

# Fetching and printing all exercises
print("\nExercises:")
res = cur.execute("SELECT * FROM exercises")
print(res.fetchall())

# Plan:
# 1. Create a simple HTML web page with a form for adding a user or an exercise.
#    - The form for adding a user should include fields for name, age, weight, height, fitness goals, and experience.
#    - The form for adding an exercise should include fields for name, description, muscle group, and difficulty.
#
# 2. Update this script or create a new one to handle HTTP requests and form submissions.
#    - You can use a Python web framework like Flask for this. It will allow you to receive data from the web form and insert it into the database.
#
# 3. Create a web page that shows results from the database.
#    - This page can display a list of users and their details, as well as a list of exercises.
#    - You can use Flask's `render_template` function to integrate the data with your HTML templates.

