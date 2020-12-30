# bruteforce solution
#We can solve this by using a set.
#We just iterate through the linked list and check if the current node is in our set (have we already seen this node)?
#If true, then we return the node.
#Otherwise, we add the node to the set and continue iterating.
#If we reach the end of the linked list, then there obviously isn't a cycle and we can return None.

def loopDetection(head):
    seenNodes = set()
    cur = head

    while cur:
        if cur in seenNodes:
            return cur
        else:
            seenNodes.add(cur)
            cur = cur.next
