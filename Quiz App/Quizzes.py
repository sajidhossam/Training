import json

class QuizApp:
    def __init__(self):
        self.questions = [
            {
                "question": "what is the capital of france?",
                "choices":["A. paris","B. Berlin","C. Cairo", "D.  London"],
                "answer": "A"
            },
            {
                "question": "What is 2 + 2?",
                "choices": ["A. 3", "B. 4", "C. 5", "D. 6"],
                "answer": "B"
            },
            {
                "question": "What is the largest planet in our Solar System?",
                "choices": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
                "answer": "B"
            }

        ]
        self.user_answer = []

    def display_question(self,question_data):
        print(question_data["question"])
        for choice in question_data["choices"]:
            print(choice)
    
    def  get_user_answer(self):
        answer = input("Plaese input the letter of your answer: ").strip().upper()
        return answer
    
    def check_answer(self, question_data, user_answer):
        if user_answer == question_data["answer"]:
            return True
        else:
            return False
    
    def run_quiz(self):
        score = 0
        total_question = len(self.questions)

        for question_data in self.questions:
            self.display_question(question_data)
            user_answer = self.get_user_answer()

            if self.check_answer(question_data, user_answer):
                print("Correct!")
                score += 1
            else:
                print(f"incorrect the right answer is {question_data["answer"]}.")

                self.user_answer.append(
                    {
                        "question" : question_data["answer"],
                        "user_answer" : user_answer,
                        "correct_answer" : question_data["answer"]

                    })
        print(f"Quiz Completed, Your score is {score}/{total_question}")

    def save_result(self, filename="quiz_result.json"):
        results = {
            "score" : sum(1 for ans in self.user_answer if ans['user_answer']== ['correct_answer']),
            "total_question" : len(self.questions),
            "user_answer" : self.user_answer
        }

        with open(filename, "w") as file:
            json.dump(results, file, indent=4)
        print(f"Result saved to {filename}")

if __name__ == "__main__":
    quiz_app = QuizApp()
    quiz_app.run_quiz()
    quiz_app.save_result()