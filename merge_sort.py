def mergeSort(alist):

    print("Splitting ",alist)

    if len(alist)>1:

        mid = len(alist)//2

        lefthalf = alist[:mid]

        righthalf = alist[mid:]

        
        print('starting mergesort of lefthalf')

        mergeSort(lefthalf)

        print('starting mergesort of righthalf')

        mergeSort(righthalf)


        i=0

        j=0

        k=0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:

                alist[k]=lefthalf[i]

                print('alist[k]=lefthalf[i]')

                i=i+1

            else:

                alist[k]=righthalf[j]

                print('alist[k]=righthalf[j]')

                j=j+1

            k=k+1


        while i < len(lefthalf):

            alist[k]=lefthalf[i]

            print('alist[k]=lefthalf[i]')

            i=i+1

            k=k+1


        while j < len(righthalf):

            alist[k]=righthalf[j]

            print('alist[k]=righthalf[j]')

            j=j+1

            k=k+1

    print("Merging ",alist)


alist = [54,26,93,17,77,31,44,55,20]

mergeSort(alist)
print(alist)  