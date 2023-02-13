import os
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

PASS = 'wwwpop13'
NAME = 'YouTuber'

print(bcolors.HEADER + " \n*** UPDATING UBUNTU APP ***\n " + bcolors.ENDC)
os.popen("sudo -S %s"%('apt update -y'), 'w').write('mypass')
time.sleep(10)

print(bcolors.OKBLUE + " \n*** UPGRATING UBUNTU APP ***\n " + bcolors.ENDC)
os.popen("sudo -S %s"%('apt upgrade -y'), 'w').write('mypass')
time.sleep(10)

print(bcolors.OKGREEN + " \n*** AUTOREMOVING UBUNTU APP ***\n " + bcolors.ENDC)
os.popen("sudo -S %s"%('apt autoremove -y'), 'w').write('mypass')
time.sleep(10)

print(bcolors.HEADER + " \n*** INSTALLING GOOGLE CHROME ***\n " + bcolors.ENDC)
os.popen("sudo -S %s"%('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'), 'w').write('mypass')
os.popen("sudo -S %s"%('apt install ./google-chrome-stable_current_amd64.deb -y'), 'w').write('mypass')
time.sleep(10)

print(bcolors.UNDERLINE + " \n*** INSTALLING python3.8 ***\n " + bcolors.ENDC)
os.popen("sudo -S %s"%('apt install python3.8 -y'), 'w').write('mypass')
os.popen("sudo -S %s"%('update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1'), 'w').write('mypass')
os.popen("sudo -S %s"%('update-alternatives --set python /usr/bin/python3.8'), 'w').write('mypass')
time.sleep(10)

print(bcolors.BOLD + " \n*** INSTALLING pip ***\n " + bcolors.ENDC)
os.popen("sudo -S %s"%('apt install python3-pip -y'), 'w').write('mypass')
os.popen("sudo -S %s"%('apt install python-pip -y'), 'w').write('mypass')
time.sleep(10)

print(bcolors.FAIL + " \n*** INSTALLING PYTHON MODULES ***\n " + bcolors.ENDC)
os.popen("sudo -S %s"%('pip install selenium'), 'w').write('mypass')
time.sleep(10)

print(bcolors.OKBLUE + " \n*** CREATING LOG FOLDER ***\n " + bcolors.ENDC)
os.popen("sudo -S %s"%('mkdir -m 777 /var/log/' + NAME), 'w').write('mypass')
time.sleep(10)

print(bcolors.UNDERLINE + " \n*** SETTING FULL PERMISSIONS ***\n " + bcolors.ENDC)
os.popen("sudo -S %s"%('chmod -R 777 /PYTHON'), 'w').write('mypass')