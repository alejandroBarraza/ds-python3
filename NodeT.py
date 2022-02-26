class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
                return
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
                return

    def contains(self, value):
        if self.value == value:
            return True

        elif value < self.value:
            if self.left:
                return self.left.contains(value)
            else:
                return False

        else:
            if self.right:
                return self.right.contains(value)
            else:
                return False

    def delete(self, value):
        if self.value == value:
            # we found the value
            # delete lead node
            if not self.left and not self.right:
                return None
            # has left child
            elif not self.right:
                return self.left
            # has right child
            elif not self.left:
                return self.right
            # if has left child ans right child, return the leftest from right tree.
            else:
                current_r_tree = self.right
                while current_r_tree.left:
                    current_r_tree = current_r_tree.left
                # found the min value from the right sub-tree
                self.value = current_r_tree.value
                self.right = self.right.delete(current_r_tree.value)
            return self

        elif value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            else:
                return None
        else:
            if self.right:
                self.right = self.right.delete(value)
            else:
                return None
        return self

    def print_in_order(self):
        # left----> root-----> right
        if self.left:
            self.left.print_in_order()
        print(self.value)
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self):
        # root---> left----> right:
        print(self.value)
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()

    def print_post_order(self):
        # left---> right---->root
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(self.value)
