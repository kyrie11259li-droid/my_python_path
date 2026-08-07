scores=[94,37,74,81,57,27,72,81,29,27,26,99,100]

mean=(sum(scores)/len(scores))

print("highest score:",max(scores))
print("lowest score:",min(scores))
print(f"average score:{mean:.2f}")

pass_count=0
fail_count=0
for score in scores:
    if score >60:
        pass_count=pass_count+1
    else:
        fail_count=fail_count+1
print("passed subjects:",pass_count)
print("failed subject:", fail_count)
