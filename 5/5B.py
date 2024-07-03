#Thank You Nipun for making this code short!
def create_text_file():
    file = open("user_text.txt", "w")
    x=int(input("Enter the number of lines (5-6): "))
    for i in range():
        text = input("Enter line " + str(i+1) + ": ")
        file.write(text + "\n")
    file.close()

def find_longest_shortest_words():
    file = open("user_text.txt", "r")
    text = file.read()
    words = text.split()
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    file.close()
    print("Longest word: " + longest_word)
    print("Length: " + str(len(longest_word)))
    print("Shortest word: " + shortest_word)
    print("Length: " + str(len(shortest_word)))

create_text_file()
find_longest_shortest_words()