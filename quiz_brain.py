 class QuizBrain:

      def __init__(self,question_list):

           self.question_number = 0
           self.qn = question_list

      def next_question(self):
          current_question = self.qn[self.question_number]
          input(f"Q.{self.question_number}:{current_question.text} (True/False) ")



