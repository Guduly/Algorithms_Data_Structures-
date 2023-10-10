'''
    list - is the list where the target is located
    target - index of the target
'''
def Linear_Search(list, target):

    '''
    finds and puts the length of list from 0-list's length
    '''
    for item in range(0,len(list)):

        if item == target:
            return print(f"FOUND!; The target is",list[item],"at",item)
        else:
            print("NOT FOUND!")
      
        
Linear_Search([1,2,3,4,5], 2)
Linear_Search([3,5,7,9,0,4], 6)
        