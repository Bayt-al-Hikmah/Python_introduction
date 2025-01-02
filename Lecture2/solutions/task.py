friend1 = {"name":"ali","age":23,"favourite_colors":{"red","green","black"}}
friend2 = {"name":"cat","age":5,"favourite_colors":{"black","green","white","orange"}}
shared_colors = friend1["favourite_colors"].intersection(friend2["favourite_colors"])
friend1_favourite = friend1["favourite_colors"].difference(friend2["favourite_colors"])
print("the colors that both",friend1["name"],"and",friend2["name"],"favourites are :")
print(shared_colors)
print("the colors that only",friend1["name"],"favourites are :")
print(friend1_favourite)