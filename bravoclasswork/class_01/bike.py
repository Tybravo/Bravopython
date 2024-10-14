
class Bike:

    def __init__(self):
        self.is_on:bool = False
        self.speed = 0
        self.gear = 0


    def turn_on(self):
        self.is_on = True
        self.speed = 0
        self.gear = 0

    def turn_off(self):
        self.is_on = False
        self.speed = 0
        self.gear = 0

    def get_status(self):
        return self.is_on

    def change_gear_one(self, gear):
     if self.speed > 0 and self.speed < 20:
         self.gear = 1

    def get_bike_on_gear_accel_1_by_1(self, gear, speed):
        if gear == 1:
            if speed >= 0 and speed <= 20:
                speed  = speed + 1
                return speed

            if speed > 20:
                self.gear = 2
                return speed

    def get_bike_on_gear_accel_2_by_2(self, gear, speed):
        if gear == 2:
            if speed >= 21 and speed <= 30:
                speed = speed + 2
                return speed

            if speed > 30:
                self.gear = 3
                return speed

    def get_bike_on_gear_accel_3_by_3(self, gear, speed):
        if gear == 3:
            if speed >= 31 and speed <= 40:
                speed = speed + 3
                return speed

            if speed > 40:
                self.gear = 4
                return speed

    def get_bike_on_gear_accel_4_by_4(self, gear, speed):
        if gear == 4:
            if speed >= 41 and speed <= 50:
                speed = speed + 4
                return speed

            if speed == 50:
                self.gear = 4
                return speed

    def get_bike_on_gear_decel_1_by_1(self, gear, speed):
        if gear == 1:
            if speed >= 0 and speed <= 20:
                speed = speed - 1
                return speed

            if speed < 20:
                self.gear = 1
                return speed

    def get_bike_on_gear_decel_2_by_2(self, gear, speed):
        if gear == 2:
            if speed >= 21 and speed <= 30:
                speed = speed - 2
                return speed

            if speed < 20:
                self.gear = 1
                return speed

    def get_bike_on_gear_decel_3_by_3(self, gear, speed):
        if gear == 3:
            if speed >= 31 and speed <= 40:
                speed = speed - 3
                return speed

            if speed < 30:
                self.gear = 2
                return speed

    def get_bike_on_gear_decel_4_by_4(self, gear, speed):
        if gear == 4:
            if 41 <= speed <= 50:
                speed = speed - 4
                return speed

            if speed < 40:
                self.gear = 3












