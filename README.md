# Simple Raspberry Pi Robot
Basic 2 wheel robot with web UI controls, using the [simple rasberry pi robot](https://learn.adafruit.com/simple-raspberry-pi-robot/).


## Pi
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