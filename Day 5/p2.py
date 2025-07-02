import pandas as pd

data = [["Krishna", 20, "Delhi"], ["Garvit", 21, "Mumbai"], ["Nasir", 22, "Bangalore"]]
df= pd.DataFrame(data, columns=["Name", "Age", "City"])
print(df,"\n")

data = {"Name": "Krishna", "Age": 20, "City": "Delhi"}
df = pd.DataFrame([data])
print(df,"\n")

data = [["Krishna", 20, "Delhi"], ["Garvit", 21, "Mumbai"], ["Nasir", 22, "Bangalore"]]
df = pd.DataFrame(data, columns=["Name", "Age", "City"])
print(df,"\n")

data = [("Krishna", 20, "Delhi"), ("Garvit", 21, "Mumbai"), ("Nasir", 22, "Bangalore")]
df = pd.DataFrame(data, columns=["Name", "Age", "City"])
print(df,"\n")

data = [{"Name": "Krishna", "Age": 20, "City": "Delhi"}, {"Name": "Garvit", "Age": 21, "City": "Mumbai"}, {"Name": "Nasir", "Age": 22, "City": "Bangalore"}]
df = pd.DataFrame(data)
print(df)