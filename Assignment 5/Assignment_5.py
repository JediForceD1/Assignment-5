def main():
    # Setup variables. DO NOT changes lines 3-9
    lst_corr_ans = ["A", "C", "A", "A", "D", "B",
			"C", "A", "C", "B", "A", "D",
			"C", "A", "D", "C", "B", "B",
			"D", "A"]
    lst_user_answers = []
    corr_count = 0
    num_questions = 20

    # LOOP 1 : Setup file variable and open the user_answers.txt file
    # Place statements to load lst_user_answers from records in user_answers.txt
    # file. Remember to rstrip the \n character
    
    print("Q\tcorr\tYour\tStatus")
    print("#\tAnswer\tAnswer\n--------------------------")

    # LOOP 2 : Code for loop to process each element from lst_corr_ans  and
    # lst_user_answers and update corr_count counter variable accordingly

    percent_corr = (corr_count/20) * 100
    percent_corr_fmt = format(percent_corr, ".1f")
    print("\nGrade : ", corr_count , "/", num_questions, " = ",
         percent_corr_fmt, sep="")
    # Determine if student passed and display result
    if percent_corr >= 75:
        print("Congratulations!! You passed the exam")
    else:
        print("Sorry, you did not pass the exam")
   # Close file

main()