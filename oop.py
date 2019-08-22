from collections import namedtuple

ALPHABET = ["a", "b", "c", "d", "e","f","g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class Person:
	def __init__(self, name, phone_number):
		self.name = name
		self.phone_number = phone_number


class Question:
    def __init__(self, question, answer, choices=[]):
        self.question = question
        self.answer = answer
        self.choices = {key: value for key, value in zip(ALPHABET, choices)}
    
    def __str__(self):
        return self.question

    def __repr__(self):
        return f"<Question: {str(self)}>"

    def check_answer(self, key):
        try:
            return self.choices[key] == self.answer 
        except KeyError:
            raise KeyError(f"The choice '{key}' is not available.")
    
    def to_dict(self):
        return {
            'question': self.question,
            'choices': self.choices,
            'answer': self.answer
        }


class Quiz:
    def __init__(self, name, questions=[]):
        self.name = name
        self.questions = questions

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Quiz: {str(self)}>"

    def __len__(self):
        return len(self.questions)
    
    def __iter__(self):
        for question in self.questions:
            yield question
            
    def add_question(self, question):
        self.questions.append(question)
        return question
    
    def to_dict(self): 
        questions_array = {self.name: [question.to_dict()
                              for question in self.questions]}
        questions_dict = questions_array['Test']
        return {i: value for i, value in enumerate(questions_dict, start=1)}

        def marking_scheme(self):
        	the_quiz = self.to_dict()

class QuizTaker:
    def __init__(self, quiz, student, graded_by):
        self.quiz = quiz
        self.student = student
        self.graded_by = graded_by
        self.responses = dict()

    def __str__(self):
        return f"{self.quiz.name}: {self.student.name}"

    def __repr__(self):
        return f"<QuizTaker: {str(self)}>"

    def __len__(self):
        return len(self.responses)

    def respond(self, question, choice):
        self.responses[question] = choice
        return choice

    def get_report(self):
        questions_answered = len(self.responses)
        questions_passed = len([question for question, choice in self.responses.items()
                                if question.check_answer(choice)])
        questions_skipped = len(self.quiz) - questions_answered
        Report = namedtuple("Report", ["student", "graded_by", "questions_passed",
                                       "questions_skipped", "questions_answered"])
        return Report(self.student, self.graded_by, questions_passed, questions_skipped,
                      questions_answered)


class Teacher(Person):
	@classmethod
	def create_quiz(cls, test_name, questions):
		return Quiz(
			test_name=test_name,
			questions=questions)

	@classmethod
	def assign_quiz(cls, quiz, students):
		quiz.students = students
		return 'The following students {} have been assigned to this quiz {}'.format(  #noqa
			*students, quiz.test_name)

	def grade_quiz(self, student_quiz, grade):
		student_quiz.grade = grade
		student_quiz.graded_by = self.name
		return 'Student {} scored grade {} in {} test'.format(
			student_quiz.name, student_quiz.grade, student_quiz.test_name)


class Student(Person):
	def __init__(self, name, phone_number, student_number):
		super(Student, self).__init__(name, phone_number)
		self.student_number = student_number


class StudentQuiz:
	def __init__(self, quiz_name, student_name):
		self.test_name = quiz_name
		self.student_name = student_name
		self.answers = dict()

	def add_answers(self, **kwargs):
		current_answers = self.answers
		current_answers.update(kwargs)
		self.answers = current_answers
		return self.answers


class Lessons:
	def __init__(self, lesson_name, teacher_name, students=[]):
		self.lesson_name = lesson_name
		self.teacher_name = teacher_name
		self.students = students

	def update_class(self, **kwargs):
		if 'lesson_name' or 'teacher_name' or 'students' in kwargs:
			for key, value in kwargs.items():
				setattr(self, key, value)
			return '{} has been updated to {}'.format(key, value)
