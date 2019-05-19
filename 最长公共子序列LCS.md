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
![avatar](https://github.com/coderGray1296/code/blob/master/pictures/LCS.png?raw=true)
图片中的箭头表示的是三种情况，左上表示xi=yi；上表示Z2>Z1；左表示Z1>Z2。我们的程序中则考虑将这三种情况保存在一个一个空间矩阵中，0为第一种情况，1为Z1>Z2，2为Z2>=Z1，**注意这个等号放在情况2还是情况3，将影响我们的结果**，代码之后会分析
图中的数字就是最长的长度记录，用C[i][j]来表示吧！～具体的看代码：
```
class Solution(object):
    def LCS(self, X, Y):
        size_x = len(X)
        size_y = len(Y)
        c = np.zeros((size_x + 1, size_y + 1), dtype=int)
        flag = np.zeros((size_x + 1, size_y + 1), dtype=int)
        for i in range(1, size_x+1):
            for j in range(1, size_y+1):
                if X[i-1] == Y[j-1]:
                    c[i][j] = c[i-1][j-1] + 1
                    flag[i][j] = 0
                elif c[i][j-1] < c[i-1][j]:
                    c[i][j] = c[i-1][j]
                    flag[i][j] = 1
                else:
                    c[i][j] = c[i][j-1]
                    flag[i][j] = 2
        self.get_char(size_x, size_y, flag, X)

    def get_char(self, i, j, flag, X):
        if i == 0 or j == 0:
            return 1
        if flag[i][j] == 0:
            self.get_char(i-1, j-1, flag, X)
            print(X[i-1])
        elif flag[i][j] == 1:
            self.get_char(i-1, j, flag, X)
        else:
            self.get_char(i, j-1, flag, X)
        return 1
```
结果如下：
```
B
D
A
B
```
看我们的结果，BDAB确实成立，但是我们看开头的例子结果确实BCBA也是成立的，这个原因就在于之前说的**等号取在哪个情况**。由于这个问题较为特殊，从最后一个字符开始，B不等于A因此比较Z1和Z2，发现Z1=Z2（当然这是递归的过程程序并不知道，我们马后炮一下）。而我们的标准将它定为情况3，所以取Z1，因此相当于按照X优先取的，所以结果不一样。
