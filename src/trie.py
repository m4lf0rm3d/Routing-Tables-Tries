"""
📌 Trie Data Structure Implementation

✨ The Trie class consists of two main classes: TrieNode and Trie. The TrieNode class represents a node in the trie and contains three attributes: 

👉 CHILD_NODES: which is a dictionary that stores the child nodes of the current node.
👉 IS_END: which is a flag that determines whether the current node is the end of a network address. 
👉 NEXT_HOP: which stores the next hop address if the current node is the end of a network address.

✨ The Trie Class consist of following attributes and functions:

👉 ROOT: the root/starting node for trie

👉 insert(self, NETWORK_ADDRESS: str, NEXT_HOP: str) -> None: 

    ✅ Time Complexity: O(k) where k is the length of the network address string
    ✅ Space Complexity: O(k) where k is the length of the network address string

👉 search(self, NETWORK_ADDRESS: str) -> TrieNode: 

    ✅ Time Complexity: O(k) where k is the length of the network address string
    ✅ Space Complexity: O(1) algorithm uses constant space to save child nodes

👉 delete(self, NETWORK_ADDRESS: str) -> None: 

    ✅ Time Complexity: O(k) where k is the length of the network address string
    ✅ Space Complexity: O(k) where k is the length of the network address string

👉 print_trie(self) -> None: 

    ✅ Time Complexity: O(k * N) where k is the length of the network address string and N is the total number of network addresses in trie
    ✅ Space Complexity: O(k * N) where k is the length of the network address string and N is the total number of network addresses in trie

👉 get_all_networks(self) -> List[Tuple[str, str]]: 

   ✅ Time Complexity: O(k * N) where k is the length of the network address string and N is the total number of network addresses in trie
   ✅ Space Complexity: O(k * N) where k is the length of the network address string and N is the total number of network addresses in trie

"""

from typing import List, Tuple

class TrieNode:
    """
    Class for each node of Network Address
    """

    def __init__(self):
        self.CHILD_NODES = {}  # stores child nodes of current node
        self.IS_END = False   # flag to determine if current node is end of a network address
        self.NEXT_HOP = None  # stores next hop if current node is end of a network address

    def __str__(self):
        return self.NEXT_HOP  # returns string representation of NEXT_HOP

