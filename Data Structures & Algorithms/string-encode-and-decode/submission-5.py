class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word
        
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            if (i + 1) < len(s):
                if s[i].isdigit() and s[i + 1] == "#":
                    result.append(s[(i+2):(i+2+int(s[i]))])
                

            i += 1

        print(result)
        return result




