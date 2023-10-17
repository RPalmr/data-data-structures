# pylint: disable=missing-docstring

RATES = {
    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885,
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """

    source_amount, source_currency = amount

    if source_currency == currency:
        return round(source_amount)

    rate_key = f"{source_currency}{currency}"
    conversion_rate = RATES.get(rate_key)

    if conversion_rate is not None:
        return round(source_amount * conversion_rate)

    return None
