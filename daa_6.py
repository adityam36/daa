def quick(sequence):
   length = len(sequence)
   if length<=1:
      return sequence
   else:
      pivot = sequence.pop()
   
   item_greater = []
   item_lower = []
   
   for item in sequence:
      if item>pivot:
         item_greater.append(item)
      else:
         item_lower.append(item)
         
   return quick(item_lower) + [pivot] + quick(item_greater)
   
print(quick([33,45,333,67,1,767,87,4,33,2,0]))

# o/p


'''
[0, 1, 2, 4, 33, 33, 45, 67, 87, 333, 767]
'''