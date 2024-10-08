
class Bike:

    def __init__(self):
        self.is_on:bool = False
        self.speed = 0
        self.gear = 0
        self.accelerate = None

    def turn_on(self):
        self.is_on = True
        self.speed = 0
        self.gear = 0

    def turn_off(self):
        self.is_on = False
        self.speed = 0
        self.gear = 1

    def get_status(self):
        return self.is_on, self.speed, self.gear

    def get_bike_on_gear_1_by_1(self, gear, speed):
        if gear == 1:
            if speed >= 0 and speed <= 20:
                speed  = speed + 1
                return speed

            if speed > 20:
                self.gear = 2
                return speed
                # else:
                #     if gear < 1:
                #         return speed

    # def change_gear_one(self, gear):
    #     if self.gear == 1:
    #         return get_bike_on_gear_1_by_1
    #
    # # def increase(self, gear):
    # #     return self.speed






