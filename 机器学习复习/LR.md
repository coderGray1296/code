### LR (Logistic Regression)
分为两部分：
- 理论推导
- 实际应用

#### 一、逻辑回归简介
逻辑回归（LR,Logistic Regression）是传统机器学习中的一种分类模型，由于LR算法具有简单、高效、易于并行且在线学习（动态扩展）的特点，在工业界具有非常广泛的应用。
>LR属于一种在线学习算法，可以利用新的数据对各个特征的权重进行更新，而不需要重新利用历史数据训练。

**明明是回归，为什么都用于分类问题呢？**
这就要提到线性回归，下面介绍一下线性回归先～
###### 线性回归
概念：对于多维空间中存在的样本点，我们用特征的线性组合（特征加权）去拟合空间中点的分布和轨迹。

有监督训练数据集（X,Y），X表示特征，Y表示标签，w表示该某一特征对应的权重，最终的线性模型如hw(x)所示：

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_1.png)

###### 逻辑回归
线性回归模型既可以用于回归，也可以用于分类。
- 对于回归问题，显而易见就是拟合
- 对于分类问题，则显得有些困难，由于输出的值没有范围，即使使用阈值划分分类区间，也不会有很好的鲁棒性
从而引出引出主角 -- 逻辑回归

>[逻辑回归是假设数据服从Bernoulli分布，因此LR属于参数模型] 后续会对比svm解释何为参数模型

**在线性回归的拟合基础上，我们希望找到一个越阶函数来实现到某个区间内值的映射，从而适应分类任务**

这个函数就是sigmoid：

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_2.png)

有了sigmoid函数之后，取值就在[0,1]之间了，我们也可以将函数值视为类为1的后验概率 p(y=1|x),也就是有一个x，通过sigmoid函数计算出来这个x属于类别1的概率大小。于是自然的，将函数值大于等于0.5的归到类别1，小于0.5的归到类别0
- y = 1, if ϕ(z)>=0.5
- y = 0, otherwise

#### 二、逻辑回归的目标函数及极大似然估计
为了找到w参数权重，需要设定目标函数（cost function）也就是损失函数。第一个想到的就是模仿线性回归的做法，使用误差的平方和作为代价函数，即：

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_3.png)

其中，z(i)=wx(i)+b，i表示第i个样本点，y(i)表示第i个样本的真实值，ϕ(z(i))表示第i个样本的预测值。这时，如果我们将ϕ(z(i))=sigmoid(z(i))代入的话，会发现这是一个非凸函数，这就意味着代价函数有着许多的局部最小值，这不利于我们的求解。

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_4.png)

**那么我们不妨来换一个思路解决这个问题。前面，我们提到了ϕ(z)可以视为类1的后验估计，所以我们有**

- p(y=1|x;w)=ϕ(wx+b)=ϕ(z)
- p(y=0|x;w)=1−ϕ(z)

其中，p(y=1|x;w)表示给定w，那么x点y=1的概率大小。上面两式可以写成一般形式

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_5.png)

接下来我们就要用**极大似然估计**来根据给定的训练集估计出参数w。
>**如何理解逻辑回归与极大似然估计的关系？**最大似然估计就是通过已知结果去反推最大概率导致该结果的参数。极大似然估计是概率论在统计学中的应用，它提供了一种给定观察数据来评估模型参数的方法，即 **“模型已定，参数未知”**，通过若干次试验，观察其结果，利用实验结果得到某个参数值能够使样本出现的概率为最大，则称为极大似然估计。逻辑回归是一种监督式学习，是有训练标签的，就是有已知结果的，从这个已知结果入手，去推导能获得最大概率的结果参数，只要我们得出了这个参数，那我们的模型就自然可以很准确的预测未知的数据了。

因此有：

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_6.png)

为了简化运算，我们对上面这个等式的两边都取一个对数

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_7.png)

我们现在要求的是使得l(w)最大的w。没错，我们的代价函数出现了，我们在l(w)前面加个负号不就变成就最小了吗？不就变成我们代价函数了吗？

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_8.png)

为了更好地理解这个代价函数，我们不妨拿一个例子的来看看

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_9.png)

我们来看看这是一个怎么样的函数

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_10.png)

从图中不难看出，如果样本的值是1的话，估计值ϕ(z)越接近1付出的代价就越小，反之越大；同理，如果样本的值是0的话，估计值ϕ(z)越接近0付出的代价就越小，反之越大。

#### 三、梯度下降求参数
