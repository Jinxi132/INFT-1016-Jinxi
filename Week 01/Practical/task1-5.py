# Task1
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

total_letters = 0

for day in days:
    total_letters += len(day)

average = total_letters / len(days)
print("Average word length:", average)

# Task2
def distance(speed, time):
    return speed * time

result = distance(60, 100)
print("Distance:", result)

# Task3
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

energy = kinetic_energy(10, 60)
print("Kinetic Energy:", energy)

# Task4
class MovingObject:

    def __init__(self, velocity, mass):
        self.velocity = velocity
        self.mass = mass

    def distance(self, duration):
        return self.velocity * duration

    def kinetic_energy(self):
        return 0.5 * self.mass * self.velocity ** 2
    
# Task5
myMovingObject = MovingObject(6, 20)

print("OOP Distance:", myMovingObject.distance(60))
print("OOP Kinetic Energy:", myMovingObject.kinetic_energy())