temperatures=[28.5,31.2,27.8,35.6,24.9,36.7]
mean=float(sum(temperatures)/len(temperatures))
hot_days_count=0
normal_days_count=0

print("highest temperature:",max(temperatures))
print("lowest temperature:", min(temperatures))
print(f"average temperature:{mean:.2f}")

for temperature in temperatures:
    if temperature > 30:
        hot_days_count=hot_days_count+1
    else:
        normal_days_count=normal_days_count+1
print("hot days:",hot_days_count)
print("normal days:",normal_days_count)
        
