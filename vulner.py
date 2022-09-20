import socket
from IPy import IP
from termcolor import colored

class PortScan():
    services = []
    open_ports = []
    def __init__(self, target, port):
        self.target = target
        self.port = port

    def scan_preference(self):
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
            self.scan_preference()

    def targets_scan(self):
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
                                self.scan(p, a)
                        elif scan_accuracy == 2:
                            a = 1.5
                            print(colored("\n◎ Scanning the first 100 ports ◎\n", 'green'))
                            for p in range(1,101):
                                self.scan(p, a)
                        elif scan_accuracy == 3:
                            a = 3
                            print(colored("\n◎ Scanning the first 100 ports ◎\n", 'green'))
                            for p in range(1,101):
                                self.scan(p, a)
                    elif port == 2:
                        if scan_accuracy == 1:
                            a = 0.5
                            print(colored("\n◎ Scanning for first 1000 Ports ◎\n", 'green'))
                            for p in range(1,1001):
                                self.scan(p, a)
                        elif scan_accuracy == 2:
                            a = 1.5
                            print(colored("\n◎ Scanning for first 1000 Ports ◎\n", 'green'))
                            for p in range(1,1001):
                                self.scan(p, a)
                        elif scan_accuracy == 3:
                            a = 3
                            print(colored("\n◎ Scanning for first 1000 Ports ◎\n", 'green'))
                            for p in range(1,1001):
                                self.scan(p, a)
                    elif port == 3:
                        if scan_accuracy == 1:
                            a = 0.5
                            print(colored("\n◎ Scanning all Ports ◎\n", 'green'))
                            for p in range(1,65536):
                                self.scan(p, a)
                        elif scan_accuracy == 2:
                            a = 1.5
                            print(colored("\n◎ Scanning all Ports ◎\n", 'green'))
                            for p in range(1,65536):
                                self.scan(p, a)
                        elif scan_accuracy == 3:
                            a = 3
                            print(colored("\n◎ Scanning all Ports ◎\n", 'green'))
                            for p in range(1,65536):
                                self.scan(p, a)
                    elif port == 4:
                        if scan_accuracy == 1:
                            a = 0.5
                            try:
                                p = int(input(colored("Enter your specific port: ", 'blue')))
                                print(colored("\n◎ Scanning port " + str(p) + " ◎\n", 'green'))
                                self.scan(p, a)
                            except ValueError:
                                continue
                        elif scan_accuracy == 2:
                            a = 1.5
                            try:
                                p = int(input(colored("Enter your specific port: ", 'blue')))
                                print(colored("\n◎ Scanning port " + str(p) + " ◎\n", 'green'))
                                self.scan(p, a)
                            except ValueError:
                                continue
                        elif scan_accuracy == 3:
                            a = 3
                            try:
                                p = int(input(colored("Enter your specific port: ", 'blue')))
                                print(colored("\n◎ Scanning port " + str(p) + " ◎\n", 'green'))
                                self.scan(p, a)
                            except ValueError:
                                continue
                    elif port == 5:
                        print(colored("[-] Quitting Portscanner for " + str(self.target) + " [-]", 'red'))
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
                        scan_accuracy = self.scan_preference()
                except ValueError:
                            continue
            except ValueError:
                print(colored("[-] Enter correct Preference [-]", 'red'))
                continue   
            
    def check_IP(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan(self, port):
        try:
            domain_check = self.check_IP()
            scan_accuracy = self.scan_preference()
            node = socket.socket()
            node.settimeout(scan_accuracy)
            node.connect((domain_check, port))
            self.open_ports.append(port)
            try:
                service = node.recv(1024).decode().strip('\n')
                self.services.append(service)
            except:
                self.services.append(' ')
            node.close()
        except:
            pass


