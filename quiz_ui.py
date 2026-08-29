import tkinter as tk
from tkinter import filedialog, messagebox
import json

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive JSON Quiz")
        self.root.geometry("650x550")
        self.root.configure(padx=20, pady=20, bg="#f4f4f9")
        
        # Application State Variables
        self.quiz_data = None
        self.current_index = 0
        self.score = 0
        
        self.show_start_screen()

    def clear_frame(self):
        """Clears all widgets from the main window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_start_screen(self):
        """Displays the initial screen to load a JSON file."""
        self.clear_frame()
        
        tk.Label(self.root, text="Welcome to the Quiz App", font=("Helvetica", 22, "bold"), bg="#f4f4f9", fg="#333").pack(pady=(60, 20))
        tk.Label(self.root, text="Load a JSON file to begin.", font=("Helvetica", 14), bg="#f4f4f9", fg="#666").pack(pady=(0, 40))
        
        load_btn = tk.Button(self.root, text="📁 Load JSON Quiz", font=("Helvetica", 14, "bold"), command=self.load_json, bg="#4CAF50", fg="white", padx=20, pady=10, cursor="hand2", borderwidth=0)
        load_btn.pack()

    def load_json(self):
        """Opens a file dialog to select and parse the JSON file."""
        filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if not filepath:
            return
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Validate JSON format
            if "quiz_title" not in data or "questions" not in data:
                raise ValueError("The JSON file must contain 'quiz_title' and 'questions'.")
            
            # Set state and start quiz
            self.quiz_data = data
            self.current_index = 0
            self.score = 0
            self.show_question()
            
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load quiz:\n\n{e}")

    def show_question(self):
        """Displays the current question and choices."""
        self.clear_frame()
        q = self.quiz_data["questions"][self.current_index]
        
        # Quiz Title
        tk.Label(self.root, text=self.quiz_data.get("quiz_title", "Quiz"), font=("Helvetica", 18, "bold"), bg="#f4f4f9", fg="#2C3E50").pack(pady=(0, 5))
        
        # Progress Tracker
        tk.Label(self.root, text=f"Question {self.current_index + 1} of {len(self.quiz_data['questions'])}", font=("Helvetica", 10, "italic"), bg="#f4f4f9", fg="#7F8C8D").pack(pady=(0, 20))
        
        # Question Text
        tk.Label(self.root, text=q["question"], font=("Helvetica", 14), bg="#f4f4f9", fg="#333", wraplength=600, justify="center").pack(pady=10)
        
        # Variable to store selected answer
        self.selected_answer = tk.StringVar(value="")
        
        # Choices Container
        choices_frame = tk.Frame(self.root, bg="#f4f4f9")
        choices_frame.pack(pady=10, fill="x", padx=40)
        
        for key in sorted(q["choices"].keys()):
            choice_text = f"{key}) {q['choices'][key]}"
            rb = tk.Radiobutton(choices_frame, text=choice_text, variable=self.selected_answer, value=key, font=("Helvetica", 12), bg="#f4f4f9", activebackground="#f4f4f9", wraplength=500, justify="left", cursor="hand2")
            rb.pack(anchor="w", pady=5)
            
        # Submit Button
        submit_btn = tk.Button(self.root, text="Submit Answer", font=("Helvetica", 12, "bold"), command=self.submit_answer, bg="#2980B9", fg="white", padx=20, pady=10, cursor="hand2", borderwidth=0)
        submit_btn.pack(pady=30)

    def submit_answer(self):
        """Evaluates the user's answer and moves to the next screen."""
        ans = self.selected_answer.get()
        if not ans:
            messagebox.showwarning("Warning", "Please select an answer before submitting!")
            return
            
        correct_ans = self.quiz_data["questions"][self.current_index]["answer"]
        
        # Feedback Pop-up
        if ans == correct_ans:
            messagebox.showinfo("Result", "✅ Correct!")
            self.score += 1
        else:
            correct_text = self.quiz_data["questions"][self.current_index]["choices"][correct_ans]
            messagebox.showerror("Result", f"❌ Incorrect.\n\nThe correct answer was:\n{correct_ans}) {correct_text}")
            
        # Move forward
        self.current_index += 1
        if self.current_index < len(self.quiz_data["questions"]):
            self.show_question()
        else:
            self.show_results()
            
    def show_results(self):
        """Displays the final score and options to restart."""
        self.clear_frame()
        total = len(self.quiz_data["questions"])
        
        tk.Label(self.root, text="Quiz Completed!", font=("Helvetica", 22, "bold"), bg="#f4f4f9", fg="#2C3E50").pack(pady=(60, 20))
        tk.Label(self.root, text=f"Your Final Score: {self.score} / {total}", font=("Helvetica", 18), bg="#f4f4f9", fg="#333").pack(pady=10)
        
        # Calculate percentage for dynamic feedback
        pct = (self.score / total) * 100
        msg = "🏆 Outstanding!" if pct >= 80 else "👍 Good effort!" if pct >= 50 else "📚 Keep reviewing!"
        tk.Label(self.root, text=msg, font=("Helvetica", 16), bg="#f4f4f9", fg="#7F8C8D").pack(pady=10)
        
        restart_btn = tk.Button(self.root, text="Load Another Quiz", font=("Helvetica", 14, "bold"), command=self.show_start_screen, bg="#27AE60", fg="white", padx=20, pady=10, cursor="hand2", borderwidth=0)
        restart_btn.pack(pady=40)

if __name__ == "__main__":
    root = tk.Tk()
    # Optional: Make the window non-resizable for a fixed, clean layout
    root.resizable(False, False)
    app = QuizApp(root)
    root.mainloop()
