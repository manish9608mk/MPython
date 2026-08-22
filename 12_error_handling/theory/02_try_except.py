# We also practiced many examples involving conditions and loops,
# including examples related to file handling.


def check_leap_year():
    try:
        year = int(input("Enter year: "))

        if year <= 0:
            print("Enter a valid year.")
            return

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print(f"Yes, {year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

    except ValueError:
        print("Please enter numbers only.")


check_leap_year()


'''
TRY / EXCEPT — SIMPLE MENTAL MODEL

try
 ↓
Run code that may cause an error.

except
 ↓
Catch and handle the expected error.

if / elif / else
 ↓
Handle normal program logic and conditions.

return
 ↓
Stop the current function and go back to the caller.


Example:

User enters "abc"
      ↓
int("abc")
      ↓
ValueError
      ↓
except ValueError
      ↓
"Please enter numbers only."


User enters -10
      ↓
No exception
      ↓
if year <= 0
      ↓
return
      ↓
Function stops.


User enters 2024
      ↓
No exception
      ↓
Leap-year condition
      ↓
Print result.


IMPORTANT:

Exception handling → handles unexpected/runtime errors.

Conditions → handle normal program logic.

return → exits the current function.

exit() → terminates the entire Python program;
          usually not needed inside functions.

INTERVIEW TIP:

Catch specific exceptions whenever possible.

Good:
    except ValueError:

Avoid:
    except:
        ...

because a bare except can hide unexpected errors.
'''