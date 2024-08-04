def add(dict, word , meaning):
  dict[word]= meaning
def remove(dict, word):
  if word in dict:
    del dict[word]
  else:
    print("Word not found")
def search(dict, word):
  if word in dict:
    print("Meaning: ", dict[word])
  else:
    print("Word not found")
def search_meaning(dict, meaning):
  found = False
  for key, value in dict.items():
    if value == meaning:
      print("Word: ", key)
      found = True
  if not found:
    print("Meaning not found")
def display(dict):
  for key, value in dict.items():
    print(key, ":", value)
dictionary = {}
while True:
    print("\nDictionary Menu:\n1. Add a new word\n2. Search for a word\n3. Find words with the same meaning\n4. Remove a word\n5. Display all words\n6. Exit")
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
      word = input("Enter a word: ")
      meaning = input("Enter its meaning: ")
      add(dictionary, word, meaning)
    elif choice == '2':
      word = input("Enter a word: ")     
      remove(dictionary, word)
    elif choice == '3':
      word = input("Enter a word: ")    
      search(dictionary, word)
    elif choice == '4':
      meaning = input("Enter a meaning: ")
      search_meaning(dictionary, meaning)
    elif choice == '5':
      display(dictionary)
    elif choice == '6':
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")
