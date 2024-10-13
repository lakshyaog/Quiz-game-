class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_questions(self):
        for question in self.questions:
            print(question['question'])
            for idx, option in enumerate(question['options']):
                print(f"{idx + 1}. {option}")
            answer = input("Your answer (1-4): ")
            if question['options'][int(answer) - 1] == question['answer']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question['answer']}\n")

    def show_score(self):
        print(f"Your final score is: {self.score}/{len(self.questions)}")


def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "What is the largest planet in our Solar System?",
            "options": ["Earth", "Jupiter", "Mars", "Saturn"],
            "answer": "Jupiter"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "NaCl"],
            "answer": "H2O"
        },
        {    "question": "what is the capital of India?",
             "options":  ["Agra","Delhi","Kanpur","Mumbai"], 
             "answer": "Delhi"
        },
        {    "question":  "what type of language python is?",
             "options":  ["High level","Low level", "Machine level", "Middle level"],
             "answer":  "High level"
            
            
        },
    ]

    quiz = Quiz(questions)
    quiz.ask_questions()
    quiz.show_score()


if __name__ == "__main__":
    main()
