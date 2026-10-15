
def calculate_bill(units: int, rate: float = 6.0) -> float:
    """Calculate an electricity bill."""
    if units < 0:
        raise ValueError("Units cannot be negative")

    return units * rate
