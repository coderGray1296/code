class Sort():
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



s = Sort()
print(s.ShellSort([4,2,8,0,5,1]))