from datetime import datetime as date

from sh import git


def check_for_update(git_working_dir):
    print("Fetching most recent code from source..." + git_working_dir)
    # Fetch most up-to-date version of code.
    git("--git-dir=" + git_working_dir + ".git/", "--work-tree=" + git_working_dir, "fetch", "origin", "main")
    print("Fetch complete.")
    print("Checking status for " + git_working_dir + "...")
    git_status = git("--git-dir=" + git_working_dir + ".git/", "--work-tree=" + git_working_dir, "status")
    # print(git_status)
    if "Your branch is up to date" in git_status and "Changes not staged for commit" not in git_status:
        print("Code up to date.")
        return False
    else:
        print("Code update available.")
        return True


def update():
    git_dir = "./"
    print("***** Checking for code update at: " + str(date.now()) + " *****")
    if check_for_update(git_dir):
        print("Resetting code...")
        # overwrite local code with remote code, losing local changes.
        git("--git-dir=" + git_dir + ".git/", "--work-tree=" + git_dir, "reset", "--hard", "origin/main")
        # fully clean untracked files and artifacts, not good idea if there are data files
        # git("--git-dir=" + git_dir + ".git/", "--work-tree=" + git_dir, "clean", "-df")
        print("Reset finished.")
        # True means code has updated
        return True
    else:
        return False


if __name__ == "__main__":
    check_for_update("./")
