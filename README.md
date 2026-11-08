# Server Inventory Tool

A small command-line tool for keeping track of servers: what they are called, where they live, which environment they belong to, and whether they answer on the network.

I built it as the final assignment in the Python course. The idea is the kind of tool a DevOps team writes for itself when a big monitoring system is overkill: a list of servers in a JSON file, a way to ping them, and a CSV report you can hand to someone else.

You can use it in two ways:

- **Menu mode** - start it without arguments and pick options from a text menu.
- **CLI mode** - pass a flag, the program does one thing and exits. This is the mode you would use in a bash script or a CI/CD pipeline.

Both modes call the same functions underneath, so a server checked from the menu is checked exactly the same way as one checked from the command line.

## What it can do

- List all servers, or only the ones in one environment (`dev`, `test`, `prod`)
- Add a server (the environment is validated, and duplicate names are refused)
- Remove a server (removing a `prod` server asks for an extra confirmation)
- Check one server or all servers with `ping`
- Save the result (`up` / `down`) and the time of the check
- Export everything to a CSV report

Every change is saved to the JSON file right away, so nothing is lost if the program is closed in the middle of something.

No external packages are needed. Everything comes from the standard library.

## Menu mode

You get this menu, and it keeps coming back until you pick 8:

```
--- Server Inventory Tool ---
1. Show all servers
2. Show servers in an environment
3. Add a server
4. Remove a server
5. Check a server
6. Check all servers
7. Export report as CSV
8. Exit
```

## CLI mode

| Command | What it does |
|---|---|
| `python3 MAIN.py --help` | Shows all flags with a short description |
| `python3 MAIN.py --list` | Prints all servers |
| `python3 MAIN.py --list --env prod` | Prints only servers in prod |
| `python3 MAIN.py --controll web01` | Pings web01 and saves the result |
| `python3 MAIN.py --controll-all` | Pings every server and saves the results |
| `python3 MAIN.py --export` | Writes a CSV report to `reports/` |

## Choosing the data file

By default the program reads and writes `server.json` in the project folder.

To use another file, set the environment variable `INVENTORY_DATAFILE = YOURFILE`

## Project structure

```
Server_status_Tool/
├── MAIN.py          entry point - reads the arguments and picks menu or CLI mode
├── meny.py          the text menu and the functions that print servers
├── storage.py       loads and saves the JSON file
├── kontroller.py    pings servers and updates their status
├── CSVwritter.py    writes the CSV report
├── server.json      the server data
├── .gitignore
├── README.md
└── REDOGORELSE.md   written explanation of the code
```
