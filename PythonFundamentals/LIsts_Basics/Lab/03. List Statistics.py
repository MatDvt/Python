num = int(input())

postives = []
negatives = []

for _ in range(num):
    current_num = int(input())
    if current_num < 0:
        negatives.append(current_num)
    else:
        postives.append(current_num)

print(postives)
print(negatives)
print(f'Count of positives: {len(postives)}. Sum of negatives: {sum(negatives)}')