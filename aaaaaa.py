# This is another cbt quesition
def  Biology():
    """This is biology Questions"""
    test = [
        {   
            "Question" : "1. What controls the activities of the cell",
            "Options" : ["A. Cytoplasm", "B. Nucleolus", "C. Nucleus", "D. Cell Membrane"],
            "Answer" : "C"
        },
        {
            "Question" : "2. What is the main characteristics of living thing",
            "Options"  : ["A. Respiration", "B. Irritability", "C. Nutrition", "D. Movement"],
            "Answer"   : "C"
        },
        {   
            "Question" : "3. What is the function of Mitochondria",
            "Options" : ["A. Powerhouse of the cell", "B. Transportation of the cell", "C. Cell Defence", "D. Cell Destruction"],
            "Answer" : "A"
        },
        {   
            "Question" : "4. The blood cell which aid in body defence is ________",
            "Options" : ["A. Thrombin ", "B. Leukocyte", "C. Thrombokinase", "D. Erythrocyte"],
            "Answer" : "B"
        },
        {   
            "Question" : "5. The strongest part of the body is ______",
            "Options" : ["A. Femur", "B. Muscle", "C. Teeth", "D. Bone"],
            "Answer" : "C"
        }
    ]
    for trials in test:
        print(trials["Question"])
        print("")
        for option in trials["Options"]:
            print(option)
        answer = input("Enter your answer here: ")
        print("")


def Chemistry():
    """This is chemistry Question"""
    test = [
        {
            "Question" : "1. What is the chemical formula for water?",
            "Options"  : ["A. H₂O", "B. CO₂", "C. NaCl", "D. CH₄"],
            "Answer"   : "A"
        },
        {
            "Question" : "2. Which element is commonly used in batteries?",
            "Options"  : ["A. Gold", "B. Lithium", "C. Iron", "D. Helium"],
            "Answer"   : "B"
        },
        {   
            "Question" : "3. What is the pH of a neutral solution at 25°C?",
            "Options" : ["A. 1", "B. 7", "C. 14", "D. 0"],
            "Answer" : "B"
        },
        {   
            "Question" : "4. Which gas is used in the process of photosynthesis?",
            "Options" : ["A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Carbon Dioxide"],
            "Answer" : "D"
        },
        {   
            "Question" : "5. What is the primary component of natural gas?",
            "Options" : ["A. Ethanol", "B. Methane", "C. Propane", "D. Butane"],
            "Answer" : "B"
        }
    ]
    for trials in test:
        print(trials["Question"])
        print("")
        for option in trials["Options"]:
            print(option)
        answer = input("Enter your answer here: ")
        print("")


def Physics():
    """This is Physics Question"""
    test = [
        {
            "Question": "1. What is the unit of force in the International System of Units (SI)?",
            "Options": ["A. Joule", "B. Newton", "C. Watt", "D. Pascal"],
            "Answer": "B"
        },
        {
            "Question": "2. What is the acceleration due to gravity on the surface of the Earth?",
            "Options": ["A. 9.8 m/s²", "B. 10 m/s²", "C. 8.9 m/s²", "D. 9.0 m/s²"],
            "Answer": "A"
        },
        {
            "Question": "3. Which law states that for every action, there is an equal and opposite reaction?",
            "Options": ["A. Newton's First Law", "B. Newton's Second Law", "C. Newton's Third Law", "D. Law of Universal Gravitation"],
            "Answer": "C"
        },
        {
            "Question": "4. What is the speed of light in a vacuum?",
            "Options": ["A. 3 × 10^6 m/s", "B. 3 × 10^8 m/s", "C. 3 × 10^10 m/s", "D. 3 × 10^12 m/s"],
            "Answer": "B"
        },
        {
            "Question": "5. Which quantity is conserved in a closed system during an elastic collision?",
            "Options": ["A. Momentum", "B. Energy", "C. Mass", "D. Both A and B"],
            "Answer": "D"
        }
    ]
    for trials in test:
        print(trials["Question"])
        print("")
        for option in trials["Options"]:
            print(option)
        answer = input("Enter your answer here: ")
        print("")


def English():
    """This is English Question"""
    test = [
        {
                "Question": "1. What is the correct form of the verb in this sentence? 'She _____ to the store every Saturday.'",
                "Options": ["A. Goes", "B. Go", "C. Going", "D. Gone"],
                "Answer": "A"
            },
            {
                "Question": "2. Which of the following sentences is punctuated correctly?",
                "Options": ["A. 'Its raining outside,' she said.", "B. 'It's raining outside,' she said.", "C. 'Its raining outside' she said.", "D. 'It's raining outside', she said."],
                "Answer": "B"
            },
            {
                "Question": "3. Choose the word that is a synonym for 'happy':",
                "Options": ["A. Sad", "B. Joyful", "C. Angry", "D. Bored"],
                "Answer": "B"
            },
            {
                "Question": "4. In which sentence is the word 'affect' used correctly?",
                "Options": ["A. The weather can affect your mood.", "B. Her speech had a big affect on me.", "C. The affect of the new policy was noticeable.", "D. The movie had a strong affect on the audience."],
                "Answer": "A"
            },
            {
                "Question": "5. Identify the sentence with a grammatical error:",
                "Options": ["A. She don't like apples.", "B. He enjoys playing soccer.", "C. They are going to the park.", "D. I have read that book."],
                "Answer": "A"
            }
    ]
    for trials in test:
        print(trials["Question"])
        print("")
        for option in trials["Options"]:
            print(option)
        answer = input("Enter your answer here: ")
        print("")