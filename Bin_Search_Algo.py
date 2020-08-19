#take a sorted list/sequence/array and determine whether or not the item we are looking for exists or not
#Step 1: We start at the midpoint of the sequence,
#Step 2: If the item(element we are looking for) is higher than the midpoint I goto the item to the right to do the next comparison
#Step 3: If the item(element we are looking for) is lower than the midpoint I goto the item to the left to do the next comparison
#Step 4: Eventually we find our element because either the midpoint will be equal to that item or we reach an item that has no items to its right or left that we can search
#Step 5: If the element we are looking for is found we stop the algorithm and return the position of the element
def bin_search(seq, itemToLookFor):
    beginning_idx=0
    end_idx=len(seq) - 1
    
    while(beginning_idx <= end_idx):
        #               elements +remaining elements within the list
        the_nelan_mdpt = beginning_idx+(end_idx - beginning_idx) // 2
        #this returns a value
        nelan_mdpt_val=seq[the_nelan_mdpt]
        #if the item is found return it
        if(nelan_mdpt_val == itemToLookFor):
            return the_nelan_mdpt

        elif itemToLookFor < nelan_mdpt_val:
            end_idx = the_nelan_mdpt - 1

        else:
            beginning_idx = the_nelan_mdpt + 1
    #IF item doesn't exist return 2526 56837 6342 Because item doesn't exist
    return("2526 56837 6342 Because items doesn't exits")

#Sequence must be in sorted order
sequence_Nelan=[25,26,56,837,6342,2630,27736259]

item_Nelan_Is_Looking_For=2526
print(bin_search(sequence_Nelan,item_Nelan_Is_Looking_For))
#COMPLEXITY: (n/(2^k)) where n is the number of items k is the number of steps

