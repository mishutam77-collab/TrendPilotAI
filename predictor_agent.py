# BRAND: TrendMiha AI
# AGENT 3: PREDICTOR ENGINE (ПРОГНОЗИСТ)

import random

class PredictorAgent:
    def __init__(self):
        self.name = "Predictor Agent"
        print(f"[{self.name}]: Инициализирован и готов к расчету математических моделей.")

    def forecast_demand(self, analyzed_trends):
        """
        Берет очищенные тренды от Аналитика и рассчитывает будущий спрос
        """
        print(f"\n[{self.name}]: Анализирую динамику и строю прогноз спроса на 30 дней вперед...")
        
        predictions = {}
        for trend in analyzed_trends:
            # Имитируем расчет: базовый рост + случайный фактор волатильности рынка
            base_growth = random.randint(15, 45)
            seasonality_factor = round(random.uniform(1.1, 1.5), 2)
            
            # Итоговый прогноз увеличения спроса в процентах
            predicted_increase = int(base_growth * seasonality_factor)
            
            predictions[trend] = {
                "predicted_growth_pct": predicted_increase,
                "risk_level": "Низкий" if predicted_increase < 40 else "Высокий (взрывной тренд)"
            }
            
            print(f"⚡ Тренд '{trend}': Ожидаемый рост спроса +{predicted_increase}% | Риск: {predictions[trend]['risk_level']}")
            
        return predictions
