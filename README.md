# ghpush - Python program to simplify the "git push origin master" step on Windows

On Windows when running the git command line:

```
git push origin master
```

you can be prompted for your github username and password.

What the `ghpush` Python program does is automate this by supplying the github
username and github password.

The github username is read from the `%USERPROFILE%\.gitconfig` file.
It looks for the line `name = githubusername` in the `[user]` stanza.

The github password is read from the `GHPASS` environment variable.
This must be set before running the `ghpush` Python program.  One way to set
the `GHPASS` environment variable is with `setpw.bat` which you can
find here:

* [Set Windows/UNIX/Linux environment variables with a password but keep the password hidden](https://github.com/andycranston/setpw)

## Pre-requisites

Python 3 must be installed.

The `pyautogui` module must be installed in the Python 3 environment.

The defaults for your Windows command prompt must have a handful of
attributes set a certain way.  Specifically:

+ The background colour must be black (RGB value 255,255,255)
+ The foreground colour must be white (RGB value 0,0,0)
+ The font must be `Raster Fonts`
+ The font size must be `8 x 12`

## Installing

Create a new directory to hold the `ghpush.py` Python program and supporting files.
I created the following directory:

```
C:\andyc\projects\ghpush-win
```

Copy the following files to this directory:

```
ghpass.png
ghpush.bat
ghpush.py
ghpush.png
ghpass.png
```

Next edit the file:

```
ghpush.bat
```

Change the line which reads:

```
SET GHHOME=C:\andyc\projects\ghpush-win
```

and change the directory name to match the directory you have copied the files into.

Next copy the `ghpush.bat` file to a directory in your `PATH` environment variable.
Because I have administrator rights on my Windows 10 system I copied it to:

```
C:\Windows
```

If you do not have access rights then select a directory in your `PATH` that you do
have write access to.

## Running

First make sure you have set the `GHPASS` environment variable to hold your
current Github account password.

Next whenever you would type:

```
git push origin master
```

instead just type:

```
ghpush
```

The screen clears and the following character sequence:

```
~~@(!--#~~
```

appears briefly (a couple of seconds).

Then the screen clears again and the `git` command is run as follows:

```
git push origin master
```

If the `git` command asks for the username or password then it is supplied automatically.

That's it!

##

## Just cache your credentials?

Yes there are other ways to supply the usernamne and password
including having the credentials cached or stored using various encryption
methods.  The `ghpush` Python program is just a different approach.

One advantage of the `ghpush` Python program is that the github password
is only stored in the GHPASS environment variable for the duration of
that command prompt session.  As long as you keep the session secure (i.e. do
not leave your workstation unattended) then your password is safe.

---------------------------------------------
End of README.md
