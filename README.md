# Raspberry Pi Web Buggy
This project is a web based UI for remote control of a basic 2 wheel robot, using the [simple rasberry pi robot](https://learn.adafruit.com/simple-raspberry-pi-robot/). This requires installation of the [MotorKit Library](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software). This is based on Python 2, which is outdated and should be updated to Python 3, including the `Robot.pyc` file, which is not included in this repository.

This project is intended for academic learning purposes, to inspire young students, and for any purposes that Florida State College at Jacksonville deems appropriate.

![A screenshot of web UI](https://github.com/wltjr/cop4813/assets/12835340/0ac95e00-3ed6-47d1-8013-3784d7959d98)

## Running
To start the embedded webapp
```bash
python web-buggy.py
```
Note: This requires the `Robot.pyc` file to be located in the same folder as the `web-buggy.py` or other location that provides access to the library

## Web UI Controls
The web server runs locally on port 5000, using the Pi's DHCP assigned IP address.
Example `http://192.168.1.100:5000`


## Pi login credentials
username: pi

password:


## GUI
The GUI is not started by default to save power since its a headless device. To start, service x11-common needs to be unmasked, and then started.

```bash
# unmask
systemctl unmask x11-common
# start X11
systemctl start x11-common.service
# or
sudo service x11-common start
# or
sudo /etc/init.d/x11-common start
```