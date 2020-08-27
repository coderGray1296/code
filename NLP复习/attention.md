# attention
注意力模型：对目标数据进行加权变化。人脑的注意力模型，说到底是一种资源分配模型，在某个特定时刻，你的注意力总是集中在画面中的某个焦点部分，而对其它部分视而不见。

从Attention的作用角度出发，我们就可以从两个角度来分类Attention种类：**Spatial Attention 空间注意力**和**Temporal Attention 时间注意力**。更具实际的应用，也可以将Attention分为**Soft Attention和Hard Attention**。Soft Attention是所有的数据都会注意，都会计算出相应的注意力权值，不会设置筛选条件。Hard Attention会在生成注意力权重后筛选掉一部分不符合条件的注意力，让它的注意力权值为0，即可以理解为不再注意这些不符合条件的部分。

## Self-Attention 模型
通过上述对Attention本质思想的梳理，我们可以更容易理解本节介绍的Self Attention模型。Self Attention也经常被称为**intra Attention**（内部Attention），最近一年也获得了比较广泛的使用，比如Google最新的机器翻译模型内部大量采用了Self Attention模型。

在一般任务的Encoder-Decoder框架中，输入Source和输出Target内容是不一样的，比如对于英-中机器翻译来说，Source是英文句子，Target是对应的翻译出的中文句子，Attention机制发生在Target的元素和Source中的所有元素之间。**而Self Attention顾名思义，指的不是Target和Source之间的Attention机制，而是Source内部元素之间或者Target内部元素之间发生的Attention机制，也可以理解为Target=Source这种特殊情况下的注意力计算机制**。其具体计算过程是一样的，只是计算对象发生了变化而已，所以此处不再赘述其计算过程细节。

如果是常规的Target不等于Source情形下的注意力计算，其物理含义正如上文所讲，比如**对于机器翻译来说，本质上是目标语单词和源语单词之间的一种单词对齐机制**。那么如果是Self Attention机制，一个很自然的问题是：通过Self Attention到底学到了哪些规律或者抽取出了哪些特征呢？或者说引入Self Attention有什么增益或者好处呢？我们仍然以机器翻译中的Self Attention来说明，下面两图是可视化地表示Self Attention在同一个英语句子内单词间产生的联系。

![avatar](https://github.com/coderGray1296/code/blob/master/NLP%E5%A4%8D%E4%B9%A0/pictures/attention_1.png)

![avatar](https://github.com/coderGray1296/code/blob/master/NLP%E5%A4%8D%E4%B9%A0/pictures/attention_2.png)

Self Attention可以捕获同一个句子中单词之间的一些**句法特征**（比如图1展示的有一定距离的短语结构）或者**语义特征**（比如图2展示的its的指代对象Law）。

**引入Self Attention后会更容易捕获句子中长距离的相互依赖的特征，因为如果是RNN或者LSTM，需要依次序序列计算，对于远距离的相互依赖的特征，要经过若干时间步步骤的信息累积才能将两者联系起来，而距离越远，有效捕获的可能性越小**。

Self Attention在计算过程中会**直接将句子中任意两个单词的联系通过一个计算步骤直接联系起来，所以远距离依赖特征之间的距离被极大缩短，有利于有效地利用这些特征**。除此外，Self Attention对于增加计算的**并行性**也有直接帮助作用。这是为何Self Attention逐渐被广泛使用的主要原因。
