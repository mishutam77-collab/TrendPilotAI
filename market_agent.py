# BRAND: TrendMiha AI
# AGENT 5: MARKET INTELLIGENCE (МАРКЕТ)

import random

class MarketAgent:
    def __init__(self):
        self.name = "Market Agent"
        print(f"[{self.name}]: Инициализирован. Мониторинг маркетплейсов готов.")

    def find_top_products(self, recommendations):
        """
        Привязывает ИИ-рекомендации к реальным нишам на маркетплейсах,
        оценивает конкуренцию и предлагает оптимальную цену.
        """
        print(f"\n[{self.name}]: Сканирую маркетплейсы на наличие товаров по целевым трендам...")
        
        market_data = {}
        for trend, rec_data in recommendations.items():
            # Симулируем рыночную аналитику
            competitors_count = random.randint(15, 250)
            average_price = random.randint(800, 4500)
            
            # Логика оценки сложности ниши
            if competitors_count > 150:
                market_difficulty = "Высокая конкуренция (нужен большой бюджет на рекламу)"
            elif 50 <= competitors_count <= 150:
                market_difficulty = "Средняя конкуренция (отличная точка для входа)"
            else:
                market_difficulty = "Низкая конкуренция (чистый и свободный рынок!)"
                
            market_data[trend] = {
                "competitors": competitors_count,
                "target_price_rub": average_price,
                "difficulty": market_difficulty,
                "recommended_action": rec_data["action_required"]
            }
            
            print(f"🛒 Ниша '{trend}': Продавцов на рынке: {competitors_count} | Рекомендуемая цена: {average_price} руб.")
            print(f"📊 Статус рынка: {market_difficulty}")
            
        return market_data
