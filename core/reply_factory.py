
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id, session)

    if not success:
        return [error]

    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses


def record_current_answer(self,answer, current_question_id, session):
    if not self.validate_answer(answer):
        return "Invalid answer.Please try again."

    if current_question_id not in self.user_responses:
        self.user_responses[current_question_id] = []

    self.user_responses[current_question_id].append(answer)
    return True, " Answer Recorded"


def get_next_question(self,current_question_id):
    current_index = self.current_question_index.get(current_question_id, 0)

    if current_index >= len(self.questions):
        return None

    question = self.questions[current_index]
    self.current_question_index[current_question_id] = current_index + 1

    return question


def generate_final_response(self,session,current_question_id):
    responses = self.user_responses.get(current_question_id, [])
    score = self.calculate_score(responses)
    tatal_questions = len(self.questions)    

    return f"You scored {score} out of {tatal_questions}."


def calculate_score(self, responses):
    score = 0
    for res in responses:
        if self.is_correct(res):
            score += 1
    return score 
