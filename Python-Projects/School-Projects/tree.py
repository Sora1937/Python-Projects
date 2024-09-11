class Node:
    def _init_(self, key):
        self.key = key #Value of the node
        self.left = None # Reference to the left child node
        self.right = None # reference to the right child node

class BinarySearchTree:
    def _init_(self):
        self.root = None # Reference to the root node of the bst

    def insert(self, key):
        if self.root is None: # If the tree is empty
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if key < node.key: # If the key is less than the current node's key
            if node.left is None: # If the left child is empty
                node.left = Node(key) # Create a new node and set it as the left child
            else:
                self._insert_recursive(self.root, key) # Call the recursive insert function with the root
        else:
            if node.right is None: # If the right child is empty
                node.right = Node(key) # Create a new node and set it as the right child
            else:
                self._insert_recursive(node.right, key) # Recursively insert in the right subtree
    
    def search(self, key):
        return self._search_recursive(self.root, key) # Call the recursive search function with the root
    
    def _search_recursive(self, node, key):
        if node is None or node.key == key: # If the node is None or the key is found
            return node # Return the node (found) or None (not found)
        if key < node.key: # If the key is less than the current node's key
            return self._search_recursive(node.left, key) # Recursively search in the left subtree
        else:
            return self._search_recursive(node.right, key) # Recursively search in the right subtree

# Test the binary Search Tree
bst = BinarySearchTree()

# Insert nodes
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(5)
bst.insert(4)
bst.insert(7)

print(bst.search(4).key)
print(bst.search(10))