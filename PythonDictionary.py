import pandas as pd
person = {
    "first" : "Maryam" ,
    "last" : "Magdy",
    "email": "maryammagdy099@gmail.com"
}
person = {
    "first" : ["Maryam"] ,
    "last" : ["Magdy"],
    "email": ["maryammagdy099@gmail.com"]
}
people = {
    "first" : ["Maryam","Saleh","Zainab"] ,
    "last" : ["Magdy","Mohammed","Ali"],
    "email": ["maryammagdy099@gmail.com", "salehmohammed32@gmail.com","zainabaly88@gmail.com"]
}
print(people["email"])
df = pd.DataFrame(people)
print(df)
print(df["email"]) # equal to --> df.email also equal to print(people["email"])
print(type(df['email']))

#access multiple columns
print(df[['last','email']])

print(df.columns) 

print(df.iloc[[0,1], 2])

print(df.loc[[0,1], 'email'])
print(df.loc[[0,1], ['email','last']])

print(df.set_index('email', inplace = True)) # equal to df = df.set_index('email')
print(df.head)
print(df.index)
print(df.loc['maryammagdy099@gmail.com', 'last']) #df.loc[0] doesn't work while df.iloc[0] works

df.reset_index(inplace=True)
print(df.index)
print(df.head)