from time import sleep


class Appliances:

    def __init__(self):
        self.bulb = "Electrical energy is converted into heat and light energy"
        self.fan = "Electrical energy is converted to mechanical energy"
        self.toaster = "Electrical energy is converted to thermal energy"
        self.cooker = "Electrical energy is converted to heat energy"
        self.blender = "Electrical energy is converted to mechanical energy"
        self.speaker = "Electrical energy is converted to sound energy"
        self.natural_gas = "Chemical energy is converted into thermal energy"



class LightBulb(Appliances):
    def  convert_energy(self):
        return self.bulb

class ElectricFan(Appliances):
    def convert_energy(self):
        return self.fan

class Toaster(Appliances):
    def convert_energy(self):
        return self.toaster

class Cooker(Appliances):
    def convert_energy(self):
        return self.cooker

class Blender(Appliances):
    def convert_energy(self):
        return self.blender


class Speaker(Appliances):
    def convert_energy(self):
        return self.speaker


class NaturalGas(Appliances):
    def convert_energy(self):
        return self.natural_gas
