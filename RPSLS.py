import random

possible_actions = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
quotes = ["I'm not crazy, my mother had me tested.", "I cry because other people are stupid, and that makes me sad.",
          "Bazinga.", "Not knowing is part of the fun.  Was that the motto of your community college?",
          "I'm a fan of anything that tries to replace actual human contact.",
          "Mom smokes in the car. Jesus is okay with it, but we can't tell dad."]

computer_action = random.choice(possible_actions)
quote_random = random.choice(quotes)

player = False

while player == False:
   player = input('Rock, Paper, Scissors, Lizard, or Spock? ')
   if player == computer_action:
       print('I played ' + computer_action + ".  It's a tie!")
       print(quote_random)
   elif player == 'Rock':
       if computer_action == 'Paper':
           print('I played ' + computer_action + ".  I won!")
           print(quote_random)
       elif computer_action == 'Lizard':
           print(player + ' crushes ' + computer_action + '.  You win this time.')
           print(quote_random)
       elif computer_action == 'Scissors':
           print('As always, ' + player + ' smashes ' + computer_action + '.')
           print(quote_random)
       else:
           print(computer_action + ' vaporizes ' + player)
           print(quote_random)
   elif player == 'Paper':
       if computer_action == 'Rock':
           print('I played ' + computer_action + '.  You win!')
           print(quote_random)
       elif computer_action == 'Scissors':
           print('Snip snip, you lose!')
           print(quote_random)
       elif computer_action == 'Lizard':
           print(computer_action + ' eats ' + player)
           print(quote_random)
       else:
           print(player + ' disproves ' + computer_action + '.  You win I guess.')
           print(quote_random)
   elif player == 'Scissors':
       if computer_action == 'Rock':
           print('I played ' + computer_action + '.  You lost to a computer!')
           print(quote_random)
       elif computer_action == 'Paper':
           print(player + ' cuts ' + computer_action + '.  You win I guess.')
           print(quote_random)
       elif computer_action == 'Lizard':
           print(player + ' decapitates ' + computer_action + ".  That's disgusting, but you win.")
           print(quote_random)
       else:
           print(computer_action + ' smashes ' + player)
           print(quote_random)
   elif player == 'Lizard':
       if computer_action == 'Rock':
           print('Oh my, ' + computer_action + ' crushes ' + player + ', so I win!')
           print(quote_random)
       elif computer_action == 'Paper':
           print(player + ' eats ' + computer_action + ".  You're making me look bad.")
           print(quote_random)
       elif computer_action == 'Scissors':
           print('Ha!  ' + computer_action + ' decapitates ' + player + '.  Which is gross, but I win.')
           print(quote_random)
       else:
           print(player + ' poisons ' + computer_action + ".  What's the fracas, you beat me!")
           print(quote_random)
   elif player == 'Spock':
       if computer_action == 'Rock':
           print(player + ' vaporizes ' + computer_action + '.  I guess you win.')
           print(quote_random)
       elif computer_action == 'Paper':
           print(computer_action + ' disproves ' + player + ".  I don't believe in luck, I'm just better at this than you.")
           print(quote_random)
       elif computer_action == 'Scissors':
           print(player + ' smashes ' + computer_action + '.  I guess you win.')
           print(quote_random)
       else:
           print(computer_action + ' poisons ' + player + ".  I guess it pays to play something other than Spock.")
           print(quote_random)
   else:
       print('That is not a valid input.  Please check your spelling!')
   again = input('Do you want to play again? (Y/N): ')
   if again == 'Y':
       player = False
   else:
       print('Bazinga, thanks for playing!')

