# Rand7求Rand10

首先要知道一个定理：
已知randN()能够生成[1,N]的均匀随机数，那么(randX() - 1) * Y + randY() 就能够生成分布为的[1, X*Y]的均匀随机数，从而实现了randXY

因此我们借鉴这个定理，利用rand7实现rand10，由于要实现rand10，那么我们只需要实现一个rand(10*n) 即实现一个10的倍数的均匀随机分布树即可，然后 rand(10*n) % n + 1就能生成 [1,10]的均匀随机数。

考虑到只能使用rand7，因此我们令randX为rand7，令randY为rand7，就能够生成rand49，然后舍弃掉大于40的均匀随机数，就能够得到rand40，进而得到rand10。

a: rand7() - 1: 0, 1, 2, 3, 4, 5, 6
a*7：0, 7, 14, 21, 28, 35, 42
a*7 + rand7(): [1,2,3,4,5,6,7], [8,9,10,11,12,13,14]...[43,44,45,46,47,48,49]

因此代码如下：
```
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return num % 10 + 1
```
