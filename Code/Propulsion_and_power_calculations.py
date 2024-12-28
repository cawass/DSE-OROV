import numpy as np

def power_requirement(mass, delta_v, delta_t):
    """
    Calculate the power requirement to perform a change in velocity (Δv) of a spacecraft in a specific amount of time (Δt).
    
    Parameters:
    mass (float): Mass of the spacecraft in kilograms.
    delta_v (float): Change in velocity in meters per second.
    delta_t (float): Time over which the change in velocity occurs in seconds.
    
    Returns:
    float: Power requirement in watts.
    """
    # Calculate the required acceleration
    acceleration = delta_v / delta_t
    
    # Calculate the force needed to achieve that acceleration
    force = mass * acceleration
    
    # Calculate the power required to produce that force
    power = force * delta_v
    
    return power

        
  
# Example usage
Successful_mission = False
Failed_mission = False
while Successful_mission == False or Failed_mission == False:
    power = power_requirement(mass, delta_v, delta_t)
print(f"Power Requirement: {power} W")
