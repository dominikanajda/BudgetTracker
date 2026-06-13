"""
storage.py
Zapis i odczyt transakcji do pliku JSON.
"""
import json
import os
from models import Transaction

FILE_PATH = "transactions.json"

def save_transactions(transactions: list):
    """
    Zapisuje listę transakcji do pliku JSON.
    Args:
        transactions (list): lista obiektów Transaction
    """
    data = []

    # zamień każdy obiekt na słownik
    for t in transactions:
        data.append({
            "amount": t.amount,
            "description": t.description,
            "date": t.date
        })

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_transactions() -> list:
    """
    Wczytuje transakcje z pliku JSON.
    Returns:
        list: lista obiektów Transaction, pusta jeśli plik nie istnieje
    """
    # sprawdź czy plik istnieje
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    transactions = []

    # odtwórz każdy obiekt ze słownika
    for item in data:
        t = Transaction(
            amount = item["amount"],
            description = item["description"],
            date = item["date"]
        )
        transactions.append(t)

    return transactions