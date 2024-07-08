def count_characters(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        upper_case_count = sum(1 for char in text if char.isupper())
        lower_case_count = sum(1 for char in text if char.islower())
        digit_count = sum(1 for char in text if char.isdigit())
        return upper_case_count, lower_case_count, digit_count

def main():
    file_name = "user_input.txt"
    with open(file_name, 'w') as file:
        x=int(input("Enter the number of lines (5-6): "))
        print("Enter 5-6 lines of text:")
        for i in range(x):
            line = input("> ")
            file.write(line + "\n")
        print("File created successfully!")

    upper_case_count, lower_case_count, digit_count = count_characters(file_name)

    print(f"File Details - ")
    print(f"File Name: {file_name}")
    print(f"Upper Case Characters: {upper_case_count}")
    print(f"Lower Case Characters: {lower_case_count}")
    print(f"Digits: {digit_count}")

if __name__ == "__main__":
    main()