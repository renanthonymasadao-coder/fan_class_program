# test_fan.py, importing libraries to test fan class program

from fan import Fan

print("\n========== FAN CLASS TEST PROGRAM ==========\n")

# FIRST FAN OBJECT
fan1 = Fan()

fan1.set_speed(Fan.FAST)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)

# SECOND FAN OBJECT
fan2 = Fan()

fan2.set_speed(Fan.MEDIUM)
fan2.set_radius(5)
fan2.set_color("blue")
fan2.set_on(False)

# DISPLAY OUTPUTS
print("\nFIRST FAN OBJECT")
fan1.display_info()

print("\nSECOND FAN OBJECT")
fan2.display_info()

print("\n==========================================")
print("        END OF PROGRAM")
print("==========================================")