arrays = ["水","金","地","火","木","土","天","海","冥"]

#for文で書く
for array in arrays:
    print(array)

#while文で書く
i = 0
while arrays[i] != "冥":
    print(arrays[i])
    i = i + 1
print(arrays[i])
