# https://www.hackerrank.com/challenges/python-lists

if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(0,N):
        cmd = input().split()
        {
              'insert': 
                lambda: 
                    list.insert(int(cmd[1]), int(cmd[2])),
              'print': 
                lambda:
                    print(list),
              'remove': 
                lambda:
                    list.remove(int(cmd[1])),
              'append': 
                lambda:
                    list.append(int(cmd[1])),
              'sort': 
                lambda:
                    list.sort(),
              'pop': 
                lambda:
                    list.pop(),
              'reverse': 
                lambda:
                    list.reverse()
        }[cmd[0]]()