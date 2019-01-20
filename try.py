class treeNode:
    def __init__(self, val):
        self.val = val
        self.next = next
    
    def preDFS(root):
        if not root:
            return
        print(root.val)
        preDFS(root.left)
        preDFS(root.right)

    def preDFS(root):
        if not root:
            return
        stack = []
        ptr = root
        while stack or root:
            if ptr:
                print(ptr.val)
                stack.append(ptr)
                ptr = ptr.left
            else:
                ptr = stack.pop()
                ptr = ptr.right
                
step 1

step 2