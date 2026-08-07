prices=[14,43,64,23,74,44,66,56,54,35,47]

total_price=float(sum(prices))
average_price=float(sum(prices)/len(prices))
most_expensive=float(max(prices))
cheapest=float(min(prices))
higher_count=0
lower_count=0


print(total_price)
print(f"{average_price:.2f}")
print(most_expensive)
print(cheapest)

for price in prices:
    if price > 40:
        higher_count=higher_count+1
    else:
        lower_count=lower_count+1
print("more than $40:",higher_count)
print("$40 or below:",lower_count)        
        
