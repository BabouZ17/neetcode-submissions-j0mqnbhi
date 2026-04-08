class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temperatures_length = len(temperatures)
        result = [0] * temperatures_length

        stack = temperatures[::-1]

        for i in range(temperatures_length):
        
            current_temp = temperatures[i]
            stack.pop()
            highest_temp = max(stack) if stack else float("-inf")

            if current_temp < highest_temp:
                stack_copy = stack.copy()
                next_temp, nb_of_days = stack_copy.pop(), 1
                while next_temp <= current_temp:
                    next_temp = stack_copy.pop()
                    nb_of_days += 1
                result[i] = nb_of_days
            else:
                result[i] = 0

        return result