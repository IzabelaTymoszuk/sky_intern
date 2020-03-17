class IllegalCarError(Exception):
    """Custom exception class for class Car"""

    def __init__(self, message):
        self.message = message


class Car:
    __person_avg = 70

    def __init__(self, pax_count, car_mass, gear_count):

        if pax_count < 1 or pax_count > 5:
            raise IllegalCarError('Pax count cannot be greater then 5, or less than 1')

        if car_mass > 2000:
            raise IllegalCarError('Car mass (excluding the passengers) cannot be greater than 2000 kg.')

        self.__pax_count = pax_count
        self.__car_mass = car_mass
        self.__gear_count = gear_count

    @property
    def gear_count(self):

        """Property to return gear count value."""

        return self.__gear_count

    @property
    def car_mass(self):

        """Property to return gear car mass."""

        return self.__car_mass

    @car_mass.setter
    def car_mass(self, value):

        """Validate setting value of car mass."""

        if value < 2001:
            self.__car_mass = value
        else:
            raise IllegalCarError('Car mass (excluding the passengers) cannot be greater than 2000 kg.')

    @property
    def pax_count(self):

        """Property to return number of passengers."""

        return self.__pax_count

    @pax_count.setter
    def pax_count(self, value):

        """Validate setting number of passengers."""

        if 0 < value < 6:
            self.__pax_count = value
        else:
            raise IllegalCarError('Pax count cannot be greater then 5, or less than 1')

    @property
    def total_mass(self):

        """Calculates the total mass of the vehicle."""

        return self.car_mass + (self.__person_avg * self.pax_count)

    def __str__(self):
        return f'Number of passengers: {self.pax_count}, Car mass: {self.car_mass}, Gear count: {self.gear_count}, ' \
            f'Total mass: {self.total_mass}'


c = Car(2, 1300, 4)
print(c)
c.pax_count = 6
print(c)