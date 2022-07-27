# TTYSaver

Small script that reduces the brightness of the screen when no key is pressed, works on tty.


## Config
- edit `DELAY` to set the idle time (in secconds)
- set `KBD_EVENT_FILE` to the event file coresponding to your keyboard

## Install
```bash
sudo ln -s "$(pwd)/ttysaver.py" /bin/ttysaver
sudo ln -s "$(pwd)/ttysaver.service" /etc/systemd/system/ttysaver.service
sudo systemctl enable ttysaver
sudo systemctl start ttysaver
```