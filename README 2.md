# Ohm's Law and Power Calculator

## What it does
The program finds voltage, current, resistance or power from two known values. The user picks what to find, types the known values, and gets the answer with its unit. It keeps running until the user quits, and it rejects bad input such as letters or a zero divisor.

## How to run it
Install Python 3, then run: python ohms_law.py

## Sample output
```
=== Ohm's Law and Power Calculator ===

What do you want to find?
  1. Voltage (V)
  2. Current (A)
  3. Resistance (ohm)
  4. Power (W)
  h. Show history
  q. Quit
Choose an option: 4
Enter voltage in volts (V): 4
Enter current in amps (A): 0.2

Answer: Power = 800 mW
Use at least a 1 W resistor.

What do you want to find?
...
Choose an option: q

Goodbye.

--- Calculation history ---
  1. Power = 800 mW
```

## My own twist
Answers are shown with automatic unit prefixes, so the program picks the most readable size. For example, 0.00255 A is shown as 2.55 mA, 4700 ohm as 4.7 kohm, and 0.8 W as 800 mW. After every power calculation, the program also checks the power against the standard resistor ratings (0.25 W, 0.5 W, 1 W, 2 W) and tells the user the smallest safe rating to use.

## What I learned
Checking input before using it stops the program from crashing. Splitting the code into small functions made each part easier to test. Showing numbers with prefixes like m and k makes results easier to read, which matters in circuits where values range from micro-amps to kilo-ohms.

## Author
ABIDOYE EMMANUEL TAIWO, ND1 Mechatronics Engineering, YabaTech.
