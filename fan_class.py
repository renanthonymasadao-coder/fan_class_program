#import libraries
class Fan:

    # Constants values
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        # Private Attributes (Encapsulation)
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
    