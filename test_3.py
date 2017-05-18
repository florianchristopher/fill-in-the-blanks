# Write a fill_in_the_blanks Quiz.
# Start by selecting three levels easy, medium and hard. Also write down their answers.

# copy from fitb_test_1:

answers_easy = {
    "__1__" : "world",
    "__2__" : "Python",
    "__3__" : "print",
    "__4__" : "world"
}

# or list? answers_easy = [ "world", "python", "print", "html"]

answers_medium = {
    "__1__" : "function",
    "__2__" : "arguments",
    "__3__" : "None",
    "__4__" : "lists"
}

answers_hard = {
    "__1__" : "class",
    "__2__" : "method",
    "__3__" : "init_",
    "__4__" : "instance",
    "__5__" : "repr",
    "__6__" : "add",
    "__7__" : "sub",
    "__8__" : "less than",
    "__9__" : "greater than",
    "__10__" : "equals"
}

level_easy = "A common first thing to do in a language is display 'Hello __1__!'  In __2__ this is particularly easy; all you have to do is type in: __3__ 'Hello __1__!' Of course, that isn't a very useful thing to do. However, it is an example of how to output to the user using the __3__ command, and produces a program which does something, so it is useful in that capacity." + "It may seem a bit odd to do something in a Turing complete language that can be done even more easily with an __4__ file in a browser, but it's a step in learning __2__ syntax, and that's really its purpose."

level_medium = "A __1__ is created with the def keyword.  You specify the inputs a __1__ takes by adding __2__ separated by commas between the parentheses. __1__s by default returns __3__ if you don't specify the value to retrun. __2__ can be standard data types such as string, integer, dictionary, tuple, and __4__ or can be more complicated such as objects and lambda functions."

level_hard = "When you create a __1__, certain __2__s are automatically generated for you if you don't make them manually. These contain multiple underscores before and after the word defining them.  When you write a __1__, you almost always include at least the __3__ __2__, defining variables for when __4__s of the __1__ get made.  Additionally, you generally want to create a __5__ __2__, which will allow a string representation of the method to be viewed by other developers. You can also create binary operators, like __6__ and __7__, which allow + and - to be used by __4__s of the __1__.  Similarly, __8__, __9__, and __10__ allow __4__s of the __1__ to be compared (with <, >, and ==)."

game_intro = "Welcome to Fill-in-the-blanks, a game to train your knowledge of Python."

# copy from fitb-test_2.py:

numbered_blanks = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__" ]

# write in pseudocode

def numbers_in_a (number, answers):
  for a in answers:
    if a in number:
      return a
  return None
"""
def check_answer (level, answers):
    replacement = numbers_in_a (number, answers)
    for number in level:
        if replacement != None:
            count = 5
            while count > 0:
                user_input = raw_input ("What should be substituted for " + replacement + "?")
                for replacement in answers:
                    if replacement is True:
                        number = number.replace (replacement, user_input)
                        replaced.append(number)
                        replaced = " ".join(replaced)
                    else:
                        count -= 1
                        print ("Let's try again. You have " + str(count) + " tries left!")
                        return count
        else:
            print "You failed to many straight guesses. GAME OVER!"
    else:
        replaced.append(number)
        replaced = " ".join(replaced)

print check_answer (level_easy, answers_easy)

"""
def play_level(level, answers):
    print level
    replaced = []
    level = level.split()
    for number in level:
        replacement = numbers_in_a (number, answers)
        if replacement != None:
            count = 5
            while count > 0:
                count -= 1
                user_input = raw_input ("What should be substituted for " + replacement + "?")
                if user_input in answers:
                    if user_input is True:
                        print ("%d is correct!") % (user_input)
                        return replacement
                    else:
                        print ("Let's try again. You have " + str(count) + " tries left!")
                        return user_input

            else:
                print "You failed to many straight guesses. GAME OVER!"
        else:
            replaced.append(number)
    replaced = " ".join(replaced)
    #for number in level:

        # replacement = numbers_in_a (number, answers)
        # if replacement != None:
            # can i substitue the follwong with a new def check_answers?
            # user_input = raw_input ("What should be substituted for " + replacement + "?")
            # check if answer is correct
            # number = number.replace (replacement, user_input)
            # replaced.append(number)
        # else:
            #replaced.append(number)
    #replaced = " ".join(replaced)
    return replaced

"""
        check if each word is identical with numbered_blanks or answers (dictionary)
        ask for the correct answer for each numbered blank
            if asnwer is True
                return to next numbered blank
            else:
                tries_left (answers)
        replace correct answer for numbered blank
        return to next numbered blank
        if all answers are correct
    return level with answers
"""

def play_game ():
    print game_intro
    choose_level = raw_input ("Please start by selecting a difficulty level. You can choose between 'easy', 'medium' and 'hard': " )
    if choose_level == 'easy':
        play_level (level_easy, answers_easy)
        return play_level (level_medium, answers_medium)
    elif choose_level == 'medium':
        play_level (level_medium, answers_medium)
        return play_level (level_hard, answers_hard)
    elif choose_level == 'hard':
        play_level (level_hard, answers_hard)
        return "You've won!"
    else:
        print "That isn't a difficulty!"
        return choose_level # ???

play_game ()
