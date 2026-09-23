class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        xInd = None
        while l < r:
            mid = (l + r) // 2
            if arr[mid] == x:
                xInd = mid
                break
            elif x > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1

        if not xInd:
            xInd = l

        if arr[xInd] < x and xInd + 1 < len(arr):
            xInd += 1


        left, right = xInd - 1, xInd
        while right - left + 1 < k + 2:
            if left < 0:
                right += 1
                continue
            elif right > len(arr) - 1:
                left -= 1
                continue

            if abs(arr[right] - x) < abs(arr[left] - x):
                right += 1
            else:
                left -= 1
        

        return arr[left+1:right]