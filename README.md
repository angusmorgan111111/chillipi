# chillipi

## System dependencies

Install with `apt-get install`:

 * python3
 * pip3
 * nginx

## Pip dependencies

Install with `pip3 install`:

 * flask
 * Flask-APScheduler
 * gunicorn

## Setup

 * Configure nginx as a proxy for chillipi to port 8000

 * Set up SSL certificate management with Let's Encrypt

 * Create a systemd unit file and enable it on startup
   * (chillipi is started with `gunicorn3 chillipi:app`)

 * Allow non-root access to hardware peripherals

## Usage

As root: `systemctl [start|restart|stop] chillipi`

## Development

Mount the chillipi directory using Samba - all files then stay local to the pi.

chillipi must be restarted to pick up new changes to files.

### Visual Studio Code

VS Code is a decent editor to use for Python.

Set it up as follows:

 * Open the chillipi directory in VS Code
 * Open `chillipi.py`
 * Intall the python plugin when prompted, then restart VS Code
 * Press Ctrl+Shift+P, type "interpreter", then select the Python 3 interpreter
 * Install the pylint plugin when prompted
