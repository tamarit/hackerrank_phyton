# https://www.hackerrank.com/challenges/capitalize

def capitalize(string):
    words = string.split(' ')
    for i in range(0, len(words)):
        if len(words[i]) > 0 and words[i][0].isalpha():
            words[i] = words[i].title()
    return ' '.join(words)

    
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)