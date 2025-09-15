#set = collection which is unordered, unindexed. No dulicate values

utensils = {"fork","spoon","knife"}
utensils.add("napkin")
utensils.remove("fork")
dishes = {"bowl","plate","cup"}
#utensils.update(dishes)
dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)