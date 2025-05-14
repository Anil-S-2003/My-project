def count_occurrences(s1, s2):
    return s2.count(s1)

# Taking input from user
s1 = input("Enter the substring: ")
s2 = input("Enter the string: ")

print("Occurrences:", count_occurrences(s1, s2))
