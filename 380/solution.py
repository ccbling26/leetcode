import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.data = {}

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        del_idx = self.data[val]
        last_idx = len(self.nums) - 1
        self.data[self.nums[last_idx]] = del_idx
        self.nums[del_idx] = self.nums[last_idx]
        del self.data[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()