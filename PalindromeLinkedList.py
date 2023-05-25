class ListNode:
    def __init__(self, val=0, next_reserved=None):
        self.val=val
        self.next=next_reserved

class Solution:

    def __init__(self):
        self.endIndex = None

    def isPalindrome(self, head: ListNode):
        ####Need 3 base cases
        #Only 1 provided
        if head is None or head.next is None:
            return True
        #Only 2 provided
        if head.next.next is None:
            return head.val == head.next.val
        #Only 3 provided
        if head.next.next.next is None:
            return head.val == head.next.next.val

        self.endIndex = head.next

        valid = True 
        try:
            self.__helper__(head)
        except Exception:
            valid = False
        return valid 
        
    def __helper__(self,subList: ListNode):
        #Recurse until you reach mid point
        if self.endIndex.next is not None and self.endIndex.next.next is not None:
            self.endIndex = self.endIndex.next.next
            closingNode = self.__helper__(subList.next)
        else:
            #Mid point reached. 2 scenarios
            if self.endIndex.next is not None:
                #Odd number
                if subList.val == subList.next.next.val:
                    return subList.next.next.next
            if self.endIndex.next is None:
                #Even number
                if subList.val == subList.next.val:
                    return subList.next.next
            raise Exception()

        if closingNode.val == subList.val:
            return closingNode.next
        else:
            raise Exception()

import unittest

def generateFromList(valArray):
    if len(valArray) == 0:
        return None
    head = root = ListNode(valArray[0])
    for i in valArray[1:]:
        head.next = ListNode(i)
        head = head.next
    return root

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_even(self):
        self.assertTrue(self.solution.isPalindrome(generateFromList([1,2,3,4,5,5,4,3,2,1])))
    def test_odd(self):
        self.assertTrue(self.solution.isPalindrome(generateFromList([1,2,3,4,3,2,1])))
    def test_even_4(self):
        self.assertTrue(self.solution.isPalindrome(generateFromList([1,2,2,1])))
    def test_even_2(self):
        self.assertTrue(self.solution.isPalindrome(generateFromList([1,1])))
    def test_odd_3(self):
        self.assertTrue(self.solution.isPalindrome(generateFromList([1,2,1])))
    def test_odd_1(self):
        self.assertTrue(self.solution.isPalindrome(generateFromList([1])))
    def test_empty(self):
        self.assertTrue(self.solution.isPalindrome(generateFromList([])))
    def test_not_odd_3(self):
        self.assertFalse(self.solution.isPalindrome(generateFromList([1,2,3])))
    def test_not_even_2(self):
        self.assertFalse(self.solution.isPalindrome(generateFromList([1,2])))
    def test_not_odd(self):
        self.assertFalse(self.solution.isPalindrome(generateFromList([1,2,3,4,5,9,3,2,1])))
    def test_not_even(self):
        self.assertFalse(self.solution.isPalindrome(generateFromList([1,2,3,4,5,5,4,3,333,1])))


if __name__== "__main__":
    unittest.main()
