'''
Created on Nov 12, 2015

@author: siva
'''
import itertools
import copy
#import numpy

LIST_ELEMENTS   = ['pe_0','pe_1b','pe_2','pe_3d','pe_4','pe_5']
NUM_GROUPS      = 3
GROUP_SIZES     = [2,2,2]
GROUP_VALUES    = [1,3,5]

#Validation :
if((NUM_GROUPS != len(GROUP_SIZES)) | (sum(GROUP_SIZES) != len(LIST_ELEMENTS)) ):
    print('Incorrect input data.Check again !!!!')
    quit()

print('Input data looks correct !!!. lets create the arrangements :)')
#The levels of nested for loops is equal to the number of groups in the arrangement.
#Therefore the number of levels needs to be changed with the number of groups.
for subset1 in itertools.combinations(LIST_ELEMENTS,GROUP_SIZES[0]):
    tmp_list = copy.deepcopy(LIST_ELEMENTS)
    tmp_list = [x for x in tmp_list if x not in subset1]
    #print(tmp_list)
    for subset2 in itertools.combinations(tmp_list,GROUP_SIZES[1]):
        tmp_list1 = copy.deepcopy(tmp_list)
        tmp_list1 = [x for x in tmp_list1 if x not in subset2]
        #print(tmp_list)
        #print(tmp_list1)
        for subset3 in itertools.combinations(tmp_list1,GROUP_SIZES[2]):
            new_arrangement = []
            #new_arrangement.append(subset1)
            #new_arrangement.append(subset2)
            #new_arrangement.append(subset3)
            new_arrangement.extend(subset1)
            new_arrangement.extend(subset2)
            new_arrangement.extend(subset3)
            value_list1 =[]
            for cntr1 in range(len(GROUP_SIZES)):
                for cntr2 in range(GROUP_SIZES[cntr1]):
                    value_list1.insert(len(value_list1),GROUP_VALUES[cntr1])
            value_list2 = []
            for elements in LIST_ELEMENTS:
                value_list2.insert(len(value_list2),value_list1[new_arrangement.index(elements)])
            print(new_arrangement)
            #print(value_list1)
            print(value_list2)
