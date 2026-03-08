def categorize_investment(df):
    df['Category'] = df['Investment_Score'].apply(
        lambda x: 'Strong' if x >= 70 else ('Moderate' if x >= 40 else 'Weak')
    )
    return df
def get_top_recommendation(df):
    top_company = df.sort_values(
        by='Investment_Score', ascending=False
    ).iloc[0]

    return {
        "Ticker": top_company['Ticker'],
        "Score": round(float(top_company['Investment_Score']), 2),
        "Category": top_company['Category']
    }
