class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        # board
        # score
        # snake len

        # head position
        self.food_ind = 0
        self.food_pos_arr = food
        self.score = 0
        self.q = deque([[0, 0]])
        self.snake_pos = set([(0, 0)])
        self.WIDTH = width
        self.HEIGHT = height

    def move(self, direction: str) -> int:
        dirs = {
            "U": [-1, 0],
            "D": [1, 0],
            "R": [0, 1],
            "L": [0, -1]
        }
        
        head_pos = self.q[-1]

        move_coords = dirs[direction]
        new_pos_c = move_coords[1] + head_pos[1]
        new_pos_r = move_coords[0] + head_pos[0]

        if new_pos_r < 0 or new_pos_r >= self.HEIGHT or new_pos_c < 0 or new_pos_c >= self.WIDTH:
            return -1
        """
        next_pos = (new_pos_r, new_pos_c)
        if next_pos in snake_pos:
            return -1
        """

        next_food_pos = [-1, -1]
        if self.food_ind < len(self.food_pos_arr):
            next_food_pos = self.food_pos_arr[self.food_ind]
        next_pos = [new_pos_r, new_pos_c]
        if next_pos != next_food_pos:
            row, col = self.q.popleft()
            self.q.append(next_pos)
            self.snake_pos.remove((row, col))

            next_pos_t = tuple(next_pos)
            if next_pos_t in self.snake_pos:
                return -1

            self.snake_pos.add(next_pos_t)
        
        else:
            self.q.append(next_pos)
            self.snake_pos.add(tuple(next_pos))
            self.score += 1
            self.food_ind += 1

        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
