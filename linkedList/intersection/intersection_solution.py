# brute force solution
#We can solve this by using a set. We first iterate through the first linked list and put every node in the set.
#We then iterate through the second linked list and check if the node is in the set. If it is, then we return the node.
def intersection(l1, l2):
    nodeSet = set()
    cur = l1

    while cur:
        nodeSet.add(cur)
        cur = cur.next

    cur = l2

    while cur:
        if cur in nodeSet:
            return cur

    return None
