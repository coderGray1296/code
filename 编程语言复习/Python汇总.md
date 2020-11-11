# Python汇总

### 列出5个python标准库
- os：提供了不少与操作系统相关联的函数
- sys: 通常用于命令行参数
- re: 正则匹配
- math: 数学运算
- datetime:处理日期时间

### 字典如何删除键和合并两个字典
del 和 update 方法

![avatar](https://github.com/coderGray1296/code/blob/master/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%E5%A4%8D%E4%B9%A0/pictures/python_1.jpg)

### 谈下Python的GIL
GIL(Global Interpreter Lock)全局解释锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。

多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大

### fun(🌟args, 🌟🌟args)中的两个参数什么意思？

![avatar](https://github.com/coderGray1296/code/blob/master/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%E5%A4%8D%E4%B9%A0/pictures/python_2.jpg)

![avatar](https://github.com/coderGray1296/code/blob/master/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%E5%A4%8D%E4%B9%A0/pictures/python_3.jpg)

### 简述面向对象中 new 和 init 的区别
init是初始化方法，创建对象后，就立刻被默认调用了，可接收参数。
