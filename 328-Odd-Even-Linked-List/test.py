# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # need to store odd end elem, even start elem, 
        # odd linked list, even linked list
        # elem = head;
        odd_head = head;
        even_head = ListNode(head.next.val);
        even_elem = even_head;
        odd_elem = odd_head;
        
        i = 0
        while (odd_elem is not None) and (odd_elem.next is not None):

            # if not the end of the odd elem linked list
            if odd_elem.next.next is not None:
                odd_elem.next = odd_elem.next.next
                odd_elem = odd_elem.next
            else: # only happens at the end of odd elem list (odd_elem.next.next will be none)
                odd_elem.next = None;

            if odd_elem.next is not None:
                even_elem.next = odd_elem.next;
                even_elem = even_elem.next; # for next iteration
            else:
                even_elem.next = None;

        odd_elem.next = even_head;

            # even = even_head;
            # even_list_str = ""
            # print '==== EVEN list  =====' + 'in iteration ' + str(i)
            # while (even.next is not None):
            #     even_list_str = even_list_str + str(even.val) + " => "
            #     even = even.next
            # even_list_str = even_list_str + str(even.val)
            # print even_list_str                


            # odd = head;
            # print '==== ODD list  =====' + 'in iteration ' + str(i)
            # odd_list_str = ""
            # while (odd.next is not None):
            #     odd_list_str = odd_list_str + str(odd.val) + " => "
            #     odd = odd.next
            # odd_list_str = odd_list_str + str(odd.val)
            # print odd_list_str+'\n'


        elem = head;
        print '==== odd even list  =====' 
        elem_list_str = ""
        while (elem.next is not None):
            elem_list_str = elem_list_str + str(elem.val) + " => "
            elem = elem.next
        elem_list_str = elem_list_str + str(elem.val)
        print elem_list_str+'\n'


        # even_elem.next = odd_head;

        # elem = head;
        # while (elem.next is not None):
        # 	elem = elem.next
        # 	print elem.val

a1 = ListNode(1);
a2 = ListNode(2); 
a3 = ListNode(3);
a4 = ListNode(4);
a5 = ListNode(5);
a6 = ListNode(6);
a7 = ListNode(7);
a8 = ListNode(8);
a1.next = a2;
a2.next = a3;
a3.next = a4;
a4.next = a5;
a5.next = a6;
a6.next = a7;
a7.next = a8;

Solution().oddEvenList(a1);
