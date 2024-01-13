def palindrom_check(s):
  normal = s
  reversed = s[::-1]
  if normal == reversed:
    print("Congrats, this is indeed a PALINDROME!")
  else: print("No Palindrome :(")

print(palindrom_check("maddam"))