#
#
# @(!--#) @(#) ghpush.py, version 001, 29-january-2020
#
# a Python windows version of the ghpush expect script
#

########################################################################

import sys
import os
import threading
import time
import subprocess
import pyautogui

########################################################################

PASSWORD_ENV_VAR_NAME   = 'GHPASS'
GIT_CONFIG_FILE         = '.gitconfig'
CLEAR_SCREEN_LINE_TOTAL = 100
GIT_EXECUTABLE          = 'C:\\Program Files\\Git\\cmd\\git.exe'
### GHPUSH_STRING           = '>>@(!--#<<'
GHPUSH_STRING           = '~~@(!--#~~'
GHPUSH_IMAGE            = 'ghpush.png'
GHPUSH_USERNAME_IMAGE   = 'ghuser.png'
GHPUSH_PASSWORD_IMAGE   = 'ghpass.png'

########################################################################

def gitusername():
    try:
        profile = os.environ['USERPROFILE']
    except KeyError:
        return ''
        
    if profile == '':
        return ''
        
    gitconfigfilename = profile + '\\' + GIT_CONFIG_FILE
    
    try:
        gitconfig = open(gitconfigfilename, 'r', encoding='utf-8')
    except IOError:
        return ''
        
    username = ''
    sectionname = ''
    
    for line in gitconfig:
        line = line.strip()
        
        if len(line) < 3:
            continue
        
        if (line[0] == '[') and (line[-1] == ']'):
            sectionname = line
            continue

        words = line.split()
        
        if len(words) != 3:
            continue
        
        if words[1] != '=':
            continue
            
        if sectionname == '[user]':
            if words[0] == 'name':
                username = words[2]
                break
    
    gitconfig.close()
    
    return username

########################################################################

def cls():
    for i in range(0, CLEAR_SCREEN_LINE_TOTAL):
        print('')
    
    return

########################################################################

def rungit():
    git = subprocess.run([GIT_EXECUTABLE, 'push', 'origin', 'master'])
    
    return

########################################################################

def drivegit(git_thread, region, username, password):
    usernamesent = False
    passwordsent = False
    
    while (usernamesent == False) or (passwordsent == False):
        if not git_thread.is_alive():
            break

        screenshot = pyautogui.screenshot(region=region)
        
        if usernamesent == False:
            dummy = pyautogui.locate(GHPUSH_USERNAME_IMAGE, screenshot, grayscale=False)
            
            if dummy != None:
                pyautogui.write(username)
                pyautogui.press('enter')
                usernamesent = True
        
        if passwordsent == False:
            dummy = pyautogui.locate(GHPUSH_PASSWORD_IMAGE, screenshot, grayscale=False)
            
            if dummy != None:
                pyautogui.write(password)
                pyautogui.press('enter')
                passwordsent = True
        
        time.sleep(0.1)                
    
    return

########################################################################

def main():
    global progname
    
    try:
        password = os.environ[PASSWORD_ENV_VAR_NAME]
    except KeyError:
        print('{}: environment variable "{}" is not defined'.format(progname, PASSWORD_ENV_VAR_NAME), file=sys.stderr)
        sys.exit(1)
    
    if password == '':
        print('{}: environment variable "{}" is the null string'.format(progname, PASSWORD_ENV_VAR_NAME), file=sys.stderr)
        sys.exit(1)
    
    username = gitusername()
    
    if username == '':
        print('{}: unable to determine github username'.format(progname), file=sys.stderr)
        sys.exit(1)
        
    cls()
        
    ### print('\x1b[1;32;40m{}'.format(GHPUSH_STRING), end='', flush=True)
    print('{}'.format(GHPUSH_STRING), end='', flush=True)
    
    time.sleep(0.1)

    imagecount = 0
    
    for thisregion in pyautogui.locateAllOnScreen(GHPUSH_IMAGE, grayscale=False):
        imagecount += 1
        if imagecount == 1:
            region = thisregion
        
    cls()

    if imagecount == 0:
        print('{}: error - cannot locate the unique GHPUSH locator image'.format(progname), file=sys.stderr)
        sys.exit(1)
    
    if imagecount > 1:
        print('{}: error - more than one ({}) unique GHPUSH locator images found'.format(progname, imagecount), file=sys.stderr)
        sys.exit(1)

    ### print('Region is {}'.format(region))        

    git_thread     = threading.Thread(target=rungit, args=())    
    
    driving_thread = threading.Thread(target=drivegit, args=(git_thread, region, username, password))
    
    git_thread.start()
    driving_thread.start()
    
    git_thread.join()
    driving_thread.join()
    
    return 0

########################################################################

progname = os.path.basename(sys.argv[0])

sys.exit(main())

# end of file
