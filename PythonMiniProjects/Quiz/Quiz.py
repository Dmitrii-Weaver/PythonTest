#console based quiz game with a timer

import time
import threading

class QuizGame:
    def __init__(self, questions):
        self.questions = questions  
        self.score = 0              
        self.time_out = False       

    def start_quiz(self):
        for question in self.questions:
            self.ask_question(question)
        self.display_final_score()

    def ask_question(self, question):
        self.time_out = False

        timer = threading.Thread(
            target=self.countdown, args=(question["time_limit"],))
        timer.start()

        print(f"\nQuestion: {question['question']}")
        for index, option in enumerate(question['options']):
            print(f"{index + 1}. {option}")

        answer = None

        while answer is None:
            try:
                if self.time_out:
                    break
                answer = int(input("\nSelect an option (1-4): "))
                if answer not in [1, 2, 3, 4]:
                    raise ValueError("Invalid option")
                break  
            except ValueError as e:
                print(e)
                answer = None

        if self.time_out:
            print("Time's up!")
        else:
            if question['options'][answer - 1] == question['correct']:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")

        timer.join() 

    def countdown(self, time_limit):
        print(f"\nYou have {time_limit} seconds to answer this question.")
        time.sleep(time_limit)
        self.time_out = True  

    def display_final_score(self):
        print(
            f"\nQuiz Over! Your final score is: {self.score}/{len(self.questions)}")


questions = [
    {"question": "What is the capital of France?", "options": [
        "Berlin", "Madrid", "Paris", "Rome"], "correct": "Paris", "time_limit": 7},
    {"question": "Which planet is known as the Red Planet?", "options": [
        "Earth", "Mars", "Jupiter", "Venus"], "correct": "Mars", "time_limit": 7},
    {"question": "What is the largest ocean on Earth?", "options": [
        "Atlantic", "Indian", "Pacific", "Arctic"], "correct": "Pacific", "time_limit": 7},
]

if __name__ == "__main__":
    quiz = QuizGame(questions)
    quiz.start_quiz()
