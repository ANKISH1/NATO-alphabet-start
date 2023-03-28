import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(file)
dict1 = df.to_dict()
# print(dict1)
# print(file)

# dict = {new_key:new_value for (index,row) in }
dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(dict)

word = input("Enter your name: ").upper()
list = [dict[i] for i in word]
print(list)