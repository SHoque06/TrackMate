from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime
# feel free to change anything here that affects you're task. This is just to get started.
# note the implementation of these methods is to be done by the database people,
# so any processing of data should be done before calling them - these methods are just for storing the data.

"""
needs validation eventually and more testing

how does the goal work?

what the db does rn 
    1. you have a user
    2. user starts a workout/session
    3. user logs exercises that they did in said session
    
    2. user logs bodyweight, separate from rest of program
    
added functions:
getBodyweightHistory      # bodyweight, bodyweight_date
getExerciseNameIdFromName # exercise_name_id
getExerciseInfo           # exercise_name_id, exercise_name, category
getAllSessionsByUserId    # session_id, user_id, session_date
getExerciseHistoryByName  # session_id, exercise_name_id, sets, reps, weight
logBodyweight
logExercise
createNewSession
removeUser
createUser
createDatabase  # removes all tables and creates new ones 
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
        self.user_id = 1 # change this and wherever this is used if we ever have multiple users
    def __del__(self):
        self.close()

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cursor = None


    def createDatabase(self):
        # Will delete all tables...
        self.cursor.execute("PRAGMA foreign_keys = OFF;")
        self.cursor.execute("DROP TABLE IF EXISTS bodyweight;")
        self.cursor.execute("DROP TABLE IF EXISTS exercise_names;")
        self.cursor.execute("DROP TABLE IF EXISTS exercise;")
        self.cursor.execute("DROP TABLE IF EXISTS sessions;")
        self.cursor.execute("DROP TABLE IF EXISTS users;")
        self.cursor.execute("PRAGMA foreign_keys = ON;")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bodyweight (
                bodyweight_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                bodyweight REAL NOT NULL,
                bodyweight_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            );
        """)

        # TODO not much point in this table. could integrate into exercise table
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
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
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
                FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
                FOREIGN KEY (exercise_name_id) REFERENCES exercise_names(exercise_name_id)
            );
        ''')


        # going to add in one default user
        # if we ever have multiple users,
        # remove this and update the functions
        self.createUser("main", "main", "main")
        self.conn.commit()

    def createUser(self, username, password, email):
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username must be a non-empty string.")
        if not isinstance(password, str) or not password.strip():
            raise ValueError("Password must be a non-empty string.")
        if not isinstance(email, str) or "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")   
        self.cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
        self.conn.commit()

    def removeUser(self, username):
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username must be a non-empty string.")
        self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        self.conn.commit()

    def createNewSession(self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        if not isinstance(user_id, int) or user_id < 1:
            raise ValueError("User ID must be a positive integer.")
        self.cursor.execute("INSERT INTO sessions (user_id, session_date) VALUES (?, ?)", (user_id, datetime.now()))
        self.conn.commit()

    def getAllSessionsByUserId(self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        # session_id, user_id, session_date
        self.cursor.execute("SELECT * FROM sessions WHERE user_id = ? ORDER BY session_date DESC", (user_id,))
        return self.cursor.fetchall()

    def getExerciseInfo(self):
        # exercise_name_id, exercise_name, category
        self.cursor.execute("SELECT * FROM exercise_names")
        return self.cursor.fetchall()

    def getExerciseNameIdFromName(self, exercise_name):
        # exercise_name_id, exercise_name, category
        
        if not isinstance(exercise_name, str) or not exercise_name.strip():
            raise ValueError("Exercise name must be a non-empty string."     
        self.cursor.execute("SELECT exercise_name_id FROM exercise_names WHERE exercise_name = ?", (exercise_name,))
        if not result:
            raise ValueError(f"Exercise '{exercise_name}' not found in database.")
        return self.cursor.fetchone()[0]

    def logExercise(self, exercise_name, sets, reps, weight, user_id=None):
        # need to check that the info given is valid
        if user_id is None:
            user_id = self.user_id
        if not isinstance(exercise_name, str) or not exercise_name.strip():
            raise ValueError("Exercise name must be a non-empty string.")
        if not isinstance(sets, int) or sets <= 0:
            raise ValueError("Sets must be a positive integer.")
        if not isinstance(reps, int) or reps <= 0:
            raise ValueError("Reps must be a positive integer.")
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Weight must be a non-negative number.")
        
        last_session_id = self.getAllSessionsByUserId(user_id)[0][0]
        if last_session_id is None:
            raise ValueError("no session found for given user")
        exercise_name_id = self.getExerciseNameIdFromName(exercise_name.upper())
        self.cursor.execute("INSERT INTO exercise (session_id, exercise_name_id, sets, reps, weight) VALUES (?, ?, ?, ?, ?)", (last_session_id, exercise_name_id, sets, reps, weight))
        self.conn.commit()

    def logBodyweight(self, weight, user_id=None):
        if user_id is None:
            user_id = self.user_id
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number.")
        self.cursor.execute("INSERT INTO bodyweight (user_id, bodyweight) VALUES (?, ?)", (user_id, weight))
        self.conn.commit()

    def getBodyweightHistory(self, user_id=None):
        if user_id is None:
            user_id = self.user_id
        # bodyweight, bodyweight_date
        self.cursor.execute("SELECT bodyweight, bodyweight_date FROM bodyweight WHERE user_id = ? ORDER BY bodyweight_date DESC", (user_id,))
        return self.cursor.fetchall()

    def getExerciseHistoryByName(self, exercise_name, user_id=None):
        if user_id is None:
            user_id = self.user_id
        exercise_name_id = self.getExerciseNameIdFromName(exercise_name.upper())
        # session_id, exercise_name_id, sets, reps, weight
        self.cursor.execute("SELECT exercise_name_id, sets, reps, weight FROM exercise WHERE exercise_name_id = ? AND session_id IN (SELECT session_id FROM sessions WHERE user_id = ?) ORDER BY session_id DESC", (exercise_name_id, user_id))
        return self.cursor.fetchall()







def tests():
    # running tests
    db = Database_()
    db.createDatabase()
    db.createUser("test_user", "test_password", "test_email")

    db.cursor.execute("INSERT INTO sessions (user_id, session_date) VALUES (?, ?)", (2, datetime.now()))
    db.removeUser("test_user")

    db.cursor.execute("INSERT INTO bodyweight (user_id, bodyweight) VALUES (?, ?)", (1, 80))
    db.cursor.execute("INSERT INTO exercise_names (exercise_name, category) VALUES (?, ?)", ("bench", "workout A"))
    db.cursor.execute("INSERT INTO sessions (user_id, session_date) VALUES (?, ?)", (1, datetime.now()))
    db.cursor.execute("INSERT INTO exercise (session_id, exercise_name_id, sets, reps, weight) VALUES (?, ?, ?, ?, ?)", (1, 1, 3, 10, 80))
    #
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
