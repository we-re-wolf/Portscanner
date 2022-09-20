import portscanner
from termcolor import colored

print(colored('''\n
       ◎ While scanning multiple targets, the program will scan one by one.
             For example if you scanning 2 targets, it will initiate the first target first, when your first target is 
                successfully scanned, exit your port preference using the exit option and then start scanning the second target. ◎ 
\n''', 'green'))

print(colored("\n◎ Split multiple Targets with ',' ◎\n", 'green'))
targets = input(colored('◎ Enter Your Target/Targets: ', 'blue'))
if ',' in targets:
    for ip_add in targets.split(','):
        portscanner.targets_scan(ip_add.strip(' '))
else:
    portscanner.targets_scan(targets)
