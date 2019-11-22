def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        current1=0
        current2=0
        temp = []
        nums1.sort()
        nums2.sort()
        while current1<len(nums1) and current2 <len(nums2):
            if nums1[current1] == nums2[current2]:
                temp.append(nums1[current1])
                current1 += 1
                current2 += 1
            elif nums1[current1] < nums2[current2]:
                current1+=1
            elif nums1[current1]>nums2[current2]:
                current2 += 1
        
        return temp
