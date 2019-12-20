class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[0:n] = nums2[:]
            return
        if n == 0:
            return

        if nums2[0] >= nums1[m - 1]:
            for i in range(n):
                nums1[m + i] = nums2[i]
            return

        for i in range(n):
            j = m + i - 1

            while j >= 0:
                if nums2[i] < nums1[j]:
                    nums1[j + 1], nums1[j] = nums1[j], nums2[i]
                    j -= 1
                else:
                    nums1[j + 1] = nums2[i]
                    break
