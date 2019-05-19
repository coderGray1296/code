# Longest Common Subsequence（LCS）
## 介绍：给定两个序列X={x0,x1,…,xm-1}，Y={y0,y1,…,yn-1}，求X和Y的一个最长公共子序列
## 例子：
```
X=ABCBDAB，Y=BDCABA
X和Y的最长公共子序列为：BCBA
```
这是一个典型的动态规划问题，当然其他的简单解法肯定有，但是我们这里就是考虑一般的解题步骤，也就是对于动态规划问题的通解。动态规划问题的最优解如果可以由子问题的最优解推导得到，则可以先求解子问题的最优解，再构造原问题的最优解；若子问题有较多的重复出现，则可以自底向上，从最终子问题向原问题逐步求解。
因此子问题的最优解必须包含在整个问题的最优解里面，这一点叫做**满足最优子结构性质**
下面我们考虑本题的解法：通常来说，考虑子问题要自底向上去考虑，因此我们从两个字符串的末端向前考虑，能否将问题拆分为最优子问题。显而易见，从字符串末端来说，每一步的情况有三种：
- 若xi=yj，则	求X0…i-1，Y0…j-1的最长公共子序列Z0…k；	Z0…k+{xi}即结果；
- 否则	求X0…i-1，Y0…j的最长公共子序列Z1;	求X0…i，Y0…j-1的最长公共子序列Z2；	比较Z1和Z2，长度较长的序列即结果；

因此可以拆分为子问题的最优解，终止条件就是当遍历到某一个字符串的0位置也就是开头位置时，终止遍历。
同时动态规划问题需要构建空间表结构，针对这个问题，我们构建原则如下：（图来自网上博客）

```
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l2 or l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

```
这种方法直接判断两个链表当前节点的大小，因为链表当前的节点肯定是在每个链表中val最小的，是后加入的指向别的链表的。
- 如果l1当前的val小于l2当前的val：那么就将l1当前节点的next指向递归(l1.next,l2)的结果，这里递归的理解是已经判断了l1小于l2，但是还需要看l1的next和当前l2的大小，如果l1的next也小于l2那么l2很可能要接在l1.next的后面，具体还要看l1.next.next和l2的大小情况。这种情况是以l1为主链将l2插进来，因此最后要返回l1作为合成链。
- 反之，亦然。

## 总结：
总结起来就是自己对于递归的理解还是比较浅，可能是刚开始刷题的原因，之后遇到此类相似的问题要考虑去构造这种递归的方法，简介快速。