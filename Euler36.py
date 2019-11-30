# Euler 36 Double Base Palindromes
# Sum of all Palindromes <1mio on base 10 and 2

# Create List with all Palindromes <1mio on base 10
list = list(range(1,1000000))
palindrome_10_list = []
palindrome_2_list = []
sum = 0
print(list)
for x in list:
        if str(x) == str(x)[::-1]:
            palindrome_10_list.append(x)
print(palindrome_10_list)

# Subset of all palindromes that are also palindrome on base 2
for x in palindrome_10_list:
    if str(bin(x)[2:]) == str(bin(x)[2:])[::-1]:
        palindrome_2_list.append(x)
print(palindrome_2_list)
for x in palindrome_2_list:
    sum = sum + x
print(sum)


# Sum subset