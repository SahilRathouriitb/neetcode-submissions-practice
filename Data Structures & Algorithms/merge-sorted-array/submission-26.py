class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m,len(nums1)):
            nums1[i] = None

        i = 0
        j = 0
        while j < n:
            if nums1[i] == None:
                nums1[i] = nums2[j]
                i += 1
                j += 1

            elif nums1[i] >= nums2[j]:
                # here j will take that place
                self.shift_nums1(nums1, i)
                nums1[i] = nums2[j]
                i += 1
                j += 1
            
            elif nums1[i] < nums2[j]:
                i = i+1 
        
        print(nums1)

    def shift_nums1(self,nums1, start_index):
        k = 0
        for i in range(start_index, len(nums1)):
            store_i = nums1[i]
            nums1[i] = k
            k = store_i
            
