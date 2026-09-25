class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        print(s)
        while i < len(s):
            j = s.find("#", i) # Finds '#' and sets j to its index
            print("Found # at:", j)
            length = int(s[i:j])
            print("Length is:", length)
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return result