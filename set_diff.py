
f1 = open('aconoff.txt','r')
list_f1 = list(f1)
unique_l1 = list(set(list_f1))
print("dim1 ", len(unique_l1), len(list_f1))

f2 = open('parkassist.txt','r')
list_f2 = list(f2)
unique_l2 = list(set(list_f2))
print("dim2 ", len(unique_l2), len(list_f2))

diff_list = []

for elem in unique_l1:
    if elem not in unique_l2:
        diff_list.append(elem)

print(diff_list)
