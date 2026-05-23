import requests


class APIFetcher:

    def __init__(self):

        self.api_key = "3fa07b12a601425d93c9d18ee5808374"

    def fetch_articles(self, topic):

        query = f"{topic} AND (software OR programming OR AI OR technology)"

        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={query}&"
            f"language=en&"
            f"sortBy=publishedAt&"
            f"apiKey={self.api_key}"
        )

        try:

            response = requests.get(url, timeout=20)

            response.raise_for_status()

            data = response.json()

            articles = data.get("articles", [])

            if not articles:
                return "No tech articles found."

            result = "\n========== TECH ARTICLES ==========\n\n"

            for index, article in enumerate(articles[:5], start=1):

                title = article["title"]
                source = article["source"]["name"]
                link = article["url"]

                result += f"Article {index}\n"
                result += f"Title  : {title}\n"
                result += f"Source : {source}\n"
                result += f"Link   : {link}\n"
                result += "-" * 50 + "\n"

            return result

        except Exception as e:
            return f"Error fetching articles: {e}"