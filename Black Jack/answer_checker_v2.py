#  def
def question_check(question, answer_list, error_message):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in answer_list:
            if response == item[0] or response == item:
                answer = item
                return answer

        # output error if item not in list
        print(error_message)
        print()


# list
yes_no = [yes, no, xxx]
available_moves = ["hit", "stay", "double up"]
unavailable_moves = []

# main

# loop for test
ans = question_check("do you want to play", yes_no, "pleas answer yes/no/xxx")

if ans == "yes":
    user_choice = "yes"
    print("you chose yes")
elif ans == "no":
    user_choice = "no"
    print("you chose no")
    quit()
else:
    print("left")
    quit()



