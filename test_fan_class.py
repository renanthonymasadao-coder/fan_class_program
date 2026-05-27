# test_fan.py, importing libraries to test fan class program

from fan import Fan

print("\n========== FAN CLASS TEST PROGRAM ==========\n")

# FIRST FAN OBJECT
fan1 = Fan()

fan1.set_speed(Fan.FAST)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)

