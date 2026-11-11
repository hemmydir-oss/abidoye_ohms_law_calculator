# Ohm's Law and Power Calculator
# Author: ABIDOYE EMMANUEL TAIWO
#
# Ohm's Law:  V = I x R   (voltage = current x resistance)
# Power:      P = V x I   (power = voltage x current)
#
# The user chooses what to find, enters the two known values,
# and gets the answer with units. The program repeats until the user quits.
#
# My own twist: answers are shown with automatic unit prefixes.
# For example 0.00255 A is shown as 2.55 mA, and 4800 ohm is shown as
# 4.8 kohm. After every power calculation, the program also checks the
# power against the standard resistor ratings (0.25 W, 0.5 W, 1 W, 2 W).

UNITS = {"voltage": "V", "current": "A", "resistance": "ohm", "power": "W"}

# Standard resistor power ratings in watts, from smallest to largest
STANDARD_RATINGS = [0.25, 0.5, 1, 2]

# SI prefixes from largest to smallest: (size of prefix, symbol)
PREFIXES = [
    (1e6, "M"),   # mega  = million
    (1e3, "k"),   # kilo  = thousand
    (1, ""),      # no prefix
    (1e-3, "m"),  # milli = thousandth
    (1e-6, "u"),  # micro = millionth (written as u, which is easy to type)
    (1e-9, "n"),  # nano  = billionth
]

history = []  # each finished calculation is stored here as a line of text


def ask_number(prompt, rule="any"):
    """Keep asking until the user types a valid number.
    rule = 'any'      accepts any number
    rule = 'nonzero'  rejects 0 (used when we divide by the value)
    rule = 'positive' accepts only numbers above 0 (used for resistance)
    """
    while True:
        text = input(prompt).strip()

        # Check that the input is a number at all
        try:
            value = float(text)
        except ValueError:
            print("  That is not a number. Try again, for example 12 or 0.5.")
            continue

        # Check the rule for this value
        if rule == "nonzero" and value == 0:
            print("  This value cannot be zero, because we divide by it. Try again.")
        elif rule == "positive" and value <= 0:
            print("  Resistance must be greater than zero. Try again.")
        else:
            return value


def format_with_prefix(value, unit):
    """Show a number with the prefix that keeps it between 1 and 1000.
    Example: 0.00255 with unit 'A' becomes '2.55 mA'."""
    if value == 0:
        return f"0 {unit}"

    size = abs(value)
    for prefix_size, symbol in PREFIXES:
        # Use the first (largest) prefix that fits the number
        if size >= prefix_size:
            return f"{value / prefix_size:.3g} {symbol}{unit}"

    # Very tiny numbers: use the smallest prefix we have
    smallest_size, smallest_symbol = PREFIXES[-1]
    return f"{value / smallest_size:.3g} {smallest_symbol}{unit}"


def calculate(choice):
    """Ask for the two known values needed for the chosen quantity.
    Returns the name of the answer and its value."""
    if choice == "1":  # find voltage: V = I x R
        current = ask_number("Enter current in amps (A): ")
        resistance = ask_number("Enter resistance in ohms: ", rule="positive")
        return "voltage", current * resistance

    elif choice == "2":  # find current: I = V / R
        voltage = ask_number("Enter voltage in volts (V): ")
        resistance = ask_number("Enter resistance in ohms: ", rule="positive")
        return "current", voltage / resistance

    elif choice == "3":  # find resistance: R = V / I
        voltage = ask_number("Enter voltage in volts (V): ")
        current = ask_number("Enter current in amps (A): ", rule="nonzero")
        return "resistance", voltage / current

    else:  # choice "4": find power: P = V x I
        voltage = ask_number("Enter voltage in volts (V): ")
        current = ask_number("Enter current in amps (A): ")
        return "power", voltage * current


def check_resistor_rating(power):
    """Compare the power with the standard resistor ratings and
    return a message telling the user which rating to use."""
    watts = abs(power)  # a resistor's rating depends on the size of the power
    for rating in STANDARD_RATINGS:  # check from smallest to largest
        if watts <= rating:
            return f"Use at least a {rating} W resistor."
    # Power is bigger than the largest rating in the list
    return (f"Warning: {format_with_prefix(watts, 'W')} is above the largest "
            f"standard rating ({STANDARD_RATINGS[-1]} W). "
            f"Use a higher-rated resistor or check the circuit.")


def show_history():
    """Print every calculation saved so far."""
    print("\n--- Calculation history ---")
    if not history:
        print("  No calculations yet.")
    for number, line in enumerate(history, start=1):
        print(f"  {number}. {line}")
    print()


def main():
    print("=== Ohm's Law and Power Calculator ===")

    while True:
        print("\nWhat do you want to find?")
        print("  1. Voltage (V)")
        print("  2. Current (A)")
        print("  3. Resistance (ohm)")
        print("  4. Power (W)")
        print("  h. Show history")
        print("  q. Quit")
        choice = input("Choose an option: ").strip().lower()

        # Decide what to do based on the menu choice
        if choice in ("1", "2", "3", "4"):
            name, value = calculate(choice)
            line = f"{name.capitalize()} = {format_with_prefix(value, UNITS[name])}"
            print(f"\nAnswer: {line}")
            history.append(line)

            # Check power against the standard resistor ratings
            if name == "power":
                print(check_resistor_rating(value))
        elif choice == "h":
            show_history()
        elif choice == "q":
            print("\nGoodbye.")
            show_history()
            break
        else:
            print("  Please choose 1, 2, 3, 4, h or q.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped. Goodbye.")
