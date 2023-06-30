class BinarySearch:
    def binarysearch(self, numberlist, value):
        low = 0
        high = len(numberlist) - 1
        while low <= high:
            mid = (low + high) // 2
            if numberlist[mid] > value:
                high = mid - 1
            elif numberlist[mid] < value:
                low = mid + 1
            else:
                return mid


obj1 = BinarySearch()
print(obj1.binarysearch([1, 2, 3, 4, 5, 6], 3))