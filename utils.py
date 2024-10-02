import logging
import os
from datetime import datetime

# Создаем директорию для логов, если она не существует
os.makedirs('logs', exist_ok=True)

# Настройка логирования
log_file = os.path.join('logs', 'utils.log')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
    filename=log_file,
    filemode='w'  # 'w' для перезаписи лога
)

logger = logging.getLogger(__name__)


def filter_by_state(data: list, state="EXECUTED"):
    """Функция, которая фильтрует список словарей по ключу state"""
    logger.debug(f"Filtering data by state: {state}")
    filtered_data = [item for item in data if item.get("state") == state]
    logger.info(f"Filtered data length: {len(filtered_data)}")
    return filtered_data


def sort_by_date(data: list, descending=True):
    """Функция, которая сортирует список по дате (по умолчанию — по убыванию)"""
    logger.debug("Sorting data by date.")
    sorted_data = sorted(
        data,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=descending
    )
    logger.info(f"Sorted data length: {len(sorted_data)}")
    return sorted_data


if __name__ == '__main__':
    # Пример данных
    sample_data = [
        {"date": "2022-02-01T10:00:00", "state": "EXECUTED"},
        {"date": "2022-01-01T10:00:00", "state": "PENDING"},
        {"date": "2022-03-01T10:00:00", "state": "EXECUTED"},
    ]

    # Использование функций
    executed_items = filter_by_state(sample_data, "EXECUTED")
    sorted_items = sort_by_date(executed_items)

    # Печать результатов
    print("Executed Items:", executed_items)
    print("Sorted Items:", sorted_items)
