"""
📌 Data Set Generator

✨ This code generates a CSV file containing random network addresses, CIDR ranges, and next hop IP addresses. It ensures that the generated network addresses are unique and excludes reserved IP addresses, such as the default route, broadcast address, and loopback IP address.

✅ Time Complexity: O(N) where N is the number of rows
✅ Space Complexity: O(N) where N is the number of rows

"""

import csv
import ipaddress
import random

# set the number of rows you want to generate
NUMBER_OF_ROWS = 1000000 #stores 1 million rows

# create a set to store the generated network addresses
NETWORK_ADDRESSES = set()

# write routes to a CSV file
with open('network_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['network_address', 'cidr', 'next_hop'])

    # generate unique network addresses and CIDR ranges
    while len(NETWORK_ADDRESSES) < NUMBER_OF_ROWS:

        # generate a random IP address
        RANDOM_IP = ipaddress.IPv4Address(random.randint(1, 2**32 - 1))

        # generate a random CIDR range
        CIDR = random.randint(1, 30)

        #list of all masks [1-30] because 31 and 32 will have no usable host and 0 will contain all combinations
        ALL_MASKS = ["255.255.255.252", "255.255.255.248", "255.255.255.240", "255.255.255.224", "255.255.255.192", "255.255.255.128", "255.255.255.0", "255.255.254.0", "255.255.252.0", "255.255.248.0", "255.255.240.0", "255.255.224.0", "255.255.192.0", "255.255.128.0", "255.255.0.0", "255.254.0.0", "255.252.0.0", "255.248.0.0", "255.240.0.0", "255.224.0.0", "255.192.0.0", "255.128.0.0", "255.0.0.0", "254.0.0.0", "252.0.0.0", "248.0.0.0", "240.0.0.0", "224.0.0.0", "192.0.0.0", "128.0.0.0"]

        # get a random network mask
        RANDOM_MASK = ipaddress.IPv4Address(random.choice(ALL_MASKS))
        
        # calculate the network address
        NETWORK_ADDRESS = ipaddress.IPv4Address(int(RANDOM_IP) & int(RANDOM_MASK))

        # check if the network address is unique and check if its not the default route and also check if its the broadcast address and also check if its loopback IP
        if NETWORK_ADDRESS not in NETWORK_ADDRESSES and str(NETWORK_ADDRESS) != '0.0.0.0' and str(NETWORK_ADDRESS)[:3] != '255' and str(NETWORK_ADDRESS)[3] != '127':

            # add the network address to the set of unique network addresses
            NETWORK_ADDRESSES.add(NETWORK_ADDRESS)

            # generate a random next hop IP address
            RANDOM_NEXT_HOP_IP = str(ipaddress.IPv4Address(random.randint(10000, 2**32 - 1)))

            # write each route to csv file
            writer.writerow((str(NETWORK_ADDRESS), CIDR, RANDOM_NEXT_HOP_IP))