import random

# Generate 20 random numbers
random_numbers = []
for _ in range(20):
    num = random.randint(1, 100)
    random_numbers.append(num)

print("Random numbers:")
print(random_numbers)

# Filter odd numbers with 2 or 4 digits
odd_numbers = []
for num in random_numbers:
    if num % 2 != 0 and len(str(num)) in (2,4):
        odd_numbers.append(num)

print("\nOdd numbers with 2 or 4 digits:")
print(odd_numbers)