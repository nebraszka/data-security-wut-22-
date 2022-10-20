dict = {"a": "123", "b": "456", "c": "789"}
string = "abcabc"
print(string.maketrans(dict))

# example dictionary
dict = {97: "123", 98: "456", 99: "789"}
string = "abcabc"
print(string.maketrans(dict))
