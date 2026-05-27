#import libraries
class Fan:

    # Constant values
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        # Private Attributes (Encapsulation)
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # Setter Methods
    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_on(self, on):
        self.__on = on

   # Getter Methods
    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def is_on(self):
        return self.__on

    # Display Method
    def display_info(self):

        # ANSI COLORS
        RESET = "\033[0m"
        YELLOW = "\033[93m"
        BLUE = "\033[94m"
        GREEN = "\033[92m"
        RED = "\033[91m"

        # Dynamic Color
        text_color = RESET

        if self.__color.lower() == "yellow":
            text_color = YELLOW
        elif self.__color.lower() == "blue":
            text_color = BLUE

        status = f"{GREEN}ON{RESET}" if self.__on else f"{RED}OFF{RESET}"

        speed_text = {
            1: "SLOW",
            2: "MEDIUM",
            3: "FAST"
        }

        print(text_color + "=" * 45)
        print("              FAN DETAILS")
        print("=" * 45)
        print(f"Speed   : {speed_text[self.__speed]}")
        print(f"Radius  : {self.__radius}")
        print(f"Color   : {self.__color}")
        print(f"Status  : {status}")
        print("=" * 45 + RESET)