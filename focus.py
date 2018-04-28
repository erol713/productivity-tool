import time
from datetime import datetime as dt

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
        #You will need administrator privileges for this, run cmd as admin
redirect = '117.0.0.1' '''This is a dead site'''
distractors = ['www.facebook.com', 'www.index.hr', 'www.thewrap.com', 'www.livescore.com', 'www.rezultati.com']
print(dt.now())

while True:
    '''If the time we set is later than now and earlier than the second time mark'''
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working Hours: ")

        with open(hosts_path, 'r+') as file:
            content = file.read()
            '''This will open our host file'''
            for site in distractors:
                if site in content:
                    pass
                else:
                    '''Here we write the names of the distracting pages in the host file, making them unaproachable'''
                    file.write(redirect + ' ' + site + '\n')

    else:
        '''If the time is not in the set parimeter'''
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            '''placing the pointer to the begining'''
            for line in content:
        #rewriting every line by line of the original hosts file without the blocked sites
                if not any(site in line for site in distractors):
                    file.write(line)
            file.truncate()
            '''Delete the written pages so they could run normaly'''
        print('Have fun')
    time.sleep(600)
    '''write the status every 10 minutes'''

