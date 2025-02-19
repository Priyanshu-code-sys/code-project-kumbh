#Question 
ques = [["First president of India _______.", ["A. Nehru", "B. Kalam", "C. Rajendra Prasad", "D. Ambedkar"]], ["Who developed Python?", ["A. Tim Berners Lee", "B. Guido Von Rossum", "C. Bill Gates", "D. Jeff Bejos"]]]

#Answer
ans = ["C","B"]

#Printing question answer
for i in ques:
    print("\n",i[0], "\n")
    print(i[1],"\n")
    ch = input("Enter your answer: ")
    for i in ans:
        if ch == i:
            print("\nCORRECT ANSWER!!!")
            print("You Win 1000/-\n")
            break
        else:
            print("\nWRONG ANSWER")
            print("Sorry! You loose!\n")

    
