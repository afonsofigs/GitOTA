import subprocess
import sys
import time
from datetime import datetime as date

from sh import git


def check_for_update(git_working_dir):
    print("Fetching most recent code from source..." + git_working_dir)
    # Fetch most up-to-date version of code.
    git("--git-dir=" + git_working_dir + ".git/", "--work-tree=" + git_working_dir, "fetch", "origin", "main")
    print("Fetch complete.")
    print("Checking status for " + git_working_dir + "...")
    status_check = git("--git-dir=" + git_working_dir + ".git/", "--work-tree=" + git_working_dir, "status")
    # print(status_check)
    if "Your branch is up to date" in status_check and "Changes not staged for commit" not in status_check:
        print("Status check passes.")
        print("Code up to date.")
        return False
    else:
        print("Code update available.")
        return True


if __name__ == "__main__":
    next_check_wait_sec = 30
    git1_dir = "./"
    git1_url = "https://github.com/afonsofigs/updater_testes.git"

    # Start main_v1
    mp = subprocess.Popen(['python', 'main.py'])
    # Start update procedure
    while True:
        print("***** Checking for code update at: " + str(date.now()) + " *****")
        if check_for_update(git1_dir):
            print("Stopping main.py v1")
            mp.terminate()

            print("Resetting code...")
            # overwrite local code with remote code, losing local changes.
            git("--git-dir=" + git1_dir + ".git/", "--work-tree=" + git1_dir, "reset", "--hard",
                "origin/main")
            # fully clean untracked files and artifacts, not good idea if there are data files
            # git("--git-dir=" + git1_dir + ".git/", "--work-tree=" + git1_dir, "clean", "-df")

            # Start updater_v2
            print("Starting updater.py v2")
            subprocess.Popen(['python', 'updater.py'])
            sys.exit()
        else:
            print("No updates found.")
        print("Check complete. Waiting " + str(next_check_wait_sec) + " seconds until next check...")
        time.sleep(next_check_wait_sec)
