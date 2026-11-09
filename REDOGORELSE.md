# Redogörelse  

# 1. Three constructs

# While loop

In my MAIN.py I used while loop to wrap the entire menu list is because a while loop allow us to keep running and asking the user until some condition is true or false, in that case the user has to type 8 (exit) for this to break.

# If/else

We used if else in almost all the files but some example is to attach each user input with code logic, to check the input validation and perform the logic, all 3 used if and else.

# Function with parameter and return

ShowAlllenv takes path as argument to see and return all the env names. The reason it returns instead of printing is because we want some other object to use it in their logic instead of printing to terminal.

## 2. Why a list of dictionaries?

A dict allows us to call each key by name and associate value with them. We have a list also so we can have multiple elements stored in a single object. Each value in the dict is saved as string.


## 3. Why JSON for storage but CSV for the report?

JSON is convenient and matches the style for my program's memory, and CSV is good for people because it can be used in spreadsheets.

# 4. Modules and functions

We have `MAIN.py`, `meny.py`, `kontroller.py` and `CSVwritter.py`. Menu holds the menu list and other functions when each choice is selected. Kontroller handles the ping of all the servers and returns a return code and updates the source file by up and down and time on last updated, and CSV is responsible for writing the source file to the CSV format in a different folder Reports with time format. And MAIN.py is where we bring all of them together and connect them.

`main()`: I wrapped the MAIN.py's majority of the code inside the `main()` so that the code doesn't run automatically when imported by other file, instead only run when its name = main.

## 5. Standard library modules

I used many standard libraries and some of them are `json`, `csv`, `subprocess`, `argparse`, `os` and `datetime`.

**json** – to turn JSON data to Python object or Python object to JSON data by `json.dumps`.

**csv** – similar to json, we turn Python object to CSV and CSV to Python object.

**subprocess** – to run command from Python code, for example ping.

**argparse** – it's used so we can take user CLI arguments and add logic and functionality to it. It is better than raw `sys.argv[index]` because I can attach --flags and rules with the arguments.

**os** – this helps us to interact with operating system, for example to check if certain file exists or to remove or create file and folder.

**datetime** – to get real time and format them.

## 6. Three examples of good practice

**Environment variable (`MAIN.py`, `main()`):** So we can have different name of file so it is not just one hardcoded.

**.gitignore:** So it ignores the rough files like .csv, report or other files that don't need to be in my repo when someone else is running the code.

I pass ping as a list, `["ping", "-c", "1", hostname]`. Then no shell is used, so a strange address can't run as a command. The exit code decides if the server is up or down.


## 7. Sources and tools

I used YouTube – Corey Schafer (Python playlists), Bro Code – and Claude to explain and guide me to understand the project requirement and check things and genarate Detailed README.md file.