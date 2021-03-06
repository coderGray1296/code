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

**在线性回归的拟合基础上，我们希望找到一个越阶函数来实现到某个区间内值的映射，从而适应分类任务，将分类任务的真实标记y与线性回归模型的预测值联系起来**

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
在开始梯度下降之前，要这里插一句，sigmoid function有一个很好的性质就是：
ϕ′(z)=ϕ(z)(1−ϕ(z))

还有，我们要明确一点，梯度的负方向就是代价函数下降最快的方向。什么？为什么？好，我来说明一下。借助于泰特展开，我们有
f(x+δ)−f(x)≈f′(x)⋅δ

其中，f′(x)和δ为向量，那么这两者的内积就等于f′(x)⋅δ=||f′(x)||⋅||δ||⋅cosθ

当θ=π时，也就是δ在f′(x)的负方向上时，取得最小值，也就是下降的最快的方向了~

w:=w+Δw, Δw=−η∇J(w) == wj:=wj+Δwj, Δwj=−η∂J(w)/∂wj

其中，wj表示第j个特征的权重；η为学习率，用来控制步长。其中的重点如下：

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_11.png)

其中代价函数同上：

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_8.png)

所以，在使用梯度下降法更新权重时，只要根据下式即可wj:=wj+η∑(y(i)−ϕ(z(i)))x(i)j

当然，在样本量极大的时候，每次更新权重会非常耗费时间，这时可以采用随机梯度下降法，这时每次迭代时需要将样本重新打乱，然后用下式不断更新权重。也就是去掉了求和，而是针对每个样本点都进行更新。

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_12.png)

#### 四、实战使用
Python的伪代码如下(对n个样本实现向量化)：
```
Z  = np.dot(w.T,x) + b
A = sigmoid(Z)
dZ = A - Y
dw = 1/m * X * dZ.T
db = 1/m * np.sum(dZ)
w = w - a*dw
b = b - a*db
```
**一般业界直接使用sklearn中的logstic regression进行训练**

#### 五、面试常见
1. **为什么要使用sigmoid函数作为假设？**
因为线性回归模型的预测值为实数，而样本的类标记为（0,1），我们需要将分类任务的真实标记y与线性回归模型的预测值联系起来，也就是找到广义线性模型中的联系函数。如果选择**单位阶跃函数**（x<0:0 x=1/2:1/2 x>0:1）的话，它是不连续的不可微。而如果选择sigmoid函数，它是连续的，而且能够将z转化为一个接近0或1的值。

2. **逻辑回归的优缺点**
优点：**形式简单，模型的可解释性非常好**，特征的权重可以看到不同的特征对最后结果的影响。**除了类别，还能得到近似概率预测**，这对许多需利用概率辅助决策的任务很有用。**对率函数是任意阶可导的凸函数，有很好的数学性质**。缺点：**准确率不是很高**，因为形势非常的简单，很难去拟合数据的真实分布。**本身无法筛选特征**，有时会用gbdt来筛选特征，然后再上逻辑回归。**处理非线性数据较麻烦**，逻辑回归在不引入其他方法的情况下，只能处理线性可分的数据，或者进一步说，处理二分类的问题 。

3. **三种梯度下降方法的选择**
**批量梯度下降BGD（Batch Gradient Descent）**：优点：会获得全局最优解，易于并行实现。缺点：更新每个参数时需要遍历所有的数据，计算量会很大并且有很多的冗余计算，导致当数据量大的时候每个参数的更新都会很慢。**随机梯度下降SGD**：优点：训练速度快；缺点：准确率下降，并不是全局最优，不易于并行实现。它的具体思路是更新每一个参数时都是用一个样本来更新。（以高方差频繁更新，优点是使得sgd会跳到新的和潜在更好的局部最优解，缺点是使得收敛到局部最优解的过程更加的复杂。）**small batch梯度下降**：结合了上述两点的优点，每次更新参数时仅使用一部分样本，减少了参数更新的次数，可以达到更加稳定的结果，一般在深度学习中采用这种方法。

