from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime
# feel free to change anything here that affects you're task. This is just to get started.
# note the implementation of these methods is to be done by the database people,
# so any processing of data should be done before calling them - these methods are just for storing the data.

# TODO create the queries for the database

"""
not sure how to use abstract methods so will leave it alone for now
im assuming we're having different users?
not sure what the goal thing is actually meant to be
now making the start of the database and will wait to see what others think
"""

class Database(ABC):
    # not actually sure what data about workouts is going to be logged.
    # maybe modify to store just an estimated 1rm rather than sets and reps?
    @abstractmethod
    def logExercise(self, exercise, sets, reps, weight):
        pass

    @abstractmethod
    def logBodyweight(self, weight):
        pass

    # return current bodyweight
    @abstractmethod
    def getBodyweight(self):
        pass

    # return array of (int time, int bodyweight)
    @abstractmethod
    def getBodyweightHistory(self):
        pass

    # return an array of tuples? e.g. (int time, int estimated_1rm) or (int time, int sets, int reps, float weight)
    @abstractmethod
    def getExerciseHistory(self, exercise):
        pass

    # am assuming a Goal class will be made
    @abstractmethod
    def storeGoal(self, goal):
        pass

    # have no idea how this is going to work, this will need to be changed.
    # method to update whether a goal has been met or not.
    @abstractmethod
    def updateGoal(self):
        pass

    # return array of goals
    @abstractmethod
    def getGoals(self):
        pass

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def setAge(self, age):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getAge(self):
        pass


class Database_():
    def __init__(self, db_name="gymapp.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
    def __del__(self):
        self.close()

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cursor = None


    def createDatabase(self):
        self.cursor.execute("PRAGMA foreign_keys = OFF;")
        self.cursor.execute("DROP TABLE IF EXISTS bodyweight;")
        self.cursor.execute("DROP TABLE IF EXISTS exercise_names;")
        self.cursor.execute("DROP TABLE IF EXISTS exercise;")
        self.cursor.execute("DROP TABLE IF EXISTS users;")
        self.cursor.execute("PRAGMA foreign_keys = ON;")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email INTEGER NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bodyweight (
                bodyweight_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                bodyweight REAL NOT NULL,
                bodyweight_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            );
        """)

        # TODO the below can be combined into exercises table depending on what the plan is
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS exercise_names (
                exercise_name_id INTEGER PRIMARY KEY,
                exercise_name TEXT NOT NULL UNIQUE,
                category TEXT NOT NULL  
            );         
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                session_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                session_date DATETIME NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            );
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS exercise (
                exercise_id INTEGER PRIMARY KEY,
                session_id INTEGER,
                exercise_name_id INTEGER,
                sets INTEGER NOT NULL,
                reps INTEGER NOT NULL,
                weight INTEGER,
                FOREIGN KEY (session_id) REFERENCES sessions(session_id),
                FOREIGN KEY (exercise_name_id) REFERENCES exercise_names(exercise_name_id)
            );
        ''')
        self.conn.commit()



def tests():
    # run any tests in this function
    db = Database_()
    db.createDatabase()
    db.cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", ("test", "test", "test"))
    db.cursor.execute("INSERT INTO bodyweight (user_id, bodyweight) VALUES (?, ?)", (1, 80))
    db.cursor.execute("INSERT INTO exercise_names (exercise_name, category) VALUES (?, ?)", ("bench", "workout A"))
    db.cursor.execute("INSERT INTO sessions (user_id, session_date) VALUES (?, ?)", (1, datetime.now()))
    db.cursor.execute("INSERT INTO exercise (session_id, exercise_name_id, sets, reps, weight) VALUES (?, ?, ?, ?, ?)", (1, 1, 3, 10, 80))
    db.cursor.execute("SELECT * FROM users")
    print(db.cursor.fetchall())
    db.cursor.execute("SELECT * FROM bodyweight")
    print(db.cursor.fetchall())
    db.cursor.execute("SELECT * FROM exercise_names")
    print(db.cursor.fetchall())
    db.cursor.execute("SELECT * FROM sessions")
    print(db.cursor.fetchall())
    db.cursor.execute("SELECT * FROM exercise")
    print(db.cursor.fetchall())

if __name__ == "__main__":
    tests()