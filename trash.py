class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order(self):
        elements = []  # Start with an empty list
        print(f"Entering node with data: {self.data}")

        # Check if there is a left subtree to traverse
        if self.left:
            print(f"Going left from node {self.data}")
            left_elements = self.left.in_order()  # Recursively get the in-order elements of the left subtree
            print(f"Back at node {self.data} from left child, left_elements: {left_elements}")
            elements += left_elements  # Add those elements to the main list
            print(f"After adding left elements, elements: {elements}")

        # Add the current node's data to the list
        elements.append(self.data)
        print(f"Added node {self.data} to elements, elements now: {elements}")

        # Check if there is a right subtree to traverse
        if self.right:
            print(f"Going right from node {self.data}")
            right_elements = self.right.in_order()  # Recursively get the in-order elements of the right subtree
            print(f"Back at node {self.data} from right child, right_elements: {right_elements}")
            elements += right_elements  # Add those elements to the main list
            print(f"After adding right elements, elements: {elements}")

        print(f"Exiting node with data: {self.data}, returning elements: {elements}")
        return elements

# Create the tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

# Perform in-order traversal
print("In-order traversal result:", root.in_order())
