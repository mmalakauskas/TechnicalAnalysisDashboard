def display_analysis(analysis):
    print(f"----{analysis.symbol} Analysis----")
    print("Indicators:")
    for name, value in analysis.indicators.items():
        print(f"{name}: {value:.2f}")
    print("Oscillators:")
    for name, value in analysis.oscillators.items():
        print(f"{name}: {value}")
    print("Moving Averages:")
    for name, value in analysis.moving_averages.items():
        print(f"{name}: {value}")

def rsi_condition(analysis):
    print(f"----{analysis.symbol} RSI Condition----")
    if analysis is None:
        return
    rsi = analysis.indicators.get('RSI')
    if rsi < 30:
        print(f"{analysis.symbol} RSI below 30, consider 'Oversold' condition.")
    elif rsi > 70:
        print(f"{analysis.symbol} RSI above 70, consider 'Overbought' condition.")
    else:
        print(f"{analysis.symbol} RSI is {rsi}, consider 'Neutral' condition.")

def recommendations(analysis):
    print(f"----{analysis.symbol} Buy/Sell Recommendations----")
    print(analysis.summary)
