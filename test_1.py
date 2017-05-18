answers_easy = {
    "__1__" : "world",
    "__2__" : "Python",
    "__3__" : "print",
    "__4__" : "HTML"
}


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

game_intro = "Welcome to Fill-in-the-blanks, a game to train your knowledge of Python. Please start by selecting a difficulty level. You can choose between 'easy', 'medium' and 'hard'."

def prompt_in_answers (prompt, answers):
    for pia in answers:
        if pia in prompt:
            return pia
    return None

def tries_left (x):
    n = 0
    while n < 5:
        y = 5 - n
        print ("Let's try again. You have " + y + " tries left!")
        return x
        n += 1
    print ("You failed to many straight guesses. GAME OVER!")

def play_level(level, answers):
    print (level)
    replaced = []
    level = level.split()
    for prompt in level:
        replacement = prompt_in_answers(prompt, answers)
        if replacement != None:
            user_input = raw_input ("What should be substituted for " + replacement + "?")
#            if user_input == answers:
#                return user_input + "is correct!"
#            else:
#                print ("That's isn't the correct answer!")
#                return tries_left (user_input)
            prompt = prompt.replace(replacement, user_input)
            replaced.append(prompt)

        else:
            replaced.append(prompt)
    replaced = " ".join(replaced)
    return replaced

def fill_in_the_blanks ():
#    print (game_intro)
    reply = raw_input (game_intro)
    while reply != None:
        if reply == 'easy':
            play_level(level_easy, answers_easy)
            return play_level(level_medium, answers_medium)
        elif reply == 'medium':
            play_level(level_medium, answers_medium)
            return play_level(level_hard, answers_hard)
        elif reply == 'hard':
            play_level(level_hard, answers_hard)
            return "You won!"
    else:
        return "That isn't a difficulty! Please choose between 'easy', 'medium' and 'hard'." + reply

fill_in_the_blanks ()
