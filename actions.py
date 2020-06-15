# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import random




class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        return []


class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name", "email"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "name": [self.from_entity(entity="name", intent=None),
                     self.from_text()],

            "email": [self.from_entity(entity="email", intent=None),
                      self.from_text()]
        }

    # regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    # def check(
    #         email,
    #         dispatcher: "CollectingDispatcher",
    #         tracker: "Tracker",
    #         domain: Dict[Text, Any],
    # )-> List[Dict]:
    #
    #     if (re.search(regex, email)):
    #         print("Valid Email")
    #     else:
    #         print("Invalid Email")
    #     # return [dispatcher.utter_message(email=tracker.get_slot('email'))]

    def submit(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        n = random.randint(0, 999)
        dispatcher.utter_message("ID is : " + str(n))
        dispatcher.utter_message(template='utter_submit', name=tracker.get_slot('name'),
                                email=tracker.get_slot('email'))

        return []
