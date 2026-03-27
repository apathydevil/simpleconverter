import conversions

def main():
    print("Welcome to the unit converter!")
    while True:
        print("\nPlease select a conversion type:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("0. Exit")
        
        choice = input("\nEnter the number of your choice: ")
        
        if choice == "1":
            print("Units: meter, kilometer, centimeter, millimeter, inch, foot, yard, mile")
            from_unit = input("Convert from: ").lower()
            to_unit = input("Convert to: ").lower()
            value = float(input("Enter value: "))
            result = conversions.convert_length(value, from_unit, to_unit)
            print("\n")
            print(f"{value} {from_unit} = {result:.4f} {to_unit}")
        elif choice == "2":
            print("Units: gram, kilogram, milligram, ton, pound, ounce")
            from_unit = input("Convert from: ").lower()
            to_unit = input("Convert to: ").lower()
            value = float(input("Enter value: "))
            result = conversions.convert_weight(value, from_unit, to_unit)
            print("\n")
            print(f"{value} {from_unit} = {result:.4f} {to_unit}")
        elif choice == "3":
            print("Units: Celsius, Fahrenheit, Kelvin")
            from_unit = input("Convert from: ").lower()
            to_unit = input("Convert to: ").lower()
            value = float(input("Enter value: "))
            result = conversions.convert_temperature(value, from_unit, to_unit)
            print("\n")
            print(f"{value} {from_unit} = {result:.4f} {to_unit}")
        elif choice == "0":
            print("\nExiting the converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()