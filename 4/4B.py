import re
text = input("Enter the text: ")

vowels = re.findall(r'[aeiouAEIOU]', text)
consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text)
digits = re.findall(r'[0-9]', text)

print("Vowels:", len(vowels))
print("Consonants:", len(consonants))
print("Digits:", len(digits))