class Trie:
    def __init__(self):
        self.ROOT = TrieNode()  # initialize the root of Trie

    def insert(self, NETWORK_ADDRESS: str, NEXT_HOP: str) -> None:
        """
        Inserts a network address with its corresponding next hop into the Trie.

        Args:
        - NETWORK_ADDRESS: A string representing the network address to be inserted.
        - NEXT_HOP: A string representing the next hop address for the given network address.

        Returns: None
        """

        CURRENT_CHILD = self.ROOT  # start from root

        for CHAR in NETWORK_ADDRESS:
            # traverse through the trie to add each character of the network address as a child node
            if CHAR not in CURRENT_CHILD.CHILD_NODES:
                CURRENT_CHILD.CHILD_NODES[CHAR] = TrieNode()
            CURRENT_CHILD = CURRENT_CHILD.CHILD_NODES[CHAR]

        # mark the last node as the end of a network address and set the next hop
        CURRENT_CHILD.IS_END = True
        CURRENT_CHILD.NEXT_HOP = NEXT_HOP

    def search(self, NETWORK_ADDRESS: str) -> TrieNode:
        """
        Searches for a network address in the Trie and returns the corresponding node if found.

        Args:
        - NETWORK_ADDRESS: A string representing the network address to be searched.

        Returns:
        - If the network address is found, returns the corresponding TrieNode; otherwise, returns None.
        """

        CURRENT_CHILD = self.ROOT  # start from root

        for CHAR in NETWORK_ADDRESS:
            # traverse through the trie to search for the network address
            if CHAR not in CURRENT_CHILD.CHILD_NODES:
                return None  # return None if network address not found
            CURRENT_CHILD = CURRENT_CHILD.CHILD_NODES[CHAR]

        return CURRENT_CHILD if CURRENT_CHILD.IS_END else None  # return the node if it's the end of a network address

    def delete(self, NETWORK_ADDRESS: str) -> None:
        """
        Deletes a network address from the Trie.
        
        Args:
        - NETWORK_ADDRESS: A string representing the network address to be deleted.

        Returns: None
        """

        self._delete_helper(NETWORK_ADDRESS, self.ROOT, 0)

    def _delete_helper(self, NETWORK_ADDRESS: str, CURRENT_CHILD: TrieNode, DEPTH: int) -> None:
        if DEPTH == len(NETWORK_ADDRESS):
            # if end of network address is reached, remove the end flag and next hop
            if CURRENT_CHILD.IS_END:
                CURRENT_CHILD.IS_END = False
                CURRENT_CHILD.NEXT_HOP = None
            return

        CHAR = NETWORK_ADDRESS[DEPTH]
        if CHAR in CURRENT_CHILD.CHILD_NODES:
            # recursively traverse through the trie to delete the network address
            CHILD = CURRENT_CHILD.CHILD_NODES[CHAR]
            self._delete_helper(NETWORK_ADDRESS, CHILD, DEPTH+1)

            # if the child node has no child nodes, is not the end of a network address, and has no next hop,
            # remove the child node
            if not CHILD.IS_END and len(CHILD.CHILD_NODES) == 0 and CHILD.NEXT_HOP is None:
                del CURRENT_CHILD.CHILD_NODES[CHAR]

    def print_trie(self) -> None:
        """
        Prints all the network addresses and their corresponding next hops stored in the Trie.
        """

        self._print_helper(self.ROOT, "")


    def _print_helper(self, CURRENT_CHILD: TrieNode, PREFIX: str) -> None:
        """
        Prints the next hop of the current child if it's an end node.
        Recursively prints the next hop of all child nodes.
        
        Args:
        - CURRENT_CHILD (Node): current child node
        - PREFIX (str): prefix string
        
        Returns: None
        """

        if CURRENT_CHILD.IS_END:
            print(CURRENT_CHILD.NEXT_HOP)
            
        for CHAR in CURRENT_CHILD.CHILD_NODES:
            self._print_helper(CURRENT_CHILD.CHILD_NODES[CHAR], PREFIX+CHAR)

    def get_all_networks(self) -> List[Tuple[str, str]]:
        """
        Returns a list of tuples representing all the network addresses in the trie.
        
        Args: None
        
        Returns:
        - ALL_NETWORKS_ADDRESSES (List[Tuple[str, str]]): list of tuples representing all network addresses
        """

        ALL_NETWORKS_ADDRESSES = []
        self._get_all_networks_helper(self.ROOT, "", ALL_NETWORKS_ADDRESSES)
        return ALL_NETWORKS_ADDRESSES

    def _get_all_networks_helper(self, CURRENT_CHILD: TrieNode, PREFIX: str, ALL_NETWORKS_ADDRESSES: List[Tuple[str, str]]) -> None:
        """
        Recursively adds tuples representing all network addresses to the ALL_NETWORKS_ADDRESSES list.
        
        Args:
        - CURRENT_CHILD (Node): current child node
        - PREFIX (str): prefix string
        - ALL_NETWORKS_ADDRESSES (List[Tuple[str, str]]): list of tuples representing all network addresses
        
        Returns: None
        """

        if CURRENT_CHILD.IS_END:
            ALL_NETWORKS_ADDRESSES.append((PREFIX, CURRENT_CHILD.NEXT_HOP))
            
        for CHAR in CURRENT_CHILD.CHILD_NODES:
            self._get_all_networks_helper(CURRENT_CHILD.CHILD_NODES[CHAR], PREFIX+CHAR, ALL_NETWORKS_ADDRESSES)