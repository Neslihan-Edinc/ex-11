def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list
user_input1=input("enter a list1: ")
user_input2=input("enter a list2: ")
merge_sorted_lists([user_input1+user_input1])

