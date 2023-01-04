# Simple Raspberry Pi Robot
Basic 2 wheel robot with web UI controls, using the [simple rasberry pi robot](https://learn.adafruit.com/simple-raspberry-pi-robot/). This requires installation of the [MotorKit Library](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software). This is based on Python 2, which is outdated and should be updated to Python 3, including the `Robot.pyc` file.

## Running
To start the embedded webapp
```bash
python web-buggy.py
```

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