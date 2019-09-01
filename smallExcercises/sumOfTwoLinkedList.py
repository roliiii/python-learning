# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    if(l1 is None and l2 is None):
      if(c!=0):
        return ListNode(c)
      return None

    if l1 is not None and l2 is not None:
      newNode = ListNode((l1.val + l2.val + c)%10)
      newNode.next = self.addTwoNumbers( l1.next,l2.next, (l1.val+l2.val+c)//10)
      return newNode
    elif l1 is not None:
      newNode = ListNode((l1.val + c)%10)
      newNode.next = self.addTwoNumbers(l1.next,None, (l1.val+c)//10)
      return newNode
    elif l2 is not None:
      newNode = ListNode((l2.val + c)%10)
      newNode.next = self.addTwoNumbers(None, l2.next, (l2.val+c)//10)
      return newNode

l1 = ListNode(9)
l1.next = ListNode(4)
l1.next.next = ListNode(6)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val),
  result = result.next
# 41101