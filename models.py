"""
models.py
Klasy danych aplikacji BudgetTracker.
"""
class Transaction:
    """
    Reprezentuje jedną transakcję finansową.
    Attributes:
        amount (float): kwota, ujemna = wydatek, dodatnia = przychód
        description (str): opis transakcji
        date (str): data w formacie YYYY-MM-DD
    """

    def __init__(self, amount: float, description: str, date: str):
        self.amount = amount
        self.description = description
        self.date = date