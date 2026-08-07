numbers=[12,5,18,7,9,20,15,22,31,44]

mean=sum(numbers)/len(numbers)
print("largest number:",max(numbers))
print("smallest number:",min(numbers))
print("average:",f"{mean:.2f}")
even=0
odd=0
largest_even=12
largest_odd=5

for number in numbers:
    if number%2 == 0:
        even=even+1
        if  largest_even < number :
            largest_even = number
    else:
        odd=odd+1
        if largest_odd < number :
            largest_odd = number
    
print("even number:",even)
print("odd number:",odd)
print("largest even number:",largest_even)
print("largest odd number:",largest_odd)
