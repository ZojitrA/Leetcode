class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        thing = []

        def recurz(s="", left=0, right=0):
            if len(s) == 2*n:
                thing.append(s)
                return

            if left < n:

                recurz(s + "(", left + 1, right)

            if right < left:

                recurz(s + ")", left, right +1)

        recurz()
        return thing
