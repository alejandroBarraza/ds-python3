from NodeT import Node


class BST:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def print_in_oder(self):
        if self.root:
            return self.root.print_in_order()
        else:
            print("no hay nodos")
            return False

    def print_pre_order(self):
        if self.root:
            self.root.print_pre_order()
        else:
            print("not values to print")
            return None

    def print_post_order(self):
        if self.root:
            self.root.print_post_order()
        else:
            print("not values to print")
            return None

    def contains(self, value):
        if self.root:
            return self.root.contains(value)

        else:
            print("valor no encontrado")
            return False

    def delete(self, value):
        if self.root:
            self.root = self.root.delete(value)
        else:
            return None
