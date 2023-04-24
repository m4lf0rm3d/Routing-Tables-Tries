import sys
import os
import csv
import time
import ipaddress

DATASETS = os.path.join(os.path.abspath(""), 'data', 'network_data.csv')

sys.path.append(os.path.abspath("src"))

from routing_table import Routing_Table

class Easy_Routing:
    def __init__(self): 
        self.ROUTING_TABLE = Routing_Table()
        self.COLORS = {
            "GREEN" : '\033[92m',
            "RED" : '\033[91m',
            "BOLD" : '\033[1m',
            "END" : '\033[0m'
        }

    def print_banner(self):
        BANNER = """   _______   ______  __   ___  ____  __  _____________  _______  
  / __/ _ | / __/\ \/ /  / _ \/ __ \/ / / /_  __/  _/ |/ / ___/  
 / _// __ |_\ \   \  /  / , _/ /_/ / /_/ / / / _/ //    / (_ /   
/___/_/ |_/___/   /_/  /_/|_|\____/\____/ /_/ /___/_/|_/\___/ v1.0
                                                              \n"""
        sys.stdout.write(self.COLORS['RED'] + BANNER + self.COLORS['END'])

    def load(self):
        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Initializing datasets <<<\n"+self.COLORS['END'])
        with open(DATASETS) as CSV_FILE:
            CSV_READER = csv.reader(CSV_FILE)
            for index, row in enumerate(CSV_READER):
                
                if index == 0: continue
                if (index + 1) % 100000 == 0:
                    
                    LOAD_STATUS = ((index+1)/1000000)*100
                    
                    print(self.COLORS['GREEN']+"\rPROGRESS: "+f"[{'#'*4 * int(LOAD_STATUS//10)}{'.'*4*(10-int(LOAD_STATUS//10))}] ("+str(LOAD_STATUS)+"%)"+self.COLORS['END'], end="", flush=True)
                self.ROUTING_TABLE.add_route(row[0], row[1], row[2])


    def add_route(self, update = False):
        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Add routes <<<\n"+self.COLORS['END']) if not update else print(self.COLORS['BOLD']+"\n>>> Update routes <<<\n"+self.COLORS['END'])

        NETWORK_ADDRESS = None
        while not NETWORK_ADDRESS:
            try:
                NETWORK_ADDRESS = ipaddress.IPv4Address(input("Enter network address:\n>>> "))
            except:
                print(self.COLORS['RED']+"Invalid network address!"+self.COLORS['END'])
                time.sleep(1)
                os.system('clear')
                self.print_banner()
                print(self.COLORS['BOLD']+"\n>>> Add routes <<<\n"+self.COLORS['END']) if not update else print(self.COLORS['BOLD']+"\n>>> Update routes <<<\n"+self.COLORS['END'])

        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Add routes <<<\n"+self.COLORS['END']) if not update else print(self.COLORS['BOLD']+"\n>>> Update routes <<<\n"+self.COLORS['END'])
        print("👉 Network address: "+str(NETWORK_ADDRESS))

        MASK = None
        while not MASK:
            try:
                MASK = int(input("\nEnter mask:\n>>> "))
                if(MASK<=0): raise ValueError()
                if(MASK>=31): raise ValueError()
            except:
                print(self.COLORS['RED']+"Invalid mask!"+self.COLORS['END'])
                time.sleep(1)
                os.system('clear')
                self.print_banner()
                print(self.COLORS['BOLD']+"\n>>> Add routes <<<\n"+self.COLORS['END']) if not update else print(self.COLORS['BOLD']+"\n>>> Update routes <<<\n"+self.COLORS['END'])
                print("👉 Network address: "+str(NETWORK_ADDRESS))
                MASK = None

        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Add routes <<<\n"+self.COLORS['END']) if not update else print(self.COLORS['BOLD']+"\n>>> Update routes <<<\n"+self.COLORS['END'])
        print("👉 Network address: "+str(NETWORK_ADDRESS))
        print("👉 Mask: "+str(MASK)) 

        NEXT_HOP_IP = None

        while not NEXT_HOP_IP:
            try:
                UPDATE_NEXT_NEW_HOP = input("\nEnter next hop IP:\n>>> ") if not update else input("\nEnter new hop IP:\n>>> ")
                NEXT_HOP_IP = ipaddress.IPv4Address(UPDATE_NEXT_NEW_HOP)
            except:
                print(self.COLORS['RED']+"Invalid next hop IP!"+self.COLORS['END']) if not update else print(self.COLORS['RED']+"Invalid new hop IP!"+self.COLORS['END'])
                time.sleep(1)
                os.system('clear')
                self.print_banner()
                print(self.COLORS['BOLD']+"\n>>> Add routes <<<\n"+self.COLORS['END']) if not update else print(self.COLORS['BOLD']+"\n>>> Update routes <<<\n"+self.COLORS['END'])
                print("👉 Network address: "+str(NETWORK_ADDRESS))
                print("👉 Mask: "+str(MASK))
                NEXT_HOP_IP = None

        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Add routes <<<\n"+self.COLORS['END'])
        print("👉 Network address: "+str(NETWORK_ADDRESS))
        print("👉 Mask: "+str(MASK))
        print("👉 Next hop IP: "+str(NEXT_HOP_IP)) if not update else print("👉 New hop IP: "+str(NEXT_HOP_IP))

        self.ROUTING_TABLE.delete_route(str(NETWORK_ADDRESS), str(MASK))
        self.ROUTING_TABLE.add_route(str(NETWORK_ADDRESS), str(MASK), str(NEXT_HOP_IP))

        print("\n✅"+self.COLORS['GREEN'] +" Route added successfully!\n"+self.COLORS['END']) if not update else print("\n✅"+self.COLORS['GREEN'] +" Route updated successfully!\n"+self.COLORS['END'])
        time.sleep(2)

    def delete_route(self):
        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Delete routes <<<\n"+self.COLORS['END'])
        NETWORK_ADDRESS = None
        while not NETWORK_ADDRESS:
            try:
                NETWORK_ADDRESS = ipaddress.IPv4Address(input("Enter network address:\n>>> "))
            except:
                print(self.COLORS['RED']+"Invalid network address!"+self.COLORS['END'])
                time.sleep(1)
                os.system('clear')
                self.print_banner()
                print(self.COLORS['BOLD']+"\n>>> Delete routes <<<\n"+self.COLORS['END'])

        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Delete routes <<<\n"+self.COLORS['END'])
        print("👉 Network address: "+str(NETWORK_ADDRESS))

        MASK = None
        while not MASK:
            try:
                MASK = int(input("\nEnter mask:\n>>> "))
                if(MASK<=0): raise ValueError()
                if(MASK>=31): raise ValueError()
            except:
                print(self.COLORS['RED']+"Invalid mask!"+self.COLORS['END'])
                time.sleep(1)
                os.system('clear')
                self.print_banner()
                print(self.COLORS['BOLD']+"\n>>> Delete routes <<<\n"+self.COLORS['END'])
                print("👉 Network address: "+str(NETWORK_ADDRESS))
                MASK = None

        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Delete routes <<<\n"+self.COLORS['END'])
        print("👉 Network address: "+str(NETWORK_ADDRESS))
        print("👉 Mask: "+str(MASK))

        self.ROUTING_TABLE.delete_route(str(NETWORK_ADDRESS), str(MASK))

        print("\n✅"+self.COLORS['GREEN'] +" Route deleted successfully!\n"+self.COLORS['END'])
        time.sleep(2)

    def get_route(self):
        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Get routes <<<\n"+self.COLORS['END'])
        IP_ADDRESS = None
        while not IP_ADDRESS:
            try:
                IP_ADDRESS = ipaddress.IPv4Address(input("Enter IP address:\n>>> "))
            except:
                print(self.COLORS['RED']+"Invalid IP address!"+self.COLORS['END'])
                time.sleep(1)
                os.system('clear')
                self.print_banner()
                print(self.COLORS['BOLD']+"\n>>> Get routes <<<\n"+self.COLORS['END'])

        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Get routes <<<\n"+self.COLORS['END'])

        SEARCH_RESULT = str(self.ROUTING_TABLE.get_route(str(IP_ADDRESS)))

        print(self.COLORS['GREEN'] + "📌 Next hop IP: " + SEARCH_RESULT + self.COLORS['END']) if SEARCH_RESULT != 'None' and SEARCH_RESULT != '172.217.19.164' else print(self.COLORS['RED'] + "😔 Route not exists!"+self.COLORS['GREEN'] +" \n\nHere's the default route:\n📌 Next hop IP: 172.217.19.164" + self.COLORS['END'])

        input("\n>>> Press ENTER to return! ")

        return

    def export_table(self):
        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Export table <<<\n"+self.COLORS['END'])

        ROW_COUNT = None
        while not ROW_COUNT:
            try:
                ROW_COUNT = int(input("Enter row count for table e.g (10-10000):\n>>> "))

                if(ROW_COUNT < 10 or ROW_COUNT > 10000): ROW_COUNT = None

            except:
                print(self.COLORS['RED']+"Invalid row count!"+self.COLORS['END'])
                time.sleep(1)
                os.system('clear')
                self.print_banner()
                print(self.COLORS['BOLD']+"\n>>> Export table <<<\n"+self.COLORS['END'])

        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Export table <<<\n"+self.COLORS['END'])
        print("👉 Row count: "+str(ROW_COUNT))

        self.ROUTING_TABLE.export_table(ROW_COUNT)

        print("\n✅"+self.COLORS['GREEN'] +" Table exported successfully!\n"+self.COLORS['END'])

        time.sleep(2)


    def run(self):
        os.system('clear')
        self.print_banner()
        print(self.COLORS['BOLD']+"\n>>> Choose an option to continue <<<\n"+self.COLORS['END'])
        print("1) Add routes")
        print("2) Delete routes")
        print("3) Update routes")
        print("4) Get routes")
        print("5) Export table")
        print("6) Exit")
        print("\nYour option (1-6):")

        try:
            OPTION_CHOSEN = int(input(">>> "))

            match OPTION_CHOSEN:

                case 1:
                    self.add_route()
                    self.run()
                
                case 2:
                    self.delete_route()
                    self.run()

                    

                case 3:
                    self.add_route(update=True)
                    self.run()

                case 4:
                    self.get_route()
                    self.run()

                case 5:
                    self.export_table()
                    self.run()

                case 6:
                    print(self.COLORS['GREEN']+"\nThankyou for using Easy Routing v1.0 ;)"+self.COLORS['END'])
                    return
                    
                case _:
                    print(self.COLORS['RED']+"Invalid option!"+self.COLORS['END'])
                    time.sleep(1)
                    os.system('clear')
                    self.run()


        except:
            print(self.COLORS['RED']+"Invalid option!"+self.COLORS['END'])
            time.sleep(1)
            os.system('clear')
            self.run()

if __name__ == "__main__":
    CISCO_TABLE = Easy_Routing()
    CISCO_TABLE.load()
    CISCO_TABLE.run()