import sys

def add(items):
    nums = [int(i) for i in items]
    return sum(nums)

if __name__ == '__main__':
    print(add(sys.argv[1:]))
