
import copy

def items_shering(values :list , index :int, num_of_items, all_possible_val:list ,j):

    if num_of_items ==0:
        return all_possible_val[2**index-1:]
    level=2**index
    to_range=level
    while to_range :
        value_in_index = all_possible_val[j]
        for i in range(0,2):
            new_possible=copy.deepcopy(value_in_index)
            new_possible[i] += values[index][i]
            all_possible_val.append(new_possible)

        to_range-=1
        j+=1

    return items_shering(values,index+1,num_of_items-1,all_possible_val ,j)




def wrapper(l):
    return items_shering(l,0,len(l),[[0,0]],0)

def find_min(l):
    if l == None :
        return l
    i=0
    index =0
    max_min = min(l[0])
    for item in l:
        minimum = min(item)
        if minimum > max_min:
            max_min = minimum
            index =i
        i+=1
    print ("the max min value is :",l[index])

if __name__ == '__main__':
    list1=[[11,22],[1,3]]
    list2 = [[11, 22], [1, 3], [5,7]]
    list3= [[1,1,],[11,11],[13,13]]
    print(wrapper(list1))
    print(wrapper(list2))
    find_min(wrapper(list1))
    find_min(wrapper(list2))
    find_min(wrapper(list3))