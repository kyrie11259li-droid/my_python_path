scores = []

subjects=int(input("how many subjects do you have?"))

for i in range(subjects):
    score=int(input(f"enter score {i+1}:"))
    scores.append(score)

print("highest score:",max(scores))
print("lowest scores:",min(scores))
mean=sum(scores)/len(scores)
print(f"average scores:{mean:.2f}")

passed=0
failed=0

for score in scores:
    if score >= 60:
        passed = passed + 1
    else:
        failed = failed +1
print("passed subjects:",passed)
print("failed subjects:",failed)
pass_rate=100*(passed/len(scores))
print(f"pass rate:{pass_rate:.2f}%")
