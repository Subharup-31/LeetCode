class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ans = []
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        item = list(hashmap.items())
        item.sort(key=lambda x:x[1], reverse = True)

        for key,val in item[:k]:
            ans.append(key)
        
        return ans