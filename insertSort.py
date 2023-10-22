'''
The goal is make an unsorted list into a sorted one

insert sort is O(n^2) and is best for small data
'''


def insertSort(list, n):

    for item in range(0,n):
        #first index and the index value under it are chosen
        key = list[item]
        j = item-1

        # if the index value under it has a higher value
        # then index and index value under will switch positions
        while(j > 0 and list[j]>key):
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

    # additional variable for switching
    store = 0

    # switches index 0 and 1 if index[0] has a higher
    #value than index 1;
    if(list[0] > list[1]):
        store = list[0]
        list[0] = list[1]
        list[1] = store
    

    return list

print(insertSort([1,4,8,4,2,1000], 6))
'''
---> [1, 2, 4, 4, 8, 1000]
'''

print(insertSort([9,5,87,543,67,0], 6))
'''
---> [0, 9, 5, 67, 87, 543]
'''

print(insertSort([934234,539825,456,94565], 4))
'''
---> [456, 934234, 94565, 539825]
'''