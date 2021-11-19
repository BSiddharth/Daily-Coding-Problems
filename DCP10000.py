from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        candDict = {}
        currentCand = candidates[0]
        currentRange = [0]
        for x in range(len(candidates)):
            if candidates[x] != currentCand:
                currentRange.append(x-1)
                candDict[currentCand] = currentRange
                currentCand = candidates[x]
                currentRange = [x]     
        currentRange.append(len(candidates)-1)
        candDict[candidates[-1]] = currentRange
        print(candDict)
        result = []
        def helper(i,currentList,currentSum):
            if currentSum == target:
                print('adding',currentList)
                result.append(currentList.copy())
                return
            if i >= len(candidates) or currentSum > target:
                print('no no')
                return
            print('looking at index',i,':',candidates[i])
            
            # if currentSum + candidates[i] <= target:
            start = candDict[candidates[i]][0]
            print('start is',start)
            end = candDict[candidates[i]][1]
            print('end is',end)
            copyList = currentList.copy()
            for x in range(end-start+1):
                copyList.append(candidates[i])
                print('helper for',end+1,copyList,currentSum + (x+1)*candidates[i])
                helper(end+1,copyList,currentSum + (x+1)*candidates[i])
            # copyList.append(candidates[i])
            # helper(i+1,copyList,currentSum + candidates[i])
            
            copyList = currentList.copy()
            print('helper for',end+1,copyList,currentSum)
            helper(end+1,copyList,currentSum)
            
        helper(0,[],0)
        return result

s = Solution()
print(s.combinationSum2([1,2,2,2,2,2,2,5],5))