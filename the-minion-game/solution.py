# https://www.hackerrank.com/challenges/the-minion-game

# # Copied from:
# # https://stackoverflow.com/a/12945063
# def consecutive_groups(iterable):
#     s = tuple(iterable)
#     for size in range(1, len(s)+1):
#         for index in range(len(s)+1-size):
#             yield iterable[index:index+size]

def minion_game(string):
    # your code goes here
    points_stuart = 0
    points_kevin = 0
    # substr = consecutive_groups(string)
    # for ss in substr:
    #     if ss[0] in ('A', 'E', 'I', 'O', 'U'):
    #         points_kevin += 1
    #     else:
    #         points_stuart += 1

    for i in range(0, len(string)):
        if string[i] in ('A', 'E', 'I', 'O', 'U'):
            points_kevin += len(string) - i
        else:  
            points_stuart += len(string) - i
    if points_stuart > points_kevin:
        print("Stuart " + str(points_stuart))
    else:
        if points_stuart < points_kevin:
            print("Kevin " + str(points_kevin))  
        else:
            print("Draw")


    
if __name__ == '__main__':
    s = input()
    minion_game(s)