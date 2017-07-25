# https://www.hackerrank.com/challenges/find-a-string

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        equal = True
        if (len(string) - i) < len(sub_string):
            equal = False
            break
        else:
            for j in range(0, len(sub_string)):
                if string[i + j] != sub_string[j]:
                    equal = False
                    break
            if equal:
                count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)