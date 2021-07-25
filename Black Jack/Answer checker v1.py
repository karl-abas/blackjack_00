#  def
def question_check(question, answer, error_message):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in answer:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error_message)
        print()


# list
yes_no = ["yes", "no", "xxx"]
# main

user_choice = ""
while loop == "yes":

    user_choice = question_check("do you want to play a game", yes_no, "please answer yes/y/no/n/xxx")
    print("you chose{}".format(user_choice))
