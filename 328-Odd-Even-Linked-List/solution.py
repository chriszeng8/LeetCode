class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # need to store odd end elem, even start elem, 
        # odd linked list, even linked list
        # elem = head;
        if head is None:
            return None
        if head.next is None:
            return head

        odd_head = head;
        even_head = ListNode(head.next.val);
        even_elem = even_head;
        odd_elem = odd_head;
        
        i = 0
        while (odd_elem is not None) and (odd_elem.next is not None):
            # print "odd_elem.next.next"
            # print odd_elem.next.next.val
            if odd_elem.next.next is not None:
                odd_elem.next = odd_elem.next.next
                odd_elem = odd_elem.next
            else:
                odd_elem.next = None;

            # print 'odd_elem.next.val: '+str(odd_elem.next.val)
            # if odd_elem.next exist
            if odd_elem.next is not None:
                even_elem.next = odd_elem.next;
                even_elem = even_elem.next; # for next iteration
            else:
                even_elem.next = None;

        odd_elem.next = even_head;
        return head;