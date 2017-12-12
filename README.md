# OVH-API for proxy of API request to OVH

# Info
This project uses Fython virtualenv together with various Python Flask modules. See below for installation instructions.

# TL;DR
* Install virtualenv
  * pip install virtualenv
  * virtualenv flask
  * source flask/bin/activate
  * pip install -r requirements.txt
* copy config.py.example to config.py and modify to your liking.
* modify the rest of the code
* run ./run-dev.sh in another terminal/screen/tmux and look at your debug output
* ...
* profit!(?)

# Installation for "production"
* Modify systemd/gunicorn.service and copy it to /etc/systemd/system/gunicorn.service
* copy systemd/gunicorn.socket to /etc/systemd/system/gunicorn.socket
* Modify systemd/gunicorn.conf and copy it to /etc/tmpfiles.d/gunicorn.conf and run ```systemd-tmpfiles --create```
* Run ```systemctl daemon-reload``` and ```systemctl enable gunicorn.service``` and ```systemctl start gunicorn``` to get it running.
* Create a nginx config with "proxy_pass http://unix:/run/gunicorn/socket;".
