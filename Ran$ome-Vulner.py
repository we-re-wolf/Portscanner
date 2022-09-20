import vulner
from termcolor import colored

print(colored('''\n
        ◎ While scanning multiple targets, the program will scan one by one.
                For example if you scanning 2 targets, it will initiate the first target first, when your first target is 
                    successfully scanned, exit your port preference using the exit option and then start scanning the second target. ◎ 
    \n''', 'green'))

print(colored("\n◎ Split multiple Targets with ',' ◎\n", 'green'))
targets = input(colored('◎ Enter Your Target/Targets: ', 'blue'))
print(colored('''
                ◎ First 100 Ports - 1
                ◎ First 1000 Ports - 2
                ◎ All Ports - 3
                ◎ Specific Port - 4
                ◎ Exit - 5
                ◎ Show options - 6
                ◎ Change Scan Preference - 7

    ◎ Only choose one option and only type the integer corresponding to the Port ◎
        ''', 'green'))
ports = int(input("Enter Port Preference: "))
vuln_file = input("Enter Path to the file Vulnerable Softwares: ")
print('\n')
target = vulner.PortScan(targets, ports)
target.scan()