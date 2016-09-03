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
