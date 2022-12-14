"""
Ragul
CP1404 Practical8
SilverServiceTaxi class, derived from Taxi
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness, price_per_km):
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(),
                                                    self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()