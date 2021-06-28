for line in range(5):
    # print space
    #print star
    #print next line
    for space in range(4-line):
        print(" ",end ="")
    for star in range(int(line+1)):
        print("*", end =" ")
    print("\n")
        
