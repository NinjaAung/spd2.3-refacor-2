# By Kami Bigdely
# Remove assignment to method parameter.
class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value


class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


def calculate_kinetic_energy(mass, distance, time):
    adjusted_distance = distance
    adjusted_mass = mass
    if adjusted_distance.unit != 'km':
        # [ly] stands for light-year (measure of distance in astronomy)
        if adjusted_distance.unit == "ly":
            # convert from light-year to km unit
            in_km = adjusted_mass.value * 9.461e12
            adjusted_distance = Distance(in_km, "km")
        else:
            print("unit is Unknown")
            return
    speed = adjusted_distance.value/time  # [km per sec]
    if adjusted_mass.unit != 'kg':
        if adjusted_mass.unit == "solar-mass":
            # convert from solar mass to kg
            value = adjusted_mass.value * 1.98892e30  # [kg]
            adjusted_mass = Mass(value, 'kg')
        else:
            print("unit is Unknown")
            return

    kinetic_energy = 0.5 * adjusted_mass.value * speed ** 2
    return kinetic_energy


mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))
