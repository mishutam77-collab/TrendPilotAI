
import random

class ScoutAgent:
    def __init__(self, name="TrendScout"):
        self.name = name
        # Источники для сбора данных
        self.sources = ["Twitter", "Google Trends", "Reddit", "Marketplace"]

    def fetch_trending_keywords(self):
        print(f"{self.name} начал сканирование трендов...")
        # Имитация получения данных
        data = [
            {"query": "искусственный интеллект", "source": random.choice(self.sources), "volume": random.randint(500, 5000)},
            {"query": "разработка на Python", "source": random.choice(self.sources), "volume": random.randint(200, 2000)}
        ]
        return data

# Тест работы разведчика
if __name__ == "__main__":
    scout = ScoutAgent()
    trends = scout.fetch_trending_keywords()
    print(f"Разведчик нашел: {trends}")
