from ai_helper import AIHelper
from api_fetcher import APIFetcher
from storage import Storage


def display_menu():
    print("\n========== AI LEARNING ASSISTANT ==========")
    print("1. Learn Topic")
    print("2. Generate Learning Roadmap")
    print("3. Fetch Programming Articles")
    print("4. View Learning History")
    print("5. Exit")
    print("===========================================")


def main():

    ai_helper = AIHelper()
    api_fetcher = APIFetcher()
    storage = Storage()

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            topic = input("\nEnter topic to learn: ")

            print("\nGenerating AI explanation...\n")

            explanation = ai_helper.explain_topic(topic)

            print(explanation)

            storage.save_history("AI Explanation", topic)

        elif choice == "2":

            topic = input("\nEnter topic for roadmap: ")

            print("\nGenerating learning roadmap...\n")

            roadmap = ai_helper.generate_roadmap(topic)

            print(roadmap)

            storage.save_history("Roadmap Generated", topic)

        elif choice == "3":

            tag = input("\nEnter programming topic (python/java/javascript): ")

            print("\nFetching latest articles...\n")

            articles = api_fetcher.fetch_articles(tag)

            print(articles)

            storage.save_history("Articles Fetched", tag)

        elif choice == "4":

            storage.view_history()

        elif choice == "5":

            print("\nThank you for using AI Learning Assistant!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
