class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        self.serial = ""
        seen = [None]

        if not root:
            return ""
        else:
            node = root
        while node :
            
            if node.left and node not in seen:
                self.serial + str(node.val)
                seen.append(node)
                node = node.left
            elif node.right and node not in seen:
                self.serial + str(node.val)
                seen.append(node)
                node = node.right
            else: 
                node = seen.pop()
            if(len(seen) == 0):
               
        
        return self.serial
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
root.left = node2
root.right = node3
node3.left = node4
node3.right = node5

Codec.serialize(Codec,root)
