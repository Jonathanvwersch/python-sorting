class Sort:
    def bubble(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)-1-i):
                if arr[j + 1] < arr[j]:
                    arr[j+ 1], arr[j] = arr[j], arr[j + 1]
    def insertion(self, arr):
        for i in range(1, len(arr)):
            while i > 0 and arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] =  arr[i - 1], arr[i]
                i -= 1

    def selection(self, arr):
        for i in range(len(arr)):
            min_index = i

            for j in range(i, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    def quick_sort_not_in_place(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid_index = len(arr) // 2
        mid = [x for x in arr if x == arr[mid_index]]
        left = [x for x in arr if x < arr[mid_index]]
        right = [x for x in arr if x > arr[mid_index]]

        return self.quick_sort_not_in_place(left) + mid + self.quick_sort_not_in_place(right)
    
    def quick_sort(self, arr):
        

    def merge_sort_not_in_place(self, arr):
        def merge(left, right):
            i, j = 0, 0
            merged = []

            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    merged.append(right[j])
                    j += 1
                else:
                    merged.append(left[i])
                    i += 1
            
            if i < len(left):
                merged.extend(left[i:])

            if j < len(right):
                merged.extend(right[j:])

            return merged


        def sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = sort(arr[:mid])
            right = sort(arr[mid:])

            return merge(left, right)


        return sort(arr)
    
    def merge(self, arr):
        
            
            

        

            
            

                    


arr = [5,3,8,3,5,9,1,6]
sorter = Sort()

# sorter.bubble(arr)
# sorter.insertion(arr)
# sorter.selection(arr)
# sorter.quick_sort_not_in_place(arr)
sorted_arr = sorter.merge_sort(arr)

print(arr)
