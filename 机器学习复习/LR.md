### LR (Logistic Regression)
分为两部分：
- 理论推导
- 实际应用

#### 一、逻辑回归的本质
逻辑回归（LR,Logistic Regression）是传统机器学习中的一种分类模型，由于LR算法具有简单、高效、易于并行且在线学习（动态扩展）的特点，在工业界具有非常广泛的应用。
>LR属于一种在线学习算法，可以利用新的数据对各个特征的权重进行更新，而不需要重新利用历史数据训练。

**明明是回归，为什么都用于分类问题呢？**
这就要提到线性回归，下面介绍一下线性回归先～
###### 线性回归
概念：对于多维空间中存在的样本点，我们用特征的线性组合（特征加权）去拟合空间中点的分布和轨迹。
有监督训练数据集（X,Y），X表示特征，Y表示标签，w表示该某一特征对应的权重，最终的线性模型如hw(x)所示：





![avatar](https://github.com/coderGray1296/NLP/blob/master/ELMo/pictures/3.jpg)

**ELMo采用了典型的两阶段过程，第一个阶段是利用语言模型进行预训练；第二个阶段是在做下游任务时，从预训练网络中提取对应单词的Word Embedding作为新特征补充道下游任务中。**
使用这个网络结构利用大量语料做语言模型任务就能预先训练好这个网络，如果训练好这个网络后，输入一个新句子Snew，**句子中每个单词都能得到对应的三个Embedding:最底层是单词的 Word Embedding，往上走是第一层双向LSTM中对应单词位置的 Embedding，这层编码单词的句法信息更多一些；再往上走是第二层LSTM中对应单词位置的 Embedding，这层编码单词的语义信息更多一些。**也就是说，ELMO 的预训练过程不仅仅学会单词的 Word Embedding，还学会了一个双层双向的LSTM网络结构，而这两者后面都有用。**很明显ELMo是基于特征的预训练模型**

![avatar](https://github.com/coderGray1296/NLP/blob/master/ELMo/pictures/4.jpg)
![avatar](https://github.com/coderGray1296/NLP/blob/master/ELMo/pictures/5.jpg)

但是ELMo同样存在着不足，LSTM与Transformer比起来提取特征的能力有限，同时，**ELMo采用双向拼接来融合特征的方式，可能会比Bert一体化的融合特征的方式弱一些。**后者并没有验证，只是一种可能性。
