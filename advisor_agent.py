# BRAND: TrendMiha AI
# AGENT 4: ADVISOR ENGINE (СОВЕТНИК)

class AdvisorAgent:
    def __init__(self):
        self.name = "Advisor Agent"
        print(f"[{self.name}]: Инициализирован и готов генерировать бизнес-рекомендации.")

    def generate_recommendations(self, predictions):
        """
        Берет математические прогнозы от Прогнозиста и превращает их в понятные советы для бизнеса
        """
        print(f"\n[{self.name}]: Формирую стратегические рекомендации на основе ИИ-прогнозов...")
        
        recommendations = {}
        for trend, data in predictions.items():
            growth = data["predicted_growth_pct"]
            
            # Логика принятия решений на основе силы тренда
            if growth >= 50:
                advice = "🔥 КРИТИЧЕСКИЙ ТРЕНД! Срочно закупать товар большими партиями, запускать рекламу и выводить карточку в топ."
                action = "Максимальный закуп"
            elif 30 <= growth < 50:
                advice = "📈 Стабильный рост. Рекомендуется умеренный закуп тестовой партии и оптимизация SEO-ключей."
                action = "Тестовый закуп"
            else:
                advice = "⏱ Слабый или угасающий тренд. Не вкладывать большие бюджеты, распродавать текущие остатки."
                action = "Наблюдение / Распродажа"
            
            recommendations[trend] = {
                "advice": advice,
                "action_required": action
            }
            
            print(f"📋 Для тренда '{trend}': {advice}")
            
        return recommendations
