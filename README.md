python scripts used for remote boot of PC

to set up button_boot.py to run from startup, 
using terminal go to etc/ folder
sudo nano rc.local
add "python path/to/button_boot.py &" at bottom of file -> & makes script run as different process

to remote boot, either ssh or use vnc and run boot.py,
similarly to kill if pc is frozen run kill.py
