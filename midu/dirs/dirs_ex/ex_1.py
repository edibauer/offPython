#!/usr/bin/python3

def find_sum(nums, goal):
    seen = {}
    for index, value in enumerate(nums):
        diff = goal - value
        if diff in seen:
            return [seen[diff], index]
        seen[value] = index
    return None

if __name__ == "__main__":
    # print("i dont make mistakes")
    # print(find_sum([4,5,6,2], 8))
        ans = find_sum([4,4,2], 8)
        print(ans)