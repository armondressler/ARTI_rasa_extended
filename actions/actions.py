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
        answer = self.askgpt(question=question)
        dispatcher.utter_message(text=f"You asked me: {tracker.latest_message['text']} and the answer is: {answer}")

        return []
    
    def askgpt(self, question, chat_log=None):
        if chat_log is None:
            chat_log = [{
                'role': 'system',
                'content': 'You are an it security expert',
            }]
        chat_log.append({'role': 'user', 'content': question})
        response = completion.create(model='gpt-3.5-turbo', messages=chat_log)
        answer = response.choices[0]['message']['content']
        chat_log.append({'role': 'assistant', 'content': answer})
        return answer