# chillipi

## System dependencies

Install with `apt-get install`:

 * python3
 * pip3

## Pip dependencies

Install with `pip3 install`:

 * flask
 * Flask-APScheduler
 * python-dotenv

## Setup

 * Create a `chillipi` user

 * Allow the `chillipi` user access to the hardware peripherals

 * Clone this repository into `/opt/chillipi` and give the `chillipi` user full
   access to it

 * Copy `chillipi.service` into `/etc/systemd/system/`

 * Reload the systemd cache, start chillipi and enable it on startup

## Usage

As root: `systemctl [start|restart|stop] chillipi`

When chillipi is running it will be available on port 5000.

## Development

Mount the chillipi directory using Samba - all files then stay local to the pi.

chillipi will pick up code changes as they are made.

### Visual Studio Code

VS Code is a decent editor to use for Python.

Set it up as follows:

 * Open the chillipi directory in VS Code
 * Open `chillipi.py`
 * Intall the python plugin when prompted, then restart VS Code
 * Press Ctrl+Shift+P, type "interpreter", then select the Python 3 interpreter
 * Install the pylint plugin when prompted


## Reading log files

 journalctl -f in putty to look at log. This is writtent by util
