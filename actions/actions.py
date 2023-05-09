from typing import Any, Text, Dict, List
import os

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.ChatCompletion()

class InfosecQuiz(Action):

    def name(self) -> Text:
        return "infosec_follow_up"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        if len(question) < 10:
            dispatcher.utter_message(text=f"Your request could not be processed, please provide more details.")
            return []
        question = f"{question} Please answer in 200 words or less."
        try:
            answer = self.askgpt(question=question)
        except openai.error.RateLimitError as err:
            answer = f"I asked ChatGPT for hints but it told me you haven't paid your bills :( ({err})"
        dispatcher.utter_message(text=f"(Forwarded to openAI): {answer}")
        return []
        
    
    def askgpt(self, question, chat_log=None):
        if chat_log is None:
            chat_log = [{
                'role': 'system',
                'content': 'You are an it security expert.',
            }]
        chat_log.append({'role': 'user', 'content': question})
        response = completion.create(model='gpt-3.5-turbo', messages=chat_log)
        answer = response.choices[0]['message']['content']
        chat_log.append({'role': 'assistant', 'content': answer})
        return answer