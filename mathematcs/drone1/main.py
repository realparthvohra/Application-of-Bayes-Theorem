import math as math
class Drone:
    def __init__(self , id , model , battery_life , coordinates=(0,0,0)):
        self.id = id
        self.model = model
        self.battery_life = battery_life
        self.flying = False
        self.coordinates = coordinates
        self.x ,self.y , self.z = self.coordinates
        
    def take_off(self,height):
        if not self.flying:
            self.flying = True
            # Code to set the drone's altitude to height
            print(f"Drone {self.id} taking off to height {height} meters.")
            self.coordinates = (self.coordinates[0], height, self.coordinates[2])
        else:
            print(f"Drone {self.id} is already flying.")

    def down(self):
        if self.flying:
            self.flying = False
            # Code to set the drone's altitude to 0
            print(f"Drone {self.id} landing.")
            self.coordinates = (self.coordinates[0], 0, self.coordinates[2])
        else:
            print(f"Drone {self.id} is already on the ground.")

    def predict_point(self,angle):
        if self.flying:
            if angle <= 0 or angle > 180:
                print("Angle must be between 1 and 180 degrees.")
                return None
            
            cos_value = math.cos(math.radians(angle))
            height = self.coordinates[1]
            distance = height / cos_value
            print(f"Drone {self.id} can reach a point at distance {distance:.2f} meters at angle {angle} degrees.")
            return distance
        else:
            print("Drone must be flying to predict point.")