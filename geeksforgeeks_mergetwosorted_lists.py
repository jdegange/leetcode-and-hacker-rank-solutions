#Clean Node-wise solution

# Python3 program to merge two 
# sorted linked lists in-place. 
import math 

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# Function to create newNode in a linkedlist 
def newNode( key): 
	temp = Node(key) 
	temp.data = key 
	temp.next = None
	return temp 

# A utility function to print linked list 
def printList( node): 
	while (node != None): 
		print(node.data, end = " ") 
		node = node.next

# Merges two given lists in-place. 
# This function mainly compares 
# head nodes and calls mergeUtil() 
def merge( h1, h2): 
	if (h1 == None): 
		return h2 
	if (h2 == None): 
		return h1 

	# start with the linked list 
	# whose head data is the least 
	if (h1.data < h2.data): 
		h1.next = merge(h1.next, h2) 
		return h1 
	
	else: 
		h2.next = merge(h1, h2.next) 
		return h2 
	
# Driver Code 
if __name__=='__main__': 
	head1 = newNode(1) 
	head1.next = newNode(3) 
	head1.next.next = newNode(5) 

	# 1.3.5 LinkedList created 
	head2 = newNode(0) 
	head2.next = newNode(2) 
	head2.next.next = newNode(4) 

	# 0.2.4 LinkedList created
     
	mergedhead = merge(head1, head2) 

	printList(mergedhead)
# This code is contributed by Srathore 
