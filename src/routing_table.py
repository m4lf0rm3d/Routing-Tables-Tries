import ipaddress
import os
from trie import Trie

class Routing_Table:
    def __init__(self):
        self.NUM_OF_ROUTES = 0
        self.ROUTES = {}
        self.DEFAULT_ROUTE = '172.217.19.164'
        for MASK in range(1,31): self.ROUTES[str(MASK)] = Trie()

    def set_default_route(self, NEXT_HOP):
        self.DEFAULT_ROUTE = NEXT_HOP

    def add_route(self, NETWORK_ADDRESS, MASK, NEXT_HOP):
        self.ROUTES[MASK].insert(NETWORK_ADDRESS, NEXT_HOP)
        self.NUM_OF_ROUTES+=1

    def get_route(self, IP_ADDRESS):
        
        FOUND_ROUTE = None

        for MASK in self.ROUTES:
            NETWORK_ADDRESS = ipaddress.ip_network(IP_ADDRESS+'/'+str(MASK), strict=False).network_address
            FOUND_ROUTE = self.ROUTES[MASK].search(str(NETWORK_ADDRESS))
            if FOUND_ROUTE: return FOUND_ROUTE

        return self.DEFAULT_ROUTE

    def delete_route(self, NETWORK_ADDRESS, MASK):
        self.ROUTES[MASK].delete(NETWORK_ADDRESS)
        self.NUM_OF_ROUTES-=1


    def update_route(self, OLD_NETWORK_ADDRESS, OLD_MASK, NEW_NETWORK_ADDRESS, NEW_MASK, NEW_NEXT_HOP):
        self.ROUTES[OLD_MASK].delete(OLD_NETWORK_ADDRESS, OLD_NEXT_HOP)
        self.ROUTES[NEW_MASK].insert(NEW_NETWORK_ADDRESS, NEW_NEXT_HOP)

    def export_table(self, NUM_OF_ROWS = 10):
        if not os.path.exists("export"):
            os.makedirs("export")
        
        for mask in range(1, 31):
            mask_routes = self.ROUTES[str(mask)].get_all_networks()
            mask_file = f"export/{mask}.html"
            with open(mask_file, "w") as mask_file:
                mask_file.write("<html><head><style>")
                mask_file.write("* {box-sizing: border-box; margin: 0; padding: 0;}")
                mask_file.write("body {font-family: Arial, sans-serif;}")
                mask_file.write("h1 {text-align: center; margin-top: 20px; margin-bottom: 20px;}")
                mask_file.write("table {border-collapse: collapse; width: 700px; margin: 0 auto;}")
                mask_file.write("th, td {text-align: center; padding: 8px;}")
                mask_file.write("th {background-color: #4CAF50; color: white;}")
                mask_file.write("tr:nth-child(even) {background-color: #f2f2f2;}")
                mask_file.write("</style></head><body>")
                mask_file.write(f"<h1>Routes for Mask {mask}</h1>")
                mask_file.write("<table>")
                mask_file.write("<tr><th>Network Address</th><th>CIDR</th><th>Next Hop</th></tr>")
                for route in mask_routes[:NUM_OF_ROWS]:
                    mask_file.write(f"<tr><td>{route[0]}</td><td>{mask}</td><td>{route[1]}</td></tr>")
                mask_file.write("</table>")
                mask_file.write("<a href='index.html' style='text-decoration: underline; color: #4CAF50; font-weight: bold;display: block; text-align: center;margin: 20px auto;'>&larr; Back to Home</a>")
                mask_file.write("</body></html>")