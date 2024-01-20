import random
import time
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BinarySearchTree:
    def add(self, root, value):
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.add(root.left, value)
        else:
            root.right = self.add(root.right, value)
        return root

    def find(self, root, value):
        if root:
            if root.value == value:
                return True
            elif value < root.value:
                return self.find(root.left, value)
            else:
                return self.find(root.right, value)
        return False

    def delete(self, root, value):
        if not root:
            return root
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.getMinValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, root.value)
        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(root.value, end=' ')
            self.printTree(root.right)

class AVLTree:
    def add(self, root, value):
        if not root:
            return TreeNode(value)
        if value < root.value:
            root.left = self.add(root.left, value)
        else:
            root.right = self.add(root.right, value)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        #Left Case
        if balance > 1 and value < root.left.value:
            return self.rightRotate(root)
        #Right Case
        if balance < -1 and value > root.right.value:
            return self.leftRotate(root)
        # Left Right Case
        if balance > 1 and value > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Right Left Case
        if balance < -1 and value < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(root.value, end=' ')
            self.printTree(root.right)


bst = BinarySearchTree()
avl = AVLTree()
root_bst = None
root_avl = None

random_numbers = random.sample(range(10000), 50)


bst_add_time = 0
for value in random_numbers:
    start_time = time.time()
    root_bst = bst.add(root_bst, value)
    bst_add_time += time.time() - start_time


avl_add_time = 0
for value in random_numbers:
    start_time = time.time()
    root_avl = avl.add(root_avl, value)
    avl_add_time += time.time() - start_time

print("BST Add Time: {:.6f} seconds".format(bst_add_time))
print("AVL Add Time: {:.6f} seconds".format(avl_add_time))


print("BST:", end=' ')
bst.printTree(root_bst)
print("\nAVL:", end=' ')
avl.printTree(root_avl)
