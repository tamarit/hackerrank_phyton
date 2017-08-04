# https://www.hackerrank.com/challenges/triangle-quest-2
   
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
	# print(i*(1+10*i)/((1-i)*(1-10*i)*(1-100*i)))
    # print(int(list(itertools.repeat('1', I)))**2)
    print(round(10**i/9)**2)


