import random
from game_data import data
import art 



def format_data(account):
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  account_followers = account['follower_count']
  return f'{account_name}, a {account_descr}, from {account_country}'

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == "b"



print(art.logo7)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)

  print(f'Compare: {format_data(account_a)}')
  print(art.vs)
  print(f'Against: {format_data(account_b)}')

  guess = input('Who has more followers? Type "A" or "B": ').lower()

  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  if is_correct:
    score += 1
    print(f'You are right! Current score: {score}.\n')
  else:
    game_should_continue = False
    print(f'Sorry, that is wrong. Final score: {score}')