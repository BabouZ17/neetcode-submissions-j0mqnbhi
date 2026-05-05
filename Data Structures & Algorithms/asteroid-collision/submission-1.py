class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = asteroid + stack[-1]
                if diff > 0: # previous is bigger
                    asteroid = 0
                elif diff == 0:
                    asteroid = 0
                    stack.pop()
                else:
                    stack.pop()

            if asteroid:
                stack.append(asteroid)
        return stack