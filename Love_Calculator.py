print('Welcome to the Love Calculator!')
your_name = input('What is your full name? \n')
their_name = input('What is their full name? \n')

combined_names = your_name + their_name
lower_case_names = combined_names.lower()

t = lower_case_names.count('t')
r = lower_case_names.count('r')
u = lower_case_names.count('u')
e = lower_case_names.count('e')

true = t + r + u + e

l = lower_case_names.count('l')
o = lower_case_names.count('o')
v = lower_case_names.count('v')
e = lower_case_names.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))


if love_score < 10:
    print(f'Your score is {love_score}, you go together like coke and menthos.')
elif love_score >= 90:
    print(f'Your score is {love_score}, you go together like Yin and Yang.')
elif (love_score >= 40) or (love_score  <=  50):
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
