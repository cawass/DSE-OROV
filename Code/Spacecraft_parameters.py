import tkinter as tk

class Engine_Caracteristics:
    def __init__(self, thrust, power, mass, ISP, efficiency):
        self.thrust = thrust
        self.power = power
        self.mass = mass
        self.ISP = ISP
        self.efficiency = efficiency

class Solar_Panel_Parameters:
    def __init__(self, mass, power, area, efficiency):
        self.mass = mass
        self.area = area
        self.efficiency = efficiency
    def power_generation(self, solar_flux):
        return solar_flux * self.area * self.efficiency

class Battery_Parameters:
    def __init__(self, mass, discharge_power, capacity, charge_power):
        self.mass = mass
        self.discharge_power = discharge_power
        self.capacity = capacity
        self.charge_power = charge_power

class Fuel_Parameters:
    def __init__(self, mass):
        self.mass = mass

class Electric_system_Parameters:
    def __init__(self, mass, efficiency):
        self.mass = mass
        self.efficiency = efficiency

class Spacecraft_Bus:
    def __init__(self, mass):
        self.mass = mass

class Spacecraft:
    def __init__(self, Engine, Solar_Panel, Battery, Fuel, Electric_system, Spacecraft_Bus):
        self.mass = Engine.mass + Solar_Panel.mass + Battery.mass + Fuel.mass + Electric_system.mass + Spacecraft_Bus.mass
        self.power_propulsive = Engine.power
        self.solar_power = Solar_Panel.power_generation(1350)
        self.battery_power = Battery.discharge_power
        self.battery_capacity = Battery.capacity
        self.efficiency = Engine.efficiency*Electric_system.efficiency
        self.battery_energy = Battery.capacity * 3600  # Assuming capacity is in Ah and converting to Joules
        self.fuel_mass = Fuel.mass

    def charge_battery(self, power, time):
        self.battery_energy += power * time

    def discharge_battery(self, power, time):
        self.battery_energy -= power * time

    def use_fuel(self, fuel_amount):
        self.fuel_mass -= fuel_amount

class SpacecraftUI:
    def __init__(self, spacecraft):
        self.spacecraft = spacecraft
        self.root = tk.Tk()
        self.root.title("Spacecraft Control Panel")

        self.battery_label = tk.Label(self.root, text=f"Battery Energy: {self.spacecraft.battery_energy} J")
        self.battery_label.pack()

        self.fuel_label = tk.Label(self.root, text=f"Fuel Mass: {self.spacecraft.fuel_mass} kg")
        self.fuel_label.pack()

        self.power_usage_label = tk.Label(self.root, text="Power Usage: 0 W")
        self.power_usage_label.pack()

        self.charge_button = tk.Button(self.root, text="Charge Battery", command=self.charge_battery)
        self.charge_button.pack()

        self.discharge_button = tk.Button(self.root, text="Discharge Battery", command=self.discharge_battery)
        self.discharge_button.pack()

        self.use_fuel_button = tk.Button(self.root, text="Use Fuel", command=self.use_fuel)
        self.use_fuel_button.pack()

        self.update_ui()

    def charge_battery(self):
        power = 100  # Example power value
        time = 1  # Example time value
        self.spacecraft.charge_battery(power, time)
        self.update_ui()

    def discharge_battery(self):
        power = 100  # Example power value
        time = 1  # Example time value
        self.spacecraft.discharge_battery(power, time)
        self.update_ui()

    def use_fuel(self):
        fuel_amount = 1  # Example fuel amount
        self.spacecraft.use_fuel(fuel_amount)
        self.update_ui()

    def update_ui(self):
        self.battery_label.config(text=f"Battery Energy: {self.spacecraft.battery_energy} J")
        self.fuel_label.config(text=f"Fuel Mass: {self.spacecraft.fuel_mass} kg")
        self.power_usage_label.config(text="Power Usage: 0 W")  # Update with actual power usage if needed

    def run(self):
        self.root.mainloop()

# Example usage
Engine_1 = Engine_Caracteristics(0.1, 1000, 10, 100, 0.7)
Solar_Panel_1 = Solar_Panel_Parameters(10, 10, 100, 0.2)
Battery_1 = Battery_Parameters(20, 2000, 10**7, 1000)
Fuel_1 = Fuel_Parameters(100)
Electric_system_1 = Electric_system_Parameters(10, 0.8)
Spacecraft_Bus_1 = Spacecraft_Bus(100)

spacecraft = Spacecraft(Engine_1, Solar_Panel_1, Battery_1, Fuel_1, Electric_system_1, Spacecraft_Bus_1)
ui = SpacecraftUI(spacecraft)
ui.run()