4. **LR模型的优化，加入正则项** 当模型的参数过多时，很容易遇到过拟合的问题。这时就需要有一种方法来控制模型的复杂度，典型的做法在优化目标中加入正则项，通过惩罚过大的参数来防止过拟合。引入正则项的LR目标函数： ![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_13.png)
一般情况下，取p=1或p=2，分别对应L1，L2正则化，两者的区别可以从下图中看出来，L1正则化（左图）倾向于使参数变为0，因此能产生稀疏解。如果是圆，则很容易切到圆周的任意一点，但是很难切到坐标轴上，这样就得不出稀疏的解，冗余数据就会相对较多!但如果是菱形或者多边形，则很容易切到坐标轴上，因此很容易产生稀疏的结果 ![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_14.png)
**实际应用时，由于我们数据的维度可能非常高，L1正则化因为能产生稀疏解，使用的更为广泛一些。** [LR正则总结](https://www.cnblogs.com/pinard/p/6035872.html)

5. **LR如何解决多分类问题？** 简言之，把Sigmoid函数换成softmax函数，即可适用于多分类的场景。
Softmax 回归是直接对逻辑回归在多分类的推广，相应的模型也可以叫做多元逻辑回归（Multinomial Logistic Regression）。有以下的概率分布和损失函数：![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_15.png)![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_16.png)

6. **LR如何解决线形不可分问题？** 逻辑回归本质上是一个线性模型，但是，这不意味着只有线性可分的数据能通过LR求解，实际上，我们可以通过2种方式帮助LR实现：1. 利用特殊核函数，对特征进行变换：把低维空间转换到高维空间，而在低维空间不可分的数据，到高维空间中线性可分的几率会高一些。2. 扩展LR算法，提出FM算法。

7. **LR为什么要对连续数值特征进行离散化？** 1. 离散化后的特征对异常数据有很强的鲁棒性：比如一个特征是年龄>30是1，否则0。如果特征没有离散化，一个异常数据“年龄300岁”会给模型造成很大的干扰；2.逻辑回归属于广义线性模型，表达能力受限；单变量离散化为N个后，每个变量有单独的权重，相当于为模型引入了非线性，能够提升模型表达能力，加大拟合；3.离散化后可以进行特征交叉，由M+N个变量变为M*N个变量，进一步引入非线性，提升表达能力；4.特征离散化后，模型会更稳定，比如如果对用户年龄离散化，20-30作为一个区间，不会因为一个用户年龄长了一岁就变成一个完全不同的人。当然处于区间相邻处的样本会刚好相反，所以怎么划分区间是门学问；

8. **什么是参数模型（LR）与非参数模型（SVM）？** 在统计学中，参数模型通常假设总体（随机变量）服从某一个分布，该分布由一些参数确定（比如正太分布由均值和方差确定），在此基础上构建的模型称为参数模型；非参数模型对于总体的分布不做任何假设，只是知道总体是一个随机变量，其分布是存在的（分布中也可能存在参数），但是无法知道其分布的形式，更不知道分布的相关参数，只有在给定一些样本的条件下，能够依据非参数统计的方法进行推断。

9. **LR与SVM的联系与区别：** **联系**：1、LR和SVM都可以处理分类问题，且一般都用于处理线性二分类问题（在改进的情况下可以处理多分类问题）2、两个方法都可以增加不同的正则化项，如l1、l2等等。所以在很多实验中，两种算法的结果是很接近的。**区别**：1、LR是参数模型[逻辑回归是假设y服从Bernoulli分布]，SVM是非参数模型，LR对异常值更敏感。2、从目标函数来看，区别在于逻辑回归采用的是logistical loss，SVM采用的是hinge loss，这两个损失函数的目的都是增加对分类影响较大的数据点的权重，减少与分类关系较小的数据点的权重。3、SVM的处理方法是只考虑support vectors，也就是和分类最相关的少数点，去学习分类器。而逻辑回归通过非线性映射，大大减小了离分类平面较远的点的权重，相对提升了与分类最相关的数据点的权重。4、逻辑回归相对来说模型更简单，好理解，特别是大规模线性分类时比较方便。而SVM的理解和优化相对来说复杂一些，SVM转化为对偶问题后,分类只需要计算与少数几个支持向量的距离,这个在进行复杂核函数计算时优势很明显,能够大大简化模型和计算。5、logic 能做的 svm能做，但可能在准确率上有问题，svm能做的logic有的做不了。

10. **如何选择LR与SVM？** 1、如果Feature的数量很大，跟样本数量差不多，这时候选用LR或者是Linear Kernel的SVM
2、如果Feature的数量比较小，样本数量一般，不算大也不算小，选用SVM+Gaussian Kernel3、如果Feature的数量比较小，而样本数量很多，需要手工添加一些feature变成第一种情况。**模型复杂度**：SVM支持核函数，可处理线性非线性问题;LR模型简单，训练速度快，适合处理线性问题;决策树容易过拟合，需要进行剪枝 **损失函数**：SVM hinge loss; LR L2正则化; adaboost 指数损失 **数据敏感度**：SVM添加容忍度对outlier不敏感，只关心支持向量，且需要先做归一化; LR对远点敏感 **数据量**：数据量大就用LR，数据量小且特征少就用SVM非线性核

11. **样本不均衡的解决办法---采样** 下采样，对于一个不均衡的数据，让目标值(如0和1分类)中的样本数据量相同，且以数据量少的一方的样本数量为准。上采样就是以数据量多的一方的样本数量为标准，把样本数量较少的类的样本数量生成和样本数量多的一方相同，称为上采样。**SMOTE人工合成数据**， SMOTE算法的基本思想是对少数类样本进行分析并根据少数类样本人工合成新样本添加到数据集中，算法流程如下： 1. 对于少数类中的每一个样本xx，用欧式距离为标准计算它到少数类样本集SminSmin中所有样本的距离，得到其k近邻 2. 确定采样倍率NN,对于每一个少数类样本xx,从其k近邻中随机选择若干个样本，假设选择的近邻为x^x^ 3. 对于每一个随机选出的近邻x^x^，分别与原样本按照如下的公式构建新的样本 xnew=x+rand(0,1)∗(x^−x) 欧式距离和曼哈顿距离公式如下![avatar](https://github.com/coderGray1296/code/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/lr_17.png)
