# GitOTA: Process self-updater from git repository

### Python on macOS example

![Visual Demo](https://github.com/afonsofigs/updater_testes/blob/main/message_change_demo.png?raw=true)

# How does it work:

- After cloning the repository to your computer and starting the main program, periodically it checks for changes on the
  remote git repository. If there are new changes, it resets the code on the local repository to match the remote
  repository and restart itself, now running with the new code.

- This can be easily transformed to run in every language, as long as the device or OS running the code can run git
  commands.

- It can also be used to update IoT systems, without the need of building a custom update server or using an external
  SaaS.

# Demo instructions:

1. Fork this repository to a repository of yours.

2. Start by installing the required python packages:

```
pip3 install -r ./requirements.txt
```

3. Run main.py:

```
python3 ./main.py
```

this will open Terminal windows and print a custom phrase.

4. Online on your GitHub repository, or on a different computer than the one currently running main.py, change the
   message that main.py prints. Don't forget to commit and push it.

```
message = "all great at: " + str(datetime.now())
```

5. The old process will now update itself and Terminal windows will continue to appear, now with the new message, just
   like the progression we see on the first image.

# Not on macOS?

Fork the code to a repository of yours and change the command that opens the Terminal windows, on main.py, to open and
print the message on the console of your OS.
Change this on main.py:

```
tell.app('Terminal', 'do script "' + yourCommand + '"')
```

then do the same as in the demo instructions.