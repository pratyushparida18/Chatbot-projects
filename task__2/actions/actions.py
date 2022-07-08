# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database_connectivity import DataUpdate
from datetime import datetime, timedelta



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        today = datetime.date(datetime.now())
        DataUpdate(tracker.get_slot("name"),tracker.get_slot("email"),today )
        dispatcher.utter_message("Thanks")

        return []
