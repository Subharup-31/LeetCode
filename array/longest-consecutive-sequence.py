class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        longest_length = 0
        #check the hashset
        for i in hashset:
            #check if its a start of a sequence(starting number)
            if i - 1 not in hashset:
                # also length can be set to 0 there will one extra iteration in that way
                length = 1
                while (i + length) in hashset:
                    length += 1
                
                longest_length = max(longest_length,length)
        
        return longest_length