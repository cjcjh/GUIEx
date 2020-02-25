def bubbleSort(a):
    sorted = False
    while(not sorted):
        sorted = True
        for i in range(1,len(a)):
            if(a[i-1] > a[i]):
                a[i-1],a[i]=a[i],a[i-1]
                sorted = False

