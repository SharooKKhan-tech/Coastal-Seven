import json
import os
from datetime import datetime


class Storage:

    def __init__(self):

        self.file_name = "history.json"

    def load_history(self):

        if not os.path.exists(self.file_name):
            return []

        try:

            with open(self.file_name, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []

    def save_history(self, activity, topic):    

        history = self.load_history()

        new_entry = {
            "activity": activity,
            "topic": topic,
            "date": str(datetime.now())
        }

        history.append(new_entry)

        with open(self.file_name, "w") as file:
            json.dump(history, file, indent=4)

    def view_history(self):

        history = self.load_history()

        if not history:
            print("\nNo learning history found.")
            return

        print("\n========== LEARNING HISTORY ==========")

        for index, item in enumerate(history, start=1):

            print(f"{index}. Activity: {item['activity']}")
            print(f"   Topic: {item['topic']}")
            print(f"   Date: {item['date']}")
            print()