class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = len(nums1) - 1
        index1 = m-1 
        index2 = n-1
        if index1 == (- 1):
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            print(nums1)
            return 
        while (index2 >=0):
            if nums1[index1] > nums2[index2]:
                nums1[last] = nums1[index1]
                last = last - 1
                index1 -= 1

            elif nums1[index1] <= nums2[index2]:
                nums1[last] = nums2[index2]
                last -= 1
                index2 -= 1
            print(index1)
            if index2 >= 0 and index1 == -1:
                for i in range(0, index2+1):
                    nums1[i] = nums2[i]
                break
        
        print(nums1)
        
