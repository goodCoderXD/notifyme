# Notify Me

Sometimes I'll run a long command on a remote machine.
I want to be notified when the command finishes.
This simple script does that. It opens a rest API on your
local machine and then when it's hit, it'll notify you.

Windows 10 machine only.

Local machine:
```ps1
pip install -r requirements.txt
python3 .\notifyme.py # will print ip
```

Remote machine:
```sh
curl "<remote ip>:5000/notify?message=<message>"
```

