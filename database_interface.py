from abc import ABC, abstractmethod

# feel free to change anything here that affects you're task. This is just to get started.
# note the implementation of these methods is to be done by the database people,
# so any processing of data should be done before calling them - these methods are just for storing the data.
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