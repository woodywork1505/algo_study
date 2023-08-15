def ask_question(question, option1, option2):
    print(question)
    print(f"1: {option1}")
    print(f"2: {option2}")

    while True:
        try:
            answer = int(input("Choose 1 or 2: "))
            if answer in [1, 2]:
                return answer
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("Please enter a number (1 or 2).")

def mbti_test():
    result = ""

    print("MBTI Personality Test\n")

    # E vs I
    answer = ask_question("Do you prefer being in large groups or socializing in busy places?", "Yes", "No")
    result += "E" if answer == 1 else "I"

    # S vs N
    answer = ask_question("Do you focus more on real-world facts or do you often think about possibilities and what might be?", "Real-world facts", "Possibilities")
    result += "S" if answer == 1 else "N"

    # T vs F
    answer = ask_question("When making decisions, do you tend to prioritize logic over emotions?", "Yes", "No")
    result += "T" if answer == 1 else "F"

    # J vs P
    answer = ask_question("Do you prefer to have things decided and planned, or are you more spontaneous?", "Decided and planned", "Spontaneous")
    result += "J" if answer == 1 else "P"

    return result

personality_type = mbti_test()
print(f"\nYour MBTI personality type is: {personality_type}")

# You can expand upon this with more detailed questions and descriptions for each type.