
# How does this project relates to the Mad Libs Generator we built with Sean? First we adapt the design to work with the numbered blanks:

numbered_blanks = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__" ]

def numbers_in_nb (number, numbered_blanks):
  for nb in numbered_blanks:
    if nb in number:
      return nb
  return None

def play_level (level, numbered_blanks):
    print level
    replaced = []
    level = level.split()
    for number in level:
        replacement = numbers_in_nb (number, numbered_blanks)
        if replacement != None:
            user_input = raw_input ("What should be substituted for " + replacement + "?")
            number = number.replace (replacement, user_input)
            replaced.append(number)
        else:
            replaced.append(number)
    replaced = " ".join(replaced)
    return replaced

print play_level(level_easy, numbered_blanks)
"""

def start_game ():
    print "Welcome to Fill-in-the-blanks, a game to train your knowledge of Python."
    user_input = raw_input ("Please start by selecting a difficulty level. You can choose between 'easy', 'medium' and 'hard': " )
    if user_input == 'easy':
        return play_game (level_easy, answers_easy)
    elif user_input == 'medium':
        return play_game (level_medium, answers_medium)
    elif user_input == 'hard':
        return play_game (level_hard, answers_hard)
    else:
        user_input = raw_input ("That isn't a difficulty level! Please choose between 'easy', 'medium' and 'hard': ")

def tries_left (count)
    count = 5
    if count > 0:
        print "Let's try again. You have " + str(count) + " tries left."
        count -= 1
        return x
    else:
        print "You failed to many straight guesses. GAME OVER!"
