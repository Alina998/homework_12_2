import logging
import os

def get_mask_card_number(a: int) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера"""
    number_in_str = str(a)

    card_number = number_in_str.split()[-1]
    mask_card_number = (
        card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    )

    parts_of_number, parts_size = len(mask_card_number), len(mask_card_number) // 4
    logger.info("Generated masked card number")
    return " ".join(
        [
            mask_card_number[i: i + parts_size]
            for i in range(0, parts_of_number, parts_size)
        ]
    )


def get_mask_account(b: int) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""
    account_number = str(b)

    mask_account = "**" + account_number[-4:]
    logger.info("Generated masked account number")
    return mask_account


# Настройка логирования
log_file = os.path.join('logs', 'masks.log')

# Создаем директорию, если она не существует
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
    filename=log_file,
    filemode='w'  # 'w' для перезаписи лога
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    masked_card_number = get_mask_card_number(1234123412341234)
    print("Masked Card Number:", masked_card_number)

    masked_account_number = get_mask_account(12345123451234512345)
    print("Masked Account Number:", masked_account_number)
