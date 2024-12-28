
class Spacecraft_Caracteristics:
    def __init__(self, mass, power):
        self.mass = mass
        self.power = power

class Engine_Caracteristics:
    def __init__(self, thrust, power, mass, ISP):
        self.thrust = thrust
        self.power = power
        self.mass = mass
        self.ISP = ISP

class Solar_Panel_Parameters:
    def __init__(self, mass, power, area, efficiency):
        self.mass = mass
        self.area = area
        self.efficiency = efficiency

class Battery_Parameters:
    def __init__(self, mass, discharge_power, capacity):
        self.mass = mass
        self.discharge_power = discharge_power
        self.capacity = capacity


OROV_1 = Spacecraft_Caracteristics(1000, 100, 10)
Mission_1 = Engine_Caracteristics(100, 10)