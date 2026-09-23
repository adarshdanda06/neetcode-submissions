class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the element x's ind
        # binary search
        # left, right ptr

        # while arrCount < k:

        # if left isnt inbound
            # add right ind
            # continue

        # elif right isnt inbound
            # increment right ind
            # continue

        # if both inbound
            # left < right
            # sub left ind

            # right < left
            # add right ind

            # if equal -> choose the val based on condition

        # iter through the left to right and add all the elems there

        # return arr

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

        print(xInd)
        print(arr[xInd])
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