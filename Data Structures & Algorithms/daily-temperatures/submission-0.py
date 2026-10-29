class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        #Brute Force
        for i in range(len(temperatures)):
            count = 0
            for j in range(i, len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    count = j - i
                    break
            
            result.append(count)

        
        return result


        