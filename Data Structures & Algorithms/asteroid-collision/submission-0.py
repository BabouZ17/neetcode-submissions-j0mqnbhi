class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] # asteroid, direction
        for asteroid in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid): # previous smaller
                    stack.pop()
                elif stack[-1] == abs(asteroid): # both destroyed
                    stack.pop()
                    alive = False
                else: # previous bigger keep it and skip current
                    alive = False
            if alive:
                stack.append(asteroid)
                
        return stack