# This is CBT Question

print("WELCOME TO ADEBAYO CBT TEST")
print("The question is 50 in total. ")
print("Biology contain 20 questions while English, Physics and Chemistry contain 10 questions each") 
print("""
INSTRUCTIONS:
  1. Use A, B, C and D to choose your option
  2. Do not choose two option as it will cancel the mark of the question
  3. Do not engange in Examination Malpractice. 
""")
print("Enter start to begin")
reply = input().upper()
score = 0



print("")
def biology():
    print("You are given type S")
    test =[
        {
            "Question" : "1. What question type is given to you",
            "Options"  : ["A. D", "B. H", "C. Y", "D. S"],
            "Answer"   : "D"
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
            "Options" : ["A.Thrombin ", "B. Leukocyte", "C. Thrombokinase", "D. Erythrocyte"],
            "Answer" : "B"
        },
        {   
            "Question" : "5. The strongest part of the body is ______",
            "Options" : ["A. Femur", "B. Muscle", "C. Teeth", "D. Bone"],
            "Answer" : "C"
        },
        {   
            "Question" : "6. The function of Red Blood Cell is _____",
            "Options" : ["A. Transportation of O2", "B. Transportation of Cl2", "C. Transportation of N3", "D. Transportation of K+"],
            "Answer" : "A"
        },
        {   
            "Question" : "7. _______ convert inactive Fibrinogen to active Fibrin",
            "Options" : ["A. Mesh", "B. Thrombin", "C. Blood Platelet", "D. Niacin"],
            "Answer" : "B"
        },
        {   
            "Question" : "8. Another name of for Red Blood Cell is ?",
            "Options" : ["A. Leukocyte", "B. Porkayotic", "C. Thrombocyte", "D. Erythrocyte"],
            "Answer" : "D"
        },
        {   
            "Question" : "9. The smallest unit of life is ?",
            "Options" : ["A. Atom", "B. Cell", "C. Molecule", "D. Organelle"],
            "Answer" : "B"
        },
        {   
            "Question" : "10. What houses the fucntional pary of hereditry",
            "Options" : ["A. DNA", "B. Cytoplasm", "C. Nucleus", "D. Cell"],
            "Answer" : "A"
        },
        {   
            "Question" : "11. What controls the activities of the cell",
            "Options" : ["A. Cytoplasm", "B. Nucleolus", "C. Nucleus", "D. Cell Membrane"],
            "Answer" : "C"
        },
        {   
            "Question" : "12. Which organism is the most ancient among all",
            "Options" : ["A. Termite", "B. Hydra", "C. Snail", "D. Sponges"],
            "Answer" : "D"
        },
        {   
            "Question" : "13. The characteristics of Echinodermata is _____",
            "Options" : ["A.No Mouth with No eyes", "B. No head with No brian", "C. No leg with No hand", "D. No ear with No Nose"],
            "Answer" : "B"
        },
        {   
            "Question" : "14. What ion aid in formation of strong bone?",
            "Options" : ["A. Ca+", "B. Ca2+", "C. Cl-", "D. N3-"],
            "Answer" : "A"
        },
        {   
            "Question" : "15. Which hormone is called fight or flight hormone",
            "Options" : ["A. Toxin", "B. Auxin", "C. Throxin", "D. Aderaline"],
            "Answer" : "D"
        },
        {   
            "Question" : "16. The highest Organizaton of life is ______",
            "Options" : ["A. Biosphere", "B. Ecosystem", "C. System", "D. Organism"],
            "Answer" : "A"
        },
        {   
            "Question" : "17. The father of classification is?",
            "Options" : ["A. Carolous Lineaus", "B. Carrolous Linneaus", "C. James Chardwick", "D. Carolous Linnaeus"],
            "Answer" : "D"
        },
        {   
            "Question" : "18. Who introduced binomial system of numenclature",
            "Options" : ["A. Carolous Lineaus", "B. Carrolous Linneaus", "C. James Chardwick", "D. Carolous Linnaeus"],
            "Answer" : "D"
        },
        {   
            "Question" : "19. What perform osmoregulation in Paramecium",
            "Options" : ["A. Contractile Vacuole", "B. Cillia", "C. Flagella", "D. Trichocysts"],
            "Answer" : "A"
        },
        {   
            "Question" : "20. The following are use for locomotion except?",
            "Options" : ["A. Flagella", "B. Trichocysts", "C. Cillia", "D. Pseudopodia"],
            "Answer" : "B"
        },
    ]
    
    for questions in test:
        print(questions["Question"])
        for option in questions["Options"]:
            print(option)
    
        answer = input("Your answer (A, B, C or D): ").upper()
        if answer == questions["Answer"]:
            print("Wow, you get get the question right")
            global score  
            score +=1
        elif answer == "":
            print("No, the correct answer is",questions["Answer"])
        else:
            print("No, the correct answer is",questions["Answer"])

def chemistry():
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
        },
        {   
            "Question" : "6. Which element is known for its role in making steel?",
            "Options" : ["A. Copper", "B. Carbon", "C. Silver", "D. Lead"],
            "Answer" : "B"
        },
        {   
            "Question" : "7. What is the process of converting a solid directly into a gas called?",
            "Options" : ["A. Melting", "B. Sublimation", "C. Condensation", "D. Evaporation"],
            "Answer" : "B"
        },
        {   
            "Question" : "8. Which acid is found in vinegar?",
            "Options" : ["A. Sulfuric Acid", "B. Hydrochloric Acid", "C. Acetic Acid", "D. Nitric Acid"],
            "Answer" : "C"
        },
        {   
            "Question" : "9. What is the name of the reaction in which a substance combines with oxygen to form oxides?",
            "Options" : ["A. Decomposition", "B. Combustion", "C. Neutralization", "D. Precipitation"],
            "Answer" : "B"
        },
        {   
            "Question" : "10. Which of the following is a noble gas?",
            "Options" : ["A. Nitrogen", "B. Oxygen", "C. Argon", "D. Hydrogen"],
            "Answer" : "C"
        },
    ]
    for questions in test:
        print(questions["Question"])
        for option in questions["Options"]:
            print(option)
        
        answer = input("Your answer (A, B, C or D): ").upper()
        if answer == questions["Answer"]:
            print("Wow, you get get the question right")
            global score
            score +=1
        elif answer == "":
            print("No, the correct answer is",questions["Answer"])
        else:
            print("No, the correct answer is",questions["Answer"])


def english():
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
            },
            {
                "Question": "6. Which sentence correctly uses a semicolon?",
                "Options": ["A. I have a big test tomorrow; I can't go out tonight.", "B. I have a big test tomorrow; and I can't go out tonight.", "C. I have a big test tomorrow; but I can't go out tonight.", "D. I have a big test tomorrow; however I can't go out tonight."],
                "Answer": "A"
            },
            {
                "Question": "7. What is the main theme of William Shakespeare's play 'Macbeth'?",
                "Options": ["A. Love and friendship", "B. Ambition and power", "C. The American Dream", "D. Family and loyalty"],
                "Answer": "B"
            },
            {
                "Question": "8. What type of literary device is used in the following sentence: 'The wind whispered through the trees'?",
                "Options": ["A. Metaphor", "B. Simile", "C. Personification", "D. Hyperbole"],
                "Answer": "C"
            },
            {
                "Question": "9. Which of the following sentences contains an example of alliteration?",
                "Options": ["A. She sells sea shells by the sea shore.", "B. The wind blew through the trees.", "C. The book was very interesting.", "D. He quickly ran across the field."],
                "Answer": "A"
            },
            {
                "Question": "10. Which word is the antonym of 'brave'?",
                "Options": ["A. Fearful", "B. Confident", "C. Courageous", "D. Bold"],
                "Answer": "A"
            }
        ]
        for questions in test:
            print(questions["Question"])
        for option in questions["Options"]:
            print(option)
        
        answer = input("Your answer (A, B, C or D): ").upper()
        if answer == questions["Answer"]:
            print("Wow, you get get the question right")
            global score
            score +=1
        elif answer == "":
            print("No, the correct answer is",questions["Answer"])
        else:
            print("No, the correct answer is",questions["Answer"])

                        
def physics():
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
        },
        {
            "Question": "6. What type of lens is used to correct hyperopia (farsightedness)?",
            "Options": ["A. Concave Lens", "B. Convex Lens", "C. Cylindrical Lens", "D. Bifocal Lens"],
            "Answer": "B"
        },
        {
            "Question": "7. What is the phenomenon where light bends as it passes from one medium to another?",
            "Options": ["A. Reflection", "B. Refraction", "C. Diffraction", "D. Dispersion"],
            "Answer": "B"
        },
        {
            "Question": "8. Which of the following is not a form of energy?",
            "Options": ["A. Kinetic Energy", "B. Potential Energy", "C. Thermal Energy", "D. Magnetic Field"],
            "Answer": "D"
        },
        {
            "Question": "9. In a circuit, what is the unit of electrical resistance?",
            "Options": ["A. Volt", "B. Ampere", "C. Ohm", "D. Watt"],
            "Answer": "C"
        },
        {
            "Question": "10. What is the principle behind the operation of a hydraulic lift?",
            "Options": ["A. Archimedes' Principle", "B. Pascal's Principle", "C. Bernoulli's Principle", "D. Coulomb's Law"],
            "Answer": "B"
        },
    ]
    
    for questions in test:
        print(questions["Question"])
        for option in questions["Options"]:
            print(option)
        answer = input("Your answer (A, B, C or D): ").upper()
        if answer == questions["Answer"]:
            print("Wow, you got the question right")
            global score
            score += 1
        elif answer == "":
            print("No, the correct answer is",questions["Answer"])
        else:
            print("No, the correct answer is", questions["Answer"])
            
    print("Your final score in Physics is", score)        
if reply == "START":
    print("Which subject will you start with(Biology, Physics, Chemistry or English)")
    subject = input().upper()

    if subject == "BIOLOGY":
        biology()
    elif subject == "PHYSICS":
        physics()
    elif subject == "CHEMISTRY":
        chemistry()
    elif subject == "ENGLISH":
        english()
else:
    print("You enter an invalid input")

print(score)