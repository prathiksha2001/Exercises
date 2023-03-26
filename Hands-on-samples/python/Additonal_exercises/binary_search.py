ls1 = [11,65,78,90,128,245,345,678,876,900,1000,1296]
# ls1 = [1,2,3,4,5,6,7,8,9]
start_index = 0
end_index = len(ls1)-1

def binary_search(start_index, end_index,search_num):
    mid_index = (end_index+start_index)//2 
    print(start_index,end_index,mid_index)
    
    if(search_num == ls1[mid_index]):
        # print(search_num)
        return mid_index
    if(start_index >= end_index):
        return None    
    if(search_num < ls1[mid_index]):
        end_index = mid_index-1
        return binary_search(start_index,end_index,search_num)
    if(search_num > ls1[mid_index]):
        start_index = mid_index + 1
        return binary_search(start_index,end_index,search_num)       

res = binary_search(start_index,end_index,1000)
if not res:
    print("not found")
else: 
    print(res)
start_index = 0
end_index = len(ls1)-1
search_num = 1000
while(start_index<end_index):
    mid_index = (start_index + end_index)//2
    if(search_num<ls1[mid_index]):
        end_index = mid_index - 1
    elif(search_num > ls1[mid_index]):
        start_index = mid_index + 1
    else:
        print(mid_index)
        break

