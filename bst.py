"""File contains all the routines for BST and Node class"""


class Node:
    """Node class used for BST"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def size(self):
        """helper function for size called in BST"""
        if self.left and self.right:
            return 1 + self.left.size() + self.right.size()
        if self.left:
            return 1 + self.left.size()
        if self.right:
            return 1 + self.right.size()
        return 1

    def __repr__(self):
        """This helps display the tree"""
        lines = []
        if self.right:
            found = False
            for line in repr(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.key))
        if self.left:
            found = False
            for line in repr(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)


class BST:
    """Tree class and included routines"""
    def __init__(self):
        """initializer of root"""
        self.root = None

    def __repr__(self):
        """helper to print out the tree image"""
        return repr(self.root)

    def is_empty(self):
        """searches is tree to check if tree is empty or not"""
        curr_item = self.root
        if curr_item is None:
            return True
        return False

    def size(self):
        """return the size of the courses"""
        if self.root:
            return self.root.size()
        return 0

    def height(self):
        """Returns the height from root to leaf"""
        node = self.root
        return self.height_helper(node) + 1

    def height_helper(self, node):
        """recursive routine called by height function"""
        if node is None:
            return -1
        left_height = self.height_helper(node.left)
        right_height = self.height_helper(node.right)
        return 1 + max(left_height, right_height)

    def add(self, a_pair):
        """adds a pair to the tree"""

        pair_in_tree = self.find_pair_in_tree(a_pair)
        if pair_in_tree is not None:
            pair_in_tree.key.count += 1
            return self

        node = Node(a_pair)
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right

    def remove(self, key):
        """remove a node from the BST using the key which is a Pair class item"""
        parent = None
        current_node = self.root

        while current_node is not None:

            if current_node.key == key:
                if current_node.left is None and current_node.right is None:  # Case 1
                    if parent is None:  # Node is root
                        self.root = None
                    elif parent.left is current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return  # Node found and removed

                if current_node.left is not None and current_node.right is None:  # Case 2
                    if parent is None:  # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return  # Node found and removed

                if current_node.left is None and current_node.right is not None:  # Case 2
                    if parent is None:  # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return  # Node found and removed

                # Case 3
                # Find successor (leftmost child of right subtree)
                successor = current_node.right
                while successor.left is not None:
                    successor = successor.left
                current_node.key = successor.key  # Copy successor to current node
                parent = current_node
                current_node = current_node.right  # Remove successor from right subtree
                key = parent.key  # Loop continues with new key

            elif current_node.key < key:  # Search right
                parent = current_node
                current_node = current_node.right
            else:  # Search left
                parent = current_node
                current_node = current_node.left

        return  # Node not found

    def find(self, desired_key):
        """Returns the specified key in the tree"""

        if self.is_empty():
            raise ValueError("ValueError exception thrown")

        current_node = self.root
        while current_node is not None:
            if current_node.key == desired_key:
                return current_node.key
            if desired_key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def find_pair_in_tree(self, desired_key):
        """Routine called by add"""
        current_node = self.root
        while current_node is not None:
            if current_node.key == desired_key:
                return current_node
            elif desired_key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def inorder(self):
        """returns list in inorder traversal"""
        inorder_list = []
        self.inorder_helper(self.root, inorder_list)
        return inorder_list

    def inorder_helper(self, vals, inorder_list):
        """recursive routine that returns inorder list"""
        if vals is None:
            return inorder_list
        else:
            self.inorder_helper(vals.left, inorder_list)
            inorder_list.append(vals.key)
            self.inorder_helper(vals.right, inorder_list)
            return inorder_list

    def preorder(self):
        """returns list in preorder traversal"""
        preorder_list = []
        self.preorder_helper(self.root, preorder_list)
        return preorder_list

    def preorder_helper(self, vals, preorder_list):
        """recursive routine that returns preorder list"""
        if vals is None:
            return preorder_list
        else:
            preorder_list.append(vals.key)
            self.preorder_helper(vals.left, preorder_list)
            self.preorder_helper(vals.right, preorder_list)
            return preorder_list

    def postorder(self):
        """returns list in postorder traversal"""
        postorder_list = []
        self.postorder_helper(self.root, postorder_list)
        return postorder_list

    def postorder_helper(self, vals, postorder_list):
        """recursive routine that returns postorder list"""
        if vals is None:
            return postorder_list
        else:
            self.postorder_helper(vals.left, postorder_list)
            self.postorder_helper(vals.right, postorder_list)
            postorder_list.append(vals.key)
            return postorder_list

    def rebalance(self):
        """Routine rebalances tree"""
        lyst = self.inorder()
        self.__init__()
        self.rebalance_helper(lyst)
        return self

    def rebalance_helper(self, lyst):
        """recursive function called by rebalance"""

        if not lyst:
            return None

        center_index = len(lyst) // 2

        root = Node(lyst[center_index])

        self.add_node(root)

        left_list = lyst[:center_index]
        right_list = lyst[center_index + 1:]

        root.left = self.rebalance_helper(left_list)
        root.right = self.rebalance_helper(right_list)
        return root

    def add_node(self, node):
        """given a ---'node'---, add it to the BST"""
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:

                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right
        return self
