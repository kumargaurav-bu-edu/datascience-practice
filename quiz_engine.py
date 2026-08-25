import json
import os
import time

def load_quiz_data(file_path):
    """Loads and validates the quiz JSON file."""
    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' does not exist.")
        return None
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            # Basic validation of the JSON structure
            if "quiz_title" not in data or "questions" not in data:
                print("❌ Error: Invalid JSON structure. Must contain 'quiz_title' and 'questions'.")
                return None
            return data
            
    except json.JSONDecodeError:
        print("❌ Error: The file is not a valid JSON. Please check syntax (commas, quotes, etc.).")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return None

def run_quiz(quiz_data):
    """Executes the interactive quiz using the loaded data."""
    title = quiz_data.get("quiz_title", "Generic Quiz")
    description = quiz_data.get("quiz_description", "")
    questions = quiz_data.get("questions", [])
    
    score = 0
    total_questions = len(questions)

    print("=" * 60)
    print(f"🧠 {title.upper()} 🧠")
    if description:
        print(description)
    print("=" * 60 + "\n")
    time.sleep(1)

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        
        # Display choice key-value pairs sorted alphabetically
        choices = q["choices"]
        for key in sorted(choices.keys()):
            print(f"  {key}) {choices[key]}")
            
        # Get and sanitize user input
        while True:
            user_answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()
            if user_answer in choices.keys():
                break
            print(f"⚠️ Invalid choice. Please select from: {', '.join(sorted(choices.keys()))}")

        # Evaluate the answer
        correct_answer = q["answer"].upper()
        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was: {correct_answer} ({choices[correct_answer]})\n")
        
        print("-" * 60)
        time.sleep(0.5)

    # Final Score Synthesis
    print("\n" + "=" * 60)
    print(f"Quiz Complete! Your final score is {score}/{total_questions}.")
    
    percentage = (score / total_questions) * 100
    if percentage == 100:
        print("🏆 Perfect score! Masterful job!")
    elif percentage >= 70:
        print("👍 Great job! You have a solid understanding.")
    else:
        print("📚 Keep studying! Review the material and try again.")
    print("=" * 60)

if __name__ == "__main__":
    # Ask the user which quiz JSON file they want to load
    print("📋 Reusable Quiz Engine")
    file_path = input("Enter the path/name of your quiz JSON file (e.g., nn_quiz.json): ").strip()
    
    # Automatically add .json if the user forgot it
    if not file_path.endswith('.json'):
        file_path += '.json'
        
    quiz_data = load_quiz_data(file_path)
    if quiz_data:
        run_quiz(quiz_data)
