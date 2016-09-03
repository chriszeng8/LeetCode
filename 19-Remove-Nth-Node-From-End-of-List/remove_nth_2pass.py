# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        

# Create a singly-linked list        
import random;
a,b=1,100;
NodeSize = 1;
NodeList = [];

head = ListNode(random.randint(a, b));

for i in range(NodeSize):
	NodeList.append(ListNode(random.randint(a, b)));

# print NodeList[0].val
print [head.val,[NodeList[i].val for i in range(NodeSize)]]

head.next = NodeList[0]
for i in range(NodeSize-1):
	NodeList[i].next = NodeList[i+1]

tempNode = head
for i in range(NodeSize+1):
	# print tempNode.val
	tempNode = tempNode.next



class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # count how many elements in a linked list
        elem = head
        counter = 1
        while (elem.next!=None):
        	# print str(counter)+' : '+str(elem.val)
        	counter = counter+1;
        	elem = elem.next;
        # print "counter: "+str(counter)

        elem2 = head
        if (counter == n):
        	head = elem2.next
        	return head

        for i in range(counter-n-1):
        	elem2 = elem2.next
        	# print "i:" + str(i)
        elem3 = elem2.next.next
        elem2.next = elem3

        # print "elem.val: " + str(elem2.val)
        # print "elem3.val: " + str(elem3.val)

        new_elem = head
        while new_elem.next:
        	# print new_elem.val
        	new_elem = new_elem.next
        return head

head2a = ListNode(1)
head2b = ListNode(2)
head2a.next= head2b

new_head = Solution().removeNthFromEnd(head2a,2)
elem = new_head
elem_list = [new_head.val]
while elem.next:
	elem_list.append(elem.next.val)
	elem = elem.next
print elem_list
