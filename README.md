# Server Inventory Tool

A small Python tool for keeping track of servers: their name, address, environment (dev, test or prod), role, and whether they respond on the network.

The server list is saved in a JSON file (`servrar.json`), servers are checked with `ping`, and a report can be exported as a CSV file that opens in any spreadsheet program.

## What it can do

- Show all servers in a table, or only the servers in one environment
- Add a new server (the name can not be empty, the environment is checked, and duplicate names are not allowed)
- Remove a server (production servers ask for an extra confirmation)
- Check whether one server or all servers respond to ping
- Save the result (`up` or `down`) and the time of the check
- Export all servers to a CSV report with the date and time in the file name

All changes are saved right away, so nothing is lost when the program is closed.

## Requirements

- Python 3.12 or newer (the code uses f-strings with nested quotes, which need 3.12)
- Linux or macOS, because the check uses the `ping` command. On Windows, use WSL or a Linux container.
- No extra packages. Everything comes from the Python standard library.

Some networks block ping. A server shown as `down` may be blocked by the network rather than switched off.

## How to start the program

Clone the repository and go into the folder:

```bash
git clone https://github.com/daud-rh-cloud/Server_status_Tool.git
cd Server_status_Tool
```

Start the menu:

```bash
python3 main.py
```

Or run a single command (see below), for example:

```bash
python3 main.py --list
```

## Menu mode

Start the program without any arguments and a numbered menu appears:

```
--- Server Inventory Tool ---
1. Show all servers
2. Show servers in an environment
3. Add a server
4. Remove a server
5. control a server
6. control all servers
7. Export report as CSV
8. Exit
```

Pick an option by typing its number. The menu comes back after every choice until you choose `8`. An invalid choice prints a message and shows the menu again.

## Command-line mode

Start the program with an option. It does that one job and then exits. Every option has an English and a Swedish name, and both do the same thing.

| Command | Swedish name | What it does |
|---|---|---|
| `python3 main.py --list` | `--lista` | Shows all servers |
| `python3 main.py --list --env prod` | `--miljo` | Shows only the servers in one environment |
| `python3 main.py --controll web01` | `--kontrollera` | Pings one server by name and saves the result |
| `python3 main.py --controll-all` | `--kontrollera-alla` | Pings all servers and saves the results |
| `python3 main.py --export` | | Exports all servers to a CSV report |
| `python3 main.py --help` | | Shows all options |

The values allowed after `--env` are the environments that exist in the data file.

## Exit codes

In command-line mode the program ends with an exit code that scripts can read:

- `0` means everything went fine
- `1` means a checked server is down, or the requested server does not exist

Check the exit code right after a command:

```bash
python3 main.py --controll web01
echo $?
```

The check functions in `controller.py` only *return* the code. `main.py` decides when to exit, so in menu mode the program keeps running after a check.

## Data file and the environment variable

By default the servers are stored in `servrar.json` in the project folder. Each server is a dictionary with these keys:

```json
{
  "namn": "web01",
  "adress": "example.com",
  "miljo": "prod",
  "roll": "webserver",
  "status": "up",
  "senast_kontrollerad": "2026-11-09 11:37"
}
```

To use a different file, set the environment variable **`INVENTORY_DATAFIL`** before starting the program. The program reads it at startup. If it is not set, `servrar.json` is used.

Examples:

```bash
# for one command only
INVENTORY_DATAFIL=test_servrar.json python3 main.py --list

# for the whole terminal session
export INVENTORY_DATAFIL=/home/user/my_servers.json
python3 main.py
```

If the data file does not exist, the program creates it with an empty list instead of crashing.

## Reports

Reports are saved as CSV files in the `rapporter/` folder, which is created automatically if it is missing. The file name contains the date and time, for example `rapporter/inventering_2026-11-22_1000.csv`.

If the server list is empty, nothing is exported and a message is shown.

Reports are not stored in Git (see `.gitignore`).

## Files

| File | What it does |
|---|---|
| `main.py` | Entry point. Reads the environment variable and the command-line options, and runs either the menu loop or a single command. Decides the exit code. |
| `menu.py` | The text menu, plus the functions that show (as a table), add and remove servers. |
| `controller.py` | Checks servers with `ping` (`controll_all`, `controll_by_name`), saves `up`/`down` and the time, and returns an exit code. |
| `csv_writer.py` | Writes the server list to a CSV report in `rapporter/`. |
| `servrar.json` | The server data (a list of dictionaries). |
| `REDOGORELSE.md` | Written explanation of the code (redogörelse). |
| `.gitignore` | Keeps reports, CSV files, `__pycache__` and editor folders out of Git. |