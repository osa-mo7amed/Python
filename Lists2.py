Alumni = [
    {"name" : "Osama ", "age" : 21, "job" : "AI Engineer"},
    {"name" : "Mohammed ", "age" : 20, "job" : "Web Developer"},
    {"name" : "Ali ", "age" : 22, "job" : "Data Scientist"},
    {"name" : "Abdaslam ", "age" : 20, "job" : None}, 
] # List of Dictionaries

i = 0
for alumni in Alumni:
    print(i+1 ,alumni["name"], alumni["age"], alumni["job"], sep=", ")
    i = i + 1
    