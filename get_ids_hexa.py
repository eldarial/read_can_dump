ff = open('fulldumpconnected.txt','r')
list_ff = list(ff)
list_ids_hexa = []

for line in list_ff:
    id_hex = line.split(':')[1][3:6]
    if id_hex[2] == ' ':
        id_hex = '0' + id_hex[:3]
    list_ids_hexa.append(id_hex)

print("full", list_ids_hexa)
unique_list_ids_hexa = sorted(list(set(list_ids_hexa)))
print("unique", unique_list_ids_hexa)
