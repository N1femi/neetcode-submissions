class Solution:

    def encode(self, strs: List[str]) -> str:
        seperator = ":;"
        encoded_string = seperator.join(strs)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        seperator = ":;"
        decoded_strs = s.split(seperator)

        return decoded_strs
