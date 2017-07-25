# https://www.hackerrank.com/challenges/alphabet-rangoli

def create_line_center(size, current):
    first = size - 1
    forth = ""
    for i in range(0,current - 1):
        forth += (chr(ord('a') + (first - i)))
        forth += '-'
    back = forth[::-1]
    forth += chr(ord('a') + (first - (current - 1)))
    return forth + back

def print_rangoli(size):
    size_line = (((size - 1) * 4) + 1)
    before = []
    for i in range(1, size):
        before.append(create_line_center(size, i).center(size_line, '-'))
    center = [create_line_center(size, size).center(size_line, '-')]
    after = list(reversed(before))
    all_lines = before + center + after
    print('\n'.join(all_lines))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)