class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "stop*&^%$#@!"
        return "+_)()".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "stop*&^%$#@!":
            return []
        return s.split("+_)()")