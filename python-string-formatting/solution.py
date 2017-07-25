# https://www.hackerrank.com/challenges/python-string-formatting

def get_rep(fun, number):
    rep = str(fun(number))
    if fun == oct:
        start = 1
    else:
        start = 2
    return (rep[start:len(rep)]).upper()

def print_formatted(number):
    binNumber = get_rep(bin, number)
    width = len(binNumber)
    for i in range(1, number + 1):
        i_dec = str(i)
        i_oct = get_rep(oct, i)
        i_hex = get_rep(hex, i)
        i_bin = get_rep(bin, i)
        dec_str = i_dec.rjust(width,' ')
        oct_str = i_oct.rjust(width,' ')
        hex_str = i_hex.rjust(width,' ')
        bin_str = i_bin.rjust(width,' ')
        print(dec_str + " " + oct_str + " " + hex_str + " "+ bin_str)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)