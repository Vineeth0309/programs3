def find(dec_num):
    if (dec_num==0):
        return
    else:
        find(int(dec_num/2))
        print(dec_num%2,end="")
find(10)