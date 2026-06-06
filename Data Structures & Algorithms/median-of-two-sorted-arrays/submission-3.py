class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) == 0 and len(nums2) == 0:
            return 0 
        
        if len(nums2) == 0:
            if len(nums1) % 2== 0:
                mid = len(nums1)//2
                return (nums1[mid]+nums1[mid-1])/2
            else:
                mid = len(nums1)//2
                return nums1[mid]
        
        if len(nums1) == 0:
            if len(nums2) % 2== 0:
                mid = len(nums2)//2
                return (nums2[mid]+nums2[mid-1])/2
            
            else:
                mid = len(nums2)//2
                return nums2[mid]

        

        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2

        # Let's firstly decide the partition length 
        # A is the smaller one
        # B is the bigger one 

        total_length = len(A) + len(B)
        left_len = total_length//2


        index_B = left_len - 1
        index_A = -1 # This means no element 

        
        while (index_A + 1) < (len(A)):

            if B[index_B] > A[index_A + 1]:
                    index_A += 1
                    index_B -= 1
            else:
                    break

            
        
        if total_length % 2 == 1:
            if  (index_A + 1) <= (len(A)-1) and ((index_B + 1) <= (len(B)-1)):
                return min(A[index_A+1], B[index_B+1])
        
            elif index_A == len(A)-1:
                return B[index_B+1]
            
            elif index_B == len(B)-1:
                return A[index_A+1]
            
            
        else:
            if index_A >= 0 and index_B >= 0:
                val1 = max(A[index_A],B[index_B])

                if (index_A + 1 < len(A)) and (index_B + 1 < len(B)):
                    val2 = min(A[index_A + 1], B[index_B+1])
                
                elif index_A + 1 == len(A):
                    val2 = B[index_B+1]
                
                elif index_B + 1 == len(B):
                    val2 = A[index_A + 1]
            

            elif index_A < 0:
                val1 = B[index_B]
                if index_B + 1 < len(B):
                    val2 = min(A[index_A + 1], B[index_B+1])
                elif index_B + 1 == len(B):
                    val2 = A[index_A + 1]
                
            elif index_B < 0:
                val1 = A[index_A]
                if index_A + 1 < len(A):
                    val2 = min(A[index_A + 1], B[index_B+1])
                else:
                    val2 = B[index_B+1]


            return (val1 + val2)/2


        

        
    