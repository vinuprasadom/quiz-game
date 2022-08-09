from data import question_data;
import random

print(random.choice(question_data)["text"])
print(random.choice(question_data)["answer"])


class Question():

    def __init__(self):
        question = random.choice(question_data)
        self.text = question["text"]
        self.answer = question["answer"]

    def print_qn(self):
        print(self.text)

    def check_ans(self, ans):
        if ans == self.answer:
            print("Correct")
            return True
        else:
            print("Wrong!!")
            return False


ans_flg = True
while ans_flg:
    qn = Question()

    qn.print_qn();
    ans = input("True/False : ")
    if not qn.check_ans(ans):
        ans_flg = False
