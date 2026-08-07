scores=[94,37,74,81,51,27,72,81,29,27,26]

mean=sum(scores)/len(scores)
print("highest score:",max(scores))
print("lowest score:",min(scores))
print("average score:",f"{mean:.2f}")


passed=0
failed=0

for score in scores:
    if score >= 60:
        passed=passed+1
    else:
        failed=failed+1
print("passed subjuects:",passed)
print("failed subjects:",failed)

pass_rate=100*(passed/len(scores))

print(f"pass rate:{pass_rate:.2f}%")
