class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                prev = stack[-1]
                if abs(prev) == abs(a):
                    stack.pop()
                    break
                elif abs(a) > prev:
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(a)

        return stack