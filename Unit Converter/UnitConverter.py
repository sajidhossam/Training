def mm_to_cm(mm):
    return mm / 10

def cm_to_mm(cm):
    return cm * 10

def mm_to_m(mm):
    return mm / 1000

def m_to_mm(m):
    return m * 1000

def cm_to_m(cm):
    return cm / 100

def m_to_cm(m):
    return m * 100

def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

def convert_units():
    print("Welcome to Metric Unit Converter!!")
    print("1. Millimeters to Centimeters")
    print("2. Centimeters to Millimeters")
    print("3. Millimeters to Meters")
    print("4. Meters to Millimeters")
    print("5. Centimeters to Meters")
    print("6. Meters to Centimeters")
    print("7. Kilometers to Meters")
    print("8. Meters to Kilometers")

    choice = int(input("choose the conversion (1/2/3/4/5/6/7/8):\n"))

    if choice == 1:
        mm  = float(input("Enter the value in millimeters: "))
        print(f"{mm} Millimeters is equal to {mm_to_cm(mm)} centimeters")

    elif choice == 2:
        cm = float(input("Enter the value in centimeters: "))
        print(f"{cm} centimeters is equal to {cm_to_m(cm)} millimeters")

    elif choice == 3:
        mm = float(input("Enter the value in millimeter: "))
        print(f"{mm} millimeter is equal to {mm_to_m(mm)} centimeters")

    elif choice == 4:
        m = float(input("Enter the value in meters: "))
        print(f"{m} Meters is equal to {m_to_mm(m)} millimeter")

    elif choice == 5:
        cm = float(input("Enter the value in cm: "))
        print(f"{cm} centimeters is equal to {cm_to_m(cm)} Meters")

    elif choice == 6:
        m = float(input("Enter the value in Meters: "))
        print(f"{m}Meters is equal to {m_to_cm(m)} Centimeters")

    elif choice == 7:
        km = float(input("Enter the value in killometer: "))
        print(f"{km} Killometers is equal to {km_to_m(km)} Meters")

    elif choice == 8:
        m = float(input("Enter the value in Meters: "))
        print(f"{m}Meters is equal to {m_to_km(m)} killometers")

    else:
        print("Invalid choice")
convert_units()





