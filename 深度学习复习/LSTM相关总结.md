### RNN LSTM GRU

##### RNN
一般的RNN结构如下图所示，是一种将以往学习的结果应用到当前学习的模型，但是这种一般的RNN存在着许多的弊端。举个例子，如果我们要预测“the clouds are in the sky”的最后一个单词，因为只在这一个句子的语境中进行预测，那么将很容易地预测出是这个单词是sky。在这样的场景中，相关的信息和预测的词位置之间的间隔是非常小的，RNN 可以学会使用先前的信息。

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_1.png)
![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_2.png)

标准的RNN结构中只有一个神经元，一个tanh层进行重复的学习，这样会存在一些弊端。例如，在比较长的环境中，例如在“I grew up in France… I speak fluent French”中去预测最后的French，那么模型会推荐一种语言的名字，但是预测具体是哪一种语言时就需要用到很远以前的France，这就说明在长环境中相关的信息和预测的词之间的间隔可以是非常长的。在理论上，RNN 绝对可以处理这样的长环境问题。人们可以仔细挑选参数来解决这类问题中的最初级形式，但在实践中，RNN 并不能够成功学习到这些知识。然而，LSTM模型就可以解决这一问题。


##### LSTM

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_3.png)

如图所示，标准LSTM模型是一种特殊的RNN类型，在每一个重复的模块中有四个特殊的结构，以一种特殊的方式进行交互。在图中，每一条黑线传输着一整个向量，粉色的圈代表一种pointwise 操作(将定义域上的每一点的函数值分别进行运算)，诸如向量的和，而黄色的矩阵就是学习到的神经网络层。

LSTM模型的核心思想是“细胞状态”。“细胞状态”类似于传送带。直接在整个链上运行，只有一些少量的线性交互。信息在上面流传保持不变会很容易。

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_4.png)

LSTM 有通过精心设计的称作为“门”的结构来去除或者增加信息到细胞状态的能力。门是一种让信息选择式通过的方法。他们包含一个 sigmoid 神经网络层和一个 pointwise 乘法操作。

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_5.png)

Sigmoid 层输出 0 到 1 之间的数值，描述每个部分有多少量可以通过。0 代表“不许任何量通过”，1 就指“允许任意量通过”。LSTM 拥有三个门，来保护和控制细胞状态。

可以分成四步完成：

**第一步**

在LSTM模型中，第一步是**决定我们从“细胞”中丢弃什么信息**，这个操作由一个忘记门层来完成。该层读取当前输入x和前神经元信息h，由ft来决定丢弃的信息。输出结果1表示“完全保留”，0 表示“完全舍弃”。

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_6.png)

**第二步**

第二步是确定细胞状态所存放的新信息，这一步由两层组成。sigmoid层作为“输入门层”，**决定我们将要更新的值i**；tanh层来创建一个新的候选值向量~Ct加入到状态中。在语言模型的例子中，我们希望增加新的主语到细胞状态中，来替代旧的需要忘记的主语。

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_7.png)

**第三步**

第三步就是更新旧细胞的状态，将Ct-1更新为Ct。我们把旧状态与 ft相乘，丢弃掉我们确定需要丢弃的信息。接着加上 it * ~Ct。这就是新的候选值，根据我们决定更新每个状态的程度进行变化。在语言模型的例子中，这就是我们实际根据前面确定的目标，丢弃旧代词的信息并添加新的信息的地方。

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_8.png)

**第四步**

最后一步就是确定输出了，这个输出将会基于我们的细胞状态，但是也是一个过滤后的版本。首先，我们**运行一个 sigmoid 层来确定细胞状态的哪个部分将输出出去**。接着，我们把细胞状态通过 tanh 进行处理（得到一个在 -1 到 1 之间的值）并将它和 sigmoid 门的输出相乘，最终我们仅仅会输出我们确定输出的那部分。在语言模型的例子中，因为语境中有一个代词，可能需要输出与之相关的信息。例如，输出判断是一个动词，那么我们需要根据代词是单数还是负数，进行动词的词形变化。

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_9.png)

##### GRU（Gated Recurrent Unit，LSTM变体）

![avatar](https://github.com/coderGray1296/code/blob/master/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A4%8D%E4%B9%A0/pictures/LSTM_10.png)

GRU作为LSTM的一种变体，将忘记门和输入门合成了一个单一的更新门。同样还混合了细胞状态和隐藏状态，加诸其他一些改动。最终的模型比标准的 LSTM 模型要简单，也是非常流行的变体。
