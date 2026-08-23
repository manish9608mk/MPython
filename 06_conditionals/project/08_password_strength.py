password = input('\nEnter your password: ').strip()
password = password.replace(" ", "") # to avoid spacace
pass_length = len(password)

if pass_length < 6:
  strength = 'Weak'
elif pass_length <= 10:
  strength = 'Medium'
else:
  strength = 'Strong'

print(f'Your password is {password} and its, strength is: {strength}')
