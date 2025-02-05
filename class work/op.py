S1 = {"Red" ,"yellow", "orange" , "blue" }
S2 = {"violet", "blue" , "purple"}
print(S1.issubset(S2))
print(S1.isdisjoint(S2))
print(S1.union(S2))
print(S1.intersection(S2))
print(S1.issuperset(S2))
S1.add("hallo eberynya")
S1.update("ooh my gaww", "crazy")
S1.remove("Red")
S1.discard("yellow")
print(S1)
print(S2)