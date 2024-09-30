# This is a Minor CBT Program
def greetings():
      """This is welcome greetings"""
      print("This is Sobur CBT Test")
      print("Welcome new Candidate")
      print("""
 INSTRUCTION:
  1. Use A, B, C and D to choose your option
  2. Do not choose two option at once
  3. Do not engange in Examination Malpractice. 
 """)
      

def Biology():
      """This is a Biology questions"""
      print("")
      print("You are given type S")
      print("")

      test = [
           {
            "Question" : "1. What question type is given to you",
            "Options"  : ["A. D", "B. B", "C. X", "D. S"],
            "Answer"   : "D" 
           },
           {
            "Question" : "2. The father of biology is ?",
            "Options"  : ["A. Gregor Mendel", "B. Aristotle", "C. Carolous Linnaeus", "D. Charles Darwin"],
            "Answer"   : "B" 
           },
           {
            "Question" : "3. Who introducte binomial system of numenclature",
            "Options"  : ["A. Gregor Mendel", "B. Aristotle", "C. Carolous Linnaeus", "D. Charles Darwin"],
            "Answer"   : "C" 
           }
      ]
      for trial in test:
            print(trial["Question"])
            for option in trial["Options"]:
                  print(option)
            answer = input("Enter your answer (A, B, C or D): ").upper()
            if answer == trial["Answer"]:
                  print("Wow, you get the question right")
                  print("")
            else:
                  print("The answer is "+ trial["Answer"])
                  print("")


def Chemisty():
      print("")
      """This is Chemistry questions"""
      print("You are given type O")
      print("")

      test = [
            {
            "Question" : "1. What question type is given to you",
            "Options"  : ["A. O", "B. B", "C. S", "D. F"],
            "Answer"   : "A" 
           },
           {
            "Question" : "2. Who prostulated first periodic law",
            "Options"  : ["A. Henry Moseley", "B. Dmitri Mendelev", "C. Antonnie Lavoisier", "D. RJ Whittaker"],
            "Answer"   : "A" 
           },
           {
            "Question" : "3. WHo discover mass to charge ratio",
            "Options"  : ["A. Henry Moseley", "B. Dmitri Mendelev", "C. Antonnie Lavoisier", "D. JJ Thomson"],
            "Answer"   : "D" 
           }
      ]
      for trial in test:
            print(trial["Question"])
            for option in trial["Options"]:
                  print(option)
            answer = input("Enter your answer (A, B, C or D): ").upper()
            if answer == trial["Answer"]:
                  print("Wow, you get the question right")
                  print("")
            else:
                  print("The answer is "+ trial["Answer"])
                  print("")


def Physics():
      """This is Physics Question"""
      print("")
      print("You are given type B")
      print("")

      test = [
            {
            "Question" : "1. What question type is given to you",
            "Options"  : ["A. D", "B. C", "C. A", "D. B"],
            "Answer"   : "D" 
           },
           {
            "Question" : "2. In a circuit, what is the unit of electrical resistance?",
            "Options"  : ["A. Volt", "B. Ampere", "C. Ohm", "D. Watt"],
            "Answer"   : "C" 
           },
           {
            "Question" : "3. What type of lens is used to correct hyperopia (farsightedness)?",
            "Options"  : ["A. Concave Lens", "B. Convex Lens", "C. Cylindrical Lens", "D. Bifocal Lens"],
            "Answer"   : "B" 
           }
      ]
      for trial in test:
            print(trial["Question"])
            for option in trial["Options"]:
                  print(option)
            answer = input("Enter your answer (A, B, C or D): ").upper()
            if answer == trial["Answer"]:
                  print("Wow, you get the question right")
                  print("")
            else:
                  print("The answer is "+ trial["Answer"])
                  print("")

      
def English():
      print("")
      """This is English Questions"""
      print("You are given U type")
      print("")
      test = [
            {
            "Question" : "1. Which question type is given to you",
            "Options"  : ["A. S", "B. D", "C. U", "D. S"],
            "Answer"   : "C" 
           },
           {
            "Question" : "2. In which sentence is the word 'affect' used correctly?",
            "Options"  : ["A. The weather can affect your mood.", "B. Her speech had a big affect on me.", "C. The affect of the new policy was noticeable.", "D. The movie had a strong affect on the audience."],
            "Answer"   : "A" 
           },
           {
            "Question" : "3. Identify the sentence with a grammatical error:",
            "Options"  : ["A. She don't like apples.", "B. He enjoys playing soccer.", "C. They are going to the park.", "D. I have read that book."],
            "Answer"   : "A" 
           }
      ]
      for trial in test:
            print(trial["Question"])
            for option in trial["Options"]:
                  print(option)
            answer = input("Enter your answer (A, B, C or D): ").upper()
            if answer == trial["Answer"]:
                  print("Wow, you get the question right")
                  print("")
            else:
                  print("The answer is "+ trial["Answer"])
                  print("")


def start():
      """This start the question"""
      name = input("Kindly enter your name here :" ).upper()
      print("Enter Start to Begin or Quit to Exit")
      reply = input("Enter Here: ").upper()
      if reply == "START":
            def questionToAsk():
                  print("Which subject will you start with (Biolgy, Physics, Chemsitry or English)")
                  subject = input("Enter your subject here : ").upper()
                  if subject == "BIOLOGY":
                        Biology()
                  elif subject == "CHEMISTRY":
                        Chemisty()
                  elif subject == "PHYSICS":
                        Physics()
                  elif subject == "ENGLISH":
                        English()
                  else:
                        print("This", subject, "is not available")
                        questionToAsk()
                  def second_question():
                        print("Which Subject will you second?")
                        secondSubject = input("Enter the second subject here: ").upper()
                        if secondSubject == subject:
                              print("You have done this subject before")
                              second_question()
                        elif secondSubject == "BIOLOGY":
                              Biology()
                        elif secondSubject == "CHEMISTRY":
                              Chemisty()
                        elif secondSubject == "PHYSICS":
                              Physics()
                        elif secondSubject == "ENGLISH":
                              English()
                        else:
                              print("The questions for", secondSubject, "subject is not available")
                              second_question()
                        def thirdSubject():
                              print("Which question will you attempt next")
                              third_subject = input("Enter the third subject here: ").upper()
                              if third_subject == secondSubject:
                                    print("You have done this subject before")
                                    thirdSubject()
                              elif third_subject == subject:
                                    print("You have done this subject before")
                                    thirdSubject()
                              elif third_subject == "BIOLOGY":
                                    Biology()
                              elif third_subject == "PHYSICS":
                                    Physics()
                              elif third_subject == "CHEMISTRY":
                                    Chemisty()
                              elif third_subject == "ENGLISH":
                                    English()
                              else:
                                    print("This question for",third_subject, "is not available")
                                    thirdSubject()
                              def lastSubject():
                                    print("What is your last subject")
                                    last_subject = input("Enter your last subject: ").upper()
                                    if last_subject == secondSubject:
                                          print("You have done this subject before")
                                          lastSubject()
                                    elif last_subject == subject:
                                          print("You have done this subject before")
                                          lastSubject()
                                    elif last_subject == third_subject:
                                          print("You have done this subject before")
                                          lastSubject()
                                    elif last_subject == "BIOLOGY":
                                          Biology()
                                    elif last_subject== "CHEMISTRY":
                                          Chemisty()
                                    elif last_subject == "PHYSICS":
                                          Physics()
                                    elif last_subject == "ENGLISH":
                                          English()
                                    else:
                                          print("The question for",last_subject,"is not available")
                                          lastSubject
                              lastSubject()
                        thirdSubject()
                  second_question()
            questionToAsk()
      elif reply == "QUIT":
            print("Exiting the program. Goodbye!", name)
            #quit()
      else:
            start()    
greetings()
start()