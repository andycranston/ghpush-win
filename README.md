# ghpush - Python program to simplify the "git push origin master" step on Windows

On Windows when running the git command line:

```
git push origin master
```

you can be prompted for your github username and password.

What the `ghpush` Python program does is automate this by supplying the github
username and github password.

The github username is extracted from the `%HOMEPROFILE%\.gitconfig` file.
In particular it looks for the line:

```
name = githubusername
```

in the `[user]` stanza.

The github password is read from the `GHPASS` environment variable.
This must be set before running the `ghpush` Python program.  One way to set
the `GHPASS` environment variable is with `setpw.bat` which you can
find here:

* [Set Windows/UNIX/Linux environment variables with a password but keep the password hidden](https://github.com/andycranston/setpw)

Here is a typical run of the `ghpush` Python program:

```
C:\some\directory> ghpush
spawn git push origin master
Username for 'https://github.com': andycranston
Password for 'https://andycranston@github.com':
Everything up-to-date
C:\some\directory>
```

## Pre-requisites

Python 3 must be installed.

## Installing

Create a new directory to hold the Python program and supporting files.
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

Next copy the `ghpush.bat` directory in your `PATH` environment variable.  Because I have administrator
rights on my Windows 10 system I copied it to:

```
C:\Windows
```

If you do not have access rights then select a directory in your `PATH` that you do
have write access to.

## Running

Whenever you would type:

```
git push origin master
```

instead just type:

```
ghpush
```

Easy :-]

## Just cache your credentials?

Yes there are many other ways to supply the usernamne and password
including having the credentials cached or stored using various encryption
methods.

The `ghpush` Python program is just a different approach.

One advantage of the `ghpush` Python program is that the github password
is only stored in the GHPASS environment variable for the duration of
that command prompt session.  As long as you keep the session secure (i.e. do
not leave your workstation unattended) then your password is safe.

---------------------------------------------
End of README.md
