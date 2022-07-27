# TTYSaver

Small script that reduces the brightness of the screen when no key is pressed, works on tty.

## Usage:
```bash
# install
sudo ln -s "$(pwd)/ttysaver.py" /bin/ttysaver
sudo ln -s "$(pwd)/ttysaver.service" /etc/systemd/system/ttysaver.service
sudo systemctl enable ttysaver
sudo systemctl start ttysaver
```