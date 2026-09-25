class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        freq_table = defaultdict(int)

        for num in nums:
            freq_table[num] += 1

        
        while k != 0:
            most_frequent = None

            for key in freq_table:
                if (most_frequent == None) or (freq_table[key] > freq_table[most_frequent]):
                    most_frequent = key
            
            del freq_table[most_frequent]
            result.append(most_frequent)
            k -= 1

        return result
