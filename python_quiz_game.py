import time




def the_game(questions_and_awnsers,options,the_counter=0,ur_point=0):

  
    for questions in questions_and_awnsers:
    
        print("------------------------------------------------------------------------------------------------------")
        print(questions)
        for option in options[the_counter]:
            print(option)
        the_counter += 1
    
    
        the_awnser = input("please pick a letters as shown for the choices\n").upper()
        # For this "while" loop, I was able to make sure if the user has the correct awnser and input within the choices I presented to them
        while True:
            if the_awnser in ["A","B","C", "D"]:
                if the_awnser == questions_and_awnsers[questions]:
                    print("correct")
                    ur_point += 1
                    break
                else:
                    print("incorrect")
                    print(f"the correct awnser is {questions_and_awnsers[questions]}")
                    break

            else:
                print("the letter or number that you have enter doesnt match the choices that are displayed")
                time.sleep(1.5)
                the_awnser = input("Please enter a vaild choice").upper()
        
    

           

    total_points = (ur_point / len(questions_and_awnsers)) * 100
    total_points = round(total_points, 2)
    total_points = int(total_points)
    
    
    # This show the results of the users and to see if they pass
    if total_points >= 90:
        print(f"congrats you have gotten an A {total_points}% ")
    elif 90 > total_points >= 80:
        print(f"you've gotten a B {total_points}%")
    elif 80 > total_points >=70:
        print(f"you've gotten a C {total_points}%")
    else:
        print(f"your score is a  {total_points}%")
        print("your score is pretty low and you need to study more to acheive your dream")


  
    match(total_points):
        case 3:
            return 4

    
def main():
    print("welcome to my python quiz, in this game it will help you improve your skills and mayabe get me an internship for the future")

    ur_name = input("to get started please enter your name ")

    print(f"Hello {ur_name}, I am going to give you a basic of what you should know about the game that i made. You will be giving a multiple choice quesetion A to D  with a point system\n")
    time.sleep(4)
    print("At the end of the quiz, you are able to take the quiz again and see what you can do to improve the score that you've gotten before\n")
    time.sleep(4)
    print("With all  that said and done, lets get right on to the quiz\n")
    time.sleep(2.4)
    print("Good luck!")
    time.sleep(3.5)




    



    # the varible "options" are the multiple choice with a 2d tuple 
    options = (

        ("A. Local Scope", "B. Global Scope", "C. Module Scope", "D. Block Scope"),
        ("A. \\i ", "B. \\f", "C. \\n", "D. \\d"), 
        ("A.0", "B.1", "C.2", "D.3"),
        ("A.True", "B.False"),
        ("A. /", "B.%", "C.//", "D.*") 

        
    )


    # For this section I have the questions and the awnsers dictionary with a for loop. I put the questions as the index and the awnsers as the value so I can be more accurate to what else I could do.
    questions_and_awnsers = {
            "what kind of scope is in a def function" : "A",
        "Which of these options give out a new line after the string?" : "C",
        "In any index, what number does it start with" : "A",
        "When a 'if' statement does meet there conditions, the 'else' statement can be executed" : "B",
        "which operator divides numbers and gives an integer as a result " : "C",
        
    }
   
   

    
    the_game(questions_and_awnsers, options)
  
    

    play_again = input("you want to retake the game again?").upper()
    if play_again != "YES":
        print("thank you for playing the game and thank you for giving it a shot")
    else:
        the_game(questions_and_awnsers, options)
      

    
    
main()












    
    



        
       
        


