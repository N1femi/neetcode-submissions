class Solution:

    def encode(self, strs: List[str]) -> str:
        seperator = ":;"
        encoded_string = seperator.join(strs)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        seperator = ":;"
        decoded_strs = s.split(seperator)

        if len(s) == 0:
            decoded_strs = []

        return decoded_strs
