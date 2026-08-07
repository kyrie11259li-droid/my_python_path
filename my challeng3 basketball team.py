points = [23,17,34,29,8,41,19]

mean=float(sum(points)/len(points))
print("highest:",float(max(points)))
print("lowest:",float(min(points)))
print(f"average:{mean:.2f}")

higher_count=0
lower_count=0

for point in points:
           if point >= 20 :
                higher_count=higher_count + 1
           else:
                lower_count=lower_count + 1
print("20+ points:", higher_count)
print("below 20:", lower_count)
               
