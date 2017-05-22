class BinaryTree:
    def __init__(self, root_id):
        self.left = None
        self.right = None
        self.root_id = root_id

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_node_value(self, value):
        self.root_id = value

    def get_node_value(self):
        return self.root_id

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.right = self.right
            self.right = tree

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            self.left = tree
            tree.left = self.left


def print_tree(tree):
    if tree is not None:
        print_tree(tree.get_left_child())
        print(tree.get_node_value())
        print_tree(tree.get_right_child())


def test_tree():
    my_tree = BinaryTree("Maud")
    my_tree.insert_left("Bob")
    my_tree.insert_right("Tony")
    my_tree.insert_right("Steven")
    print_tree(my_tree)

print('start')
test_tree()

