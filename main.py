import time
from datetime import datetime

from applescript import tell

if __name__ == "__main__":
    next_check_wait_sec = 10
    yourCommand = ("echo All okaay at: " + str(datetime.now()))

    while True:
        print("All okaay at: ", datetime.now())
        tell.app('Terminal', 'do script "' + yourCommand + '"')
        time.sleep(next_check_wait_sec)
