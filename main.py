
# BRAND: TrendMiha AI
# MAIN ORCHESTRATOR / BRAIN (FULL ORCHESTRA VERSION)

from scout_agent import ScoutAgent
from analyst_core import AnalystAgent
from predictor_agent import PredictorAgent
from advisor_agent import AdvisorAgent
from market_agent import MarketAgent

def run_trend_pilot():
    print("=== [Brain] Запуск ПОЛНОЙ управляющей системы TrendMiha AI ===")
    print("Статус: Все 5 ИИ-агентов подключены. Запуск сквозного анализа...\n")
    
    # 1. Запускаем Агента-Разведчика (Scout)
    scout = ScoutAgent()
    raw_trends = scout.fetch_trending_keywords()
    
    # 2. Передаем собранные данные Агент-Аналитику (Analyst)
    analyst = AnalystAgent()
    final_analysis = analyst.analyze_trends(raw_trends)
    
    # 3. Передаем очищенные тренды Агенту-Прогнозисту (Predictor)
    predictor = PredictorAgent()
    predictions = predictor.forecast_demand(final_analysis)
    
    # 4. Передаем прогнозы Агенту-Советнику (Advisor)
    advisor = AdvisorAgent()
    recommendations = advisor.generate_recommendations(predictions)
    
    # 5. Финализируем анализ через Агента-Маркета (Market)
    market = MarketAgent()
    final_market_data = market.find_top_products(recommendations)
    
    print("\n=== [Brain] РАБОТА ВСЕЙ ЦЕПОЧКИ АГЕНТОВ ЗАВЕРШЕНА УСПЕШНО ===")
    print("Система TrendMiha AI полностью готова к поиску прибыльных товаров! 🚀")

if __name__ == "__main__":
    run_trend_pilot()
