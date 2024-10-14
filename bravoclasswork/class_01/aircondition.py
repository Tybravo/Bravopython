
class AirCondition:

    def __init__(self):
        self.is_on: bool = False
        self.temperature = 0

    def turn_on(self):
        self.is_on = True
        self.temperature = 16

    def turn_off(self):
        self.is_on = False
        self.temperature = 0

    def get_bike_status(self):
        return self.is_on


    def get_temp_start_from_16(self, temperature):
        if self.is_on:
            return self.temperature

    def get_temp_increased(self,temperature):
        if self.is_on:
            if self.temperature >= 16 and self.temperature <= 30:
                self.temperature += 1
                return self.temperature

    def get_temp_decreased(self, temperature):
        if self.is_on:
            if self.temperature >= 17 and self.temperature <= 30:
                self.temperature -= 1
                return self.temperature

    def get_temp_maintain_30(self, temperature):
        if self.is_on:
            if temperature == 30:
                    return temperature

    def get_temp_maintain_16(self, temperature):
        if self.is_on:
            if temperature == 16:
                return temperature






