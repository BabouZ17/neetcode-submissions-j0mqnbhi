from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0

        self.directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }
        self.snake = deque([(0, 0)])
        self.snake_set = {(0, 0)}

    def move(self, direction: str) -> int:
        dr, dc = self.directions[direction]
        head = self.snake[-1]
        new_head = (head[0] + dr, head[1] + dc)
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1

        eating = (self.food_index < len(self.food) and
            new_head == tuple(self.food[self.food_index]))
        if not eating:
            tail = self.snake.popleft()
            self.snake_set.remove(tail)

        if new_head in self.snake_set:
            return -1
        
        self.snake.append(new_head)
        self.snake_set.add(new_head)

        if eating:
            self.food_index += 1
        return len(self.snake) - 1
    

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
