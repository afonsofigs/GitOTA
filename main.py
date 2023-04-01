import os
import sys
import time
from datetime import datetime

from applescript import tell

from updater import update

if __name__ == "__main__":
    next_check_wait_sec = 10
    while True:
        message = "all super at: " + str(datetime.now())
        yourCommand = ("echo " + message)
        print(message)
        # Open macOS terminal window and print the message
        tell.app('Terminal', 'do script "' + yourCommand + '"')

        # Check for updates and perform them
        if update():
            # Start the updated version of main.py, self re-launching
            # If using systemctl to control this main.py, simply set it to reboot always, no need for self re-launching
            print("Starting new main.py")
            os.system('python3 main.py')

            print("Terminating old main.py")
            sys.exit(0)

        print("Check complete")

        print("Waiting " + str(next_check_wait_sec) + " seconds until next check...")
        time.sleep(next_check_wait_sec)
