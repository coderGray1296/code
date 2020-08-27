# attention
注意力模型：对目标数据进行加权变化。人脑的注意力模型，说到底是一种资源分配模型，在某个特定时刻，你的注意力总是集中在画面中的某个焦点部分，而对其它部分视而不见。

从Attention的作用角度出发，我们就可以从两个角度来分类Attention种类：**Spatial Attention 空间注意力**和**Temporal Attention 时间注意力**。更具实际的应用，也可以将Attention分为**Soft Attention和Hard Attention**。Soft Attention是所有的数据都会注意，都会计算出相应的注意力权值，不会设置筛选条件。Hard Attention会在生成注意力权重后筛选掉一部分不符合条件的注意力，让它的注意力权值为0，即可以理解为不再注意这些不符合条件的部分。
