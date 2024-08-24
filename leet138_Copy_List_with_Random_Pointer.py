# Solution

# // Time Complexity : O(N)
# // Space Complexity : O(N) - Dictionary
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Approach is to go over the linked list and create nodes and random nodes and keep adding them into dictionary
# anytime we are trying to create a node, we can check in dictionary if it is already created.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def buildNextAndRandom(nodeDict,retNode,curNode):
    if curNode.next != None:
        if curNode.next not in nodeDict:
            retNode.next = Node(curNode.next.val)
            nodeDict[curNode.next] = retNode.next
        else:
            retNode.next = nodeDict[curNode.next]
    else:
        retNode.next = None
    
    if curNode.random != None:
        if curNode.random not in nodeDict:
            retNode.random = Node(curNode.random.val)
            nodeDict[curNode.random] = retNode.random
        else:
            retNode.random = nodeDict[curNode.random]
    else:
        retNode.random = None

def copyRandomList(head):
    nodeDict = {}
    
    if head == None:
        return head
    
    curr = head
    retHead = Node(curr.val)
    nodeDict[curr] = retHead

    buildNextAndRandom(nodeDict,retHead,curr)

    curr = head.next
    
    while curr != None:
        newNode = nodeDict[curr]
        
        buildNextAndRandom(nodeDict,newNode,curr)

        curr = curr.next

    return retHead

if __name__ == "__main__":
    # This doesnt run since linked list is not created
    # head = [[1,1],[2,1]]
    # head = [[3,null],[3,0],[3,null]]
    head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    copyRandomList(head)