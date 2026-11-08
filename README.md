# Server Inventory Tool

A small Python tool for keeping track of servers: their name, address, environment (dev, test or prod), role, and whether they respond on the network.

The server list is saved in a JSON file, servers are checked with `ping`, and a report can be exported as a CSV file that opens in any spreadsheet program.

## What it can do

- Show all servers, or only the servers in one environment
- Add a new server (the environment is checked, and duplicate names are not allowed)
- Remove a server (production servers ask for an extra confirmation)
- Check whether one server or all servers respond to ping
- Save the result (up or down) and the time of the check
- Export all servers to a CSV report with the date and time in the file name

All changes are saved right away, so nothing is lost when the program is closed.

## Two ways to use it

**Menu mode:** start the program without any arguments. A numbered menu appears. Pick an option by typing its number. The menu keeps coming back until you choose to exit. Invalid choices give a message and the menu is shown again.

**Command-line mode:** start the program with an option. It does that one job and then exits. This mode is useful in scripts, scheduled jobs and CI/CD pipelines.

To see every available option and what it does, run the main file with `--help`.

Both modes use the same code underneath, so a task does exactly the same thing whichever mode you use.

## Exit codes

In command-line mode the program ends with an exit code that scripts can read:

- `0` means everything went fine
- `1` means a checked server is down, or the requested server does not exist

Check the exit code right after a command with `echo $?`.

## Requirements

- Python 3.12 or newer
- Linux or macOS (the check uses the `ping` command). On Windows, use WSL or a Linux container.
- No extra packages. Everything comes from the Python standard library.

Some networks block ping. A server shown as down may be blocked by the network rather than switched off.

## How to run it

1. Clone the repository.
2. Open a terminal in the project folder.
3. Run the main file with Python 3 to start menu mode, or add an option to use command-line mode.

## Data file

The servers are stored in a JSON file in the project folder. You can choose a different file by setting an environment variable before starting the program. The program reads the variable at startup, and if it is not set, the default file is used.

If the data file does not exist, the program starts with an empty server list instead of crashing.

## Reports

Reports are saved as CSV files in a reports folder, which is created automatically if it is missing. Each report has the date and time in its file name. Reports are not stored in Git.

## Project structure

The code is split into separate modules, each with one job:

- an entry point that reads the command-line options and starts the right mode
- a module for the text menu and showing, adding and removing servers
- a module that checks servers with ping
- a module that writes the CSV report
- a JSON file with the server data
- a written explanation of the code (redogörelse)