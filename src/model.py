import math
def generate_live_investment_score(data):
    price = data["Price"]
    high_52 = data["High_52"]
    low_52 = data["Low_52"]
    market_cap = data["Market_Cap"]
    price_position = (price - low_52) / (high_52 - low_52) * 100
    stability_score = min(100, math.log10(market_cap) * 10)
    investment_score = (
        0.6 * price_position +
        0.4 * stability_score
    )
    return round(investment_score, 2)

