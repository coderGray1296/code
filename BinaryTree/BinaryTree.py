class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree():
    '''
    - 创建二叉树，完成
    - 添加元素(广度，先序(带#标示)，前+中，中+后)
    - 广度遍历
    - 深度遍历(先序遍历，中序遍历，后序遍历)递归和非递归
    '''
    def __init__(self):
        self.root = None
        self.queue = [] #用来存放正在操作的三个树节点，分别是root,left和right
        self.create_queue = [] #用来存放先序序列来创建二叉树
        pass

    #通过先序序列创建二叉树，没有左右子节点被标记为'#'
    def createTree(self):
        current = self.create_queue.pop(0)
        if current != '#':
            new_node = Node(current)
            if self.root is None:
                self.root = new_node
            new_node.left = self.createTree()
            new_node.right = self.createTree()
            return new_node
        return None

    #通过前序序列和中序序列创建二叉树
    def create_tree(self, pre_order, mid_order):
        if len(pre_order) == 0:
            return None
        new_node = Node(pre_order[0])
        if self.root is None:
            self.root = new_node
        i = mid_order.index(pre_order[0])
        print(i)
        new_node.left = self.create_tree(pre_order[1:1+i], mid_order[:i])
        new_node.right = self.create_tree(pre_order[1+i:], mid_order[i+1:])
        return new_node

    #通过中序和后序创建二叉树
    def construct_tree(self, mid_order, post_order):
        length = len(post_order)
        if length == 0:
            return None
        new_node = Node(post_order[-1])
        if self.root is None:
            self.root = new_node
        i = mid_order.index(post_order[-1])
        new_node.left = self.construct_tree(mid_order[:i], post_order[:i])
        new_node.right = self.construct_tree(mid_order[i+1:], post_order[length-2-i:length-1])
        return new_node

    #通过层次遍历顺序创建二叉树
    def add(self, val):
        new_node = Node(val)
        self.queue.append(new_node)
        if self.root is None:
            self.root = new_node
        else:
            tree_node = self.queue[0]
            if tree_node.left is None:
                tree_node.left = new_node
            else:
                tree_node.right = new_node
                self.queue.pop(0)

    #通过递归进行先序遍历
    def recursion_vlr(self, root):
        if root is None:
            return
        print(root.val)
        self.recursion_vlr(root.left)
        self.recursion_vlr(root.right)

    #通过栈非递归进行先序遍历
    def pre_order_stack(self, root):
        if root is None:
            return
        mystack = []
        node = root
        while mystack or node:
            while node:
                print(node.val)
                mystack.append(node)
                node = node.left
            node = mystack.pop()
            node = node.right

    #通过递归进行中序遍历
    def recursion_lvr(self, root):
        if root is None:
            return
        self.recursion_lvr(root.left)
        print(root.val)
        self.recursion_lvr(root.right)

    #通过栈非递归进行中序遍历
    def mid_order_stack(self, root):
        if root is None:
            return
        mystack = []
        node = root
        while mystack or node:
            while node:
                mystack.append(node)
                node = node.left
            node = mystack.pop()
            print(node.val)
            node = node.right

    #通过递归进行后序遍历
    def recursion_lrv(self, root):
        if root is None:
            return
        self.recursion_lrv(root.left)
        self.recursion_lrv(root.right)
        print(root.val)

    #通过栈非递归进行后序遍历，先遍历右子树，在遍历左子树，最后逆序数出
    def post_order_stack(self, root):
        if root is None:
            return
        mystack1 = []
        #stack2是为了逆序输出，全都存在2栈中，1栈的作用是按照右、左的顺序遍历节点存入2栈
        mystack2 = []
        node = root
        while mystack1 or node:
            while node:
                mystack2.append(node)
                mystack1.append(node)
                node = node.right
            node = mystack1.pop()
            node = node.left
        while mystack2:
            print(mystack2.pop().val)


    #利用队列进行广度优先遍历BFS
    def level_scan(self):
        queue = []
        current = self.root
        queue.append(current)
        while queue:
            current = queue.pop(0)
            print(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

b = BinaryTree()
#for i in range(1,10):
#    b.add(i)
#b.recursion_vlr(b.root)
#b.level_scan()
#b.create_queue = ['A','B','D','H','#','#','I','#','#','E','#','#','C','F','#','J','#','#','G','#','#']
#b.createTree()
pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
post_order = [7, 4, 2, 5, 8, 6, 3, 1]
#b.create_tree(pre_order, mid_order)
#b.construct_tree(mid_order, post_order)
#b.recursion_vlr(b.root)
#b.pre_order_stack(b.root)
#b.mid_order_stack(b.root)
#b.post_order_stack(b.root)