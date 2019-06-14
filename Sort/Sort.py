class Sort():
    def __init__(self):
        self.heap_len = 0
    '''
    实现各种排序算法
    - 冒泡排序
    - 选择排序
    - 插入排序
    - 希尔排序
    - 快速排序
    - 归并排序
    - 堆排序
    '''
    #冒泡排序
    def BubbleSort(self, arr):
        if len(arr) == 0:
            return arr
        for i in range(0, len(arr)-1):
            for j in range(0, len(arr)-i-1):
                if arr[j+1] < arr[j]:
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp
        return arr
    #选择排序
    def SelectionSort(self, arr):
        if len(arr) == 0:
            return arr
        for i in range(0, len(arr)-1):
            min_index = i
            for j in range(i, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index == i:
                continue
            else:
                temp = arr[i]
                arr[i] = arr[min_index]
                arr[min_index] = temp
        return arr
    #插入排序
    def InsertSort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return arr
        for i in range(1, len(arr)):
            current = arr[i]
            j = i
            while j > 0 and arr[j-1] > current:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = current
        return arr
    #希尔排序
    def ShellSort(self, arr):
        if len(arr) == 0:
            return arr
        increasement = len(arr)
        while increasement > 1:
            #每次缩小增量
            increasement = increasement // 3 + 1
            for i in range(0, increasement):
                #在每个子序列中进行直接插入排序
                for j in range(i + increasement, len(arr), increasement):
                    #相比于直接插入排序，这里增加一个比较，由于增量分组大部分都已有序，可降低复杂度，从而发挥增量分组的优势
                    if arr[j] < arr[j - increasement]:
                        current = arr[j]
                        k = j
                        while k > 0 and arr[k - increasement] > current:
                            arr[k] = arr[k - increasement]
                            k -= increasement
                        arr[k] = current
        return arr
    #快速排序
    def QuickSort(self, arr, start, end):
        if start >= end:
            return
        i = start
        j = end
        baseline = arr[start]
        while i < j:
            while i < j and arr[j] >= baseline:
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1
            while i < j and arr[i] < baseline:
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        arr[i] = baseline
        self.QuickSort(arr, start, i-1)
        self.QuickSort(arr, i+1, end)
        return arr

    #归并排序(2-路分治)
    def MergeSort(self, arr):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return self.merge(self.MergeSort(left), self.MergeSort(right))

    def merge(self, left, right):
        result = []
        length = len(left) + len(right)
        i = 0
        j = 0
        for index in range(0, length):
            if i >= len(left):
                result.append(right[j])
                j += 1
            elif j >= len(right):
                result.append(left[i])
                i += 1
            elif left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        return result

    #堆排序
    def HeapSort(self, arr):
        self.heap_len = len(arr)
        if self.heap_len < 1:
            return arr
        #构建一个最大堆
        self.buildMaxHeap(arr)
        #循环将首位(最大值)与末位交换，然后重新调整最大堆
        while self.heap_len > 0:
            self.swap(arr, 0, self.heap_len - 1)
            self.heap_len -= 1
            self.adjust(arr, 0)
        return arr

    #建立最大堆
    def buildMaxHeap(self, arr):
        #利用完全二叉树的性质，从最后一个非叶子结点开始向上构造最大堆
        for i in range(self.heap_len // 2, -1, -1):
            self.adjust(arr, i)
    #调整使之成为最大堆
    def adjust(self, arr, i):
        maxIndex = i
        #如果有左子树，而且左子树大于父节点，将最大指针指向左子树
        if 2 * i < self.heap_len and arr[2 * i] > arr[maxIndex]:
            maxIndex = 2 * i
        # 如果有右子树，而且右子树大于父节点，将最大指针指向右子树
        if 2 * i + 1 < self.heap_len and arr[2 * i + 1] > arr[maxIndex]:
            maxIndex = 2 * i + 1
        #如果父节点不是最大值，则将父节点与最大值交换，并且递归调整与父节点交换的位置
        if maxIndex != i:
            self.swap(arr, maxIndex, i)
            self.adjust(arr, maxIndex)

    def swap(self, arr, i, j):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp


s = Sort()
print(s.HeapSort([4,2,8,5,0,1]))