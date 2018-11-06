'''
Aaron McCormick
Assingment 5
10/18/2018
'''
def main():
    lst_corr_ans = ["A", "C", "A", "A", "D", "B",
			"C", "A", "C", "B", "A", "D",
			"C", "A", "D", "C", "B", "B",
			"D", "A"]
    lst_user_answers = []
    corr_count = 0
    num_questions = 20
    print("Q\tcorr\tYour\tStatus")
    print("#\tAnswer\tAnswer\n--------------------------")
    with open("user_answers.txt", 'r') as f:
        lst_user_answers = [line.rstrip("\n") for line in f]   # save chars to a list
    for i, item in enumerate(lst_user_answers):
        lst_user_answers[i] = item.rstrip("\r")
    pos = int(0)
    for i in lst_corr_ans:
        if i == lst_user_answers[pos]:
            print(pos + 1, "\t", lst_corr_ans[pos], "\t", lst_user_answers[pos], "\t", sep = "")
            corr_count += 1         
        elif i != lst_user_answers[pos]:
             print(pos + 1, "\t", lst_corr_ans[pos], "\t", lst_user_answers[pos], "\tX", sep = "")
        pos += 1
    percent_corr = (corr_count/20) * 100
    percent_corr_fmt = format(percent_corr, ".1f")
    print("\nGrade : ", corr_count , "/", num_questions, " = ", percent_corr_fmt, sep="")
    if percent_corr >= 75:
        print("Congratulations!! You passed the exam")
    else:
        print("Sorry, you did not pass the exam")
main()