for i in range(1,100):
    if (i%3 == 0) and (i%5 == 0):
        print('parapeba')
        continue
    elif (i%3 == 0):
        print('para')
        continue
    elif (i%5 == 0):
        print('peba')
        continue
    print(i)
