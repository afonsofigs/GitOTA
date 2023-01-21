import time
from datetime import datetime

if __name__ == "__main__":
    next_check_wait_sec = 60
    while True:
        print("All okaay at: ", datetime.now())
        time.sleep(next_check_wait_sec)
