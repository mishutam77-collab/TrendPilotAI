# BRAND: TrendMiha AI
# MAIN ORCHESTRATOR / BRAIN

from scout_agent import ScoutAgent
from analyst_core import AnalystAgent

def run_trend_pilot():
    print("=== [Brain] Запуск управляющей системы TrendMiha AI ===")
    print("Статус: Все системы активны. Поиск трендов запущен...\n")
    
    # 1. Запускаем Агента-Разведчика (Scout)
    scout = ScoutAgent()
    raw_trends = scout.fetch_trending_keywords()
    
    # 2. Передаем собранные данные Агенту-Аналитику (Analyst)
    analyst = AnalystAgent()
    final_analysis = analyst.analyze_trends(raw_trends)
    
    print("\n=== [Brain] Работа цепочки агентов завершена успешно ===")
    print(f"Итоговый отчет сформирован для дальнейшего прогнозирования спроса.")

if __name__ == "__main__":
    run_trend_pilot()
