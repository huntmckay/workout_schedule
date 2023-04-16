class Exercise:
    def __init__(self, name, date):
        self.name = name
        self.date = date

class Lift(Exercise):
    def __init__(self, name, weight, reps, date):
        super().__init__(name, date)
        self.reps = reps
        self.weight = weight 

    def __str__(self):
        return f"Lift = {self.name} ({self.weight}lbs for {self.reps} reps, on {self.date})"

# # TODO define a new dataclass for different carido types
# class Cardio(Exercise):
#     def __init__(self, name, speed, time, distance):
#         self.time = time # needs better name timeperformed 
#         self.distance = distance # assert mile or km input
#         self.speed = speed(self.distance, self.time)
#     def __str__(self):
#         return f"{self.name}({self.distance},{self.time},{self.speed},{self.date})"
# 
#     def speed(distance,time):
#         return distance/time

bench = Lift("Bench Press", 150, 10, '20230416')
print(bench)

