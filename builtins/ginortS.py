string = input()
low = ''
upp = ''
odd = ''
even = ''
for char in string:
    if char.isdigit():
        if int(char) % 2 == 0:
            even += char
        else:
            odd += char
    elif char.isupper():
        upp += char
    else:
        low += char
low = ''.join(sorted(low))
upp = ''.join(sorted(upp))
odd = ''.join(sorted(odd))
even = ''.join(sorted(even))
print((low + upp + odd + even))