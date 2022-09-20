import socket
from IPy import IP
from termcolor import colored

def port_service(s):
    return s.recv(1024)

def scan_preference():
    print(colored('''

        ◎ Low but fast - 1
        ◎ Medium but moderate - 2
        ◎ High but slow - 3

◎ Only enter the integer value assigned to the options ◎    
    ''', 'green'))
    try:
        accuracy = int(input(colored("Enter your scan preference: ", 'blue')))
        return accuracy
    except ValueError:
        print(colored("[-] Enter correct Scan Preference [-]", 'red'))
        scan_preference()

def targets_scan(target):
    domain_check = check_IP(target)
    print(colored("\n" + "◎ Scanning Target " + str(target) + " ◎", 'green'))
    scan_accuracy = scan_preference()
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
    while True:
        try: 
            port = int(input(colored("Enter your Port preference: ", 'blue')))
            try:
                if port == 1:
                    if scan_accuracy == 1:
                        a = 0.5
                        print(colored("\n◎ Scanning the first 100 ports ◎\n", 'green'))
                        for p in range(1,101):
                            scan(domain_check, p, a)
                    elif scan_accuracy == 2:
                        a = 1.5
                        print(colored("\n◎ Scanning the first 100 ports ◎\n", 'green'))
                        for p in range(1,101):
                            scan(domain_check, p, a)
                    elif scan_accuracy == 3:
                        a = 3
                        print(colored("\n◎ Scanning the first 100 ports ◎\n", 'green'))
                        for p in range(1,101):
                            scan(domain_check, p, a)
                elif port == 2:
                    if scan_accuracy == 1:
                        a = 0.5
                        print(colored("\n◎ Scanning for first 1000 Ports ◎\n", 'green'))
                        for p in range(1,1001):
                            scan(domain_check, p, a)
                    elif scan_accuracy == 2:
                        a = 1.5
                        print(colored("\n◎ Scanning for first 1000 Ports ◎\n", 'green'))
                        for p in range(1,1001):
                            scan(domain_check, p, a)
                    elif scan_accuracy == 3:
                        a = 3
                        print(colored("\n◎ Scanning for first 1000 Ports ◎\n", 'green'))
                        for p in range(1,1001):
                            scan(domain_check, p, a)
                elif port == 3:
                    if scan_accuracy == 1:
                        a = 0.5
                        print(colored("\n◎ Scanning all Ports ◎\n", 'green'))
                        for p in range(1,65536):
                            scan(domain_check, p, a)
                    elif scan_accuracy == 2:
                        a = 1.5
                        print(colored("\n◎ Scanning all Ports ◎\n", 'green'))
                        for p in range(1,65536):
                            scan(domain_check, p, a)
                    elif scan_accuracy == 3:
                        a = 3
                        print(colored("\n◎ Scanning all Ports ◎\n", 'green'))
                        for p in range(1,65536):
                            scan(domain_check, p, a)
                elif port == 4:
                    if scan_accuracy == 1:
                        a = 0.5
                        try:
                            p = int(input(colored("Enter your specific port: ", 'blue')))
                            print(colored("\n◎ Scanning port " + str(p) + " ◎\n", 'green'))
                            scan(domain_check, p, a)
                        except ValueError:
                            continue
                    elif scan_accuracy == 2:
                        a = 1.5
                        try:
                            p = int(input(colored("Enter your specific port: ", 'blue')))
                            print(colored("\n◎ Scanning port " + str(p) + " ◎\n", 'green'))
                            scan(domain_check, p, a)
                        except ValueError:
                            continue
                    elif scan_accuracy == 3:
                        a = 3
                        try:
                            p = int(input(colored("Enter your specific port: ", 'blue')))
                            print(colored("\n◎ Scanning port " + str(p) + " ◎\n", 'green'))
                            scan(domain_check, p, a)
                        except ValueError:
                            continue
                elif port == 5:
                    print(colored("[-] Quitting Portscanner for " + str(target) + " [-]", 'red'))
                    break
                elif port == 6:
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
                elif port == 7:
                    scan_accuracy = scan_preference()
            except ValueError:
                        continue
        except ValueError:
            print(colored("[-] Enter correct Preference [-]", 'red'))
            continue   
         
def check_IP(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan(ip, port, accuracy):
    try:
        node = socket.socket()
        node.settimeout(accuracy)
        node.connect((ip, port))
        try:
            service = port_service(node)
            print(colored('[+] Port ' + str(port) + " is Open: ", 'green') + colored(str(service.decode().strip('\n')), 'green'))
        except:
            print(colored('[+] Port ' + str(port) + " is Open", 'green'))
    except:
        pass

if __name__ == "__main__":
    print(colored('''\n
        ◎ While scanning multiple targets, the program will scan one by one.
                For example if you scanning 2 targets, it will initiate the first target first, when your first target is 
                    successfully scanned, exit your port preference using the exit option and then start scanning the second target. ◎ 
    \n''', 'green'))

    print(colored("\n◎ Split multiple Targets with ',' ◎\n", 'green'))
    targets = input(colored('◎ Enter Your Target/Targets: ', 'blue'))
    if ',' in targets:
        for ip_add in targets.split(','):
            targets_scan(ip_add.strip(' '))
    else:
        targets_scan(targets)

