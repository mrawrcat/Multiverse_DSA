'''
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.

Constraints:

The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node.

Psuedocode planning

To remove a node from the linked list we should first find our node by iterating through the
linkedList to find the node we are deleting. When we find our node, we assign the next of
the previous node to the next of the node after our current node.

In the context of this problem we cannot delete this specific node. we are given the node
but not the head of the list so we cannot iterate (search) through the list and do not know 
the previous node to make the previous node's next the next node.
We only know this node and the next (succeding) nodes .
To "remove" the current node, we basically replace this node's next and value to the next
node so that this node becomes the next node and points to the node after the next node.

To do this we change this node's value and next to be the next node's value and next.
If we want to remove the next node for garbage collection
we set the next node's next to None/Null
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        # set this node's value to next node's value
        node.val = node.next.val
        # set this node's next to next node's next
        node.next = node.next.next
        # if we want to garbage collect set next node's next to None
        node.next.next = None
