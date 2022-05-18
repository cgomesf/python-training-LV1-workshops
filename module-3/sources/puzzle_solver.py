def main():
    """main"""




    # open file
    with open("input.txt","r") as f:
        content=f.readlines()   # reading file

    # read depths
    _l=[]
    for s in content:
        depth=int(s.strip('\n'))
        _l.append(depth)

    # count number of times value is higher than previous value
    c=0
    for a,b in zip(_l,_l[1:]):
        if b < a:
            c+=    1

    print( c )
    assert c == 1655

if __name__=="__main__":
    main()