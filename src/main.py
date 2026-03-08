from live_data_fetch import fetch_live_company_data
from model import generate_live_investment_score
def main():
    print("Share Market Investment Prediction System")
    print("----------------------------------------")
    company = input("Enter NSE Company Symbol (e.g., TCS, INFY, WIPRO): ").strip().upper()
    if not company.endswith(".NS"):
        company += ".NS"
    print(f"\nFetching live data for {company}...")
    data = fetch_live_company_data(company)
    if data is None:
        print("Live market data is unavailable for this company.")
        return
    score = generate_live_investment_score(data)
    if score >= 70:
        category = "Strong Investment"
    elif score >= 40:
        category = "Moderate Investment"
    else:
        category = "Weak Investment"
    print("\nInvestment Analysis Result")
    print("--------------------------")
    print(f"Company           : {company}")
    print(f"Investment Score  : {score}/100")
    print(f"Category          : {category}")
main()