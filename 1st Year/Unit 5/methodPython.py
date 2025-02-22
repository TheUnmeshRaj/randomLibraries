class Room:
   length = 0.0
   breadth = 0.0
   def calculate_area(self):
       print("Area of Room =", self.length * self.breadth)

study_room = Room()

study_room.length = 40
study_room.breadth = 30

print(study_room.calculate_area())