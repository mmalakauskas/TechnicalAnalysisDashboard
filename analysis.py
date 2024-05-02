from tradingview_ta import TA_Handler, Interval, Exchange

def get_handler(symbols):
    return TA_Handler(
        symbol=symbols,
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_1_MINUTE
    )

def get_technical_analysis(symbols):
    handler = get_handler(symbols)
    try:
        analysis = handler.get_analysis()
        return analysis
    except Exception as e:
        print(f"Error when fetching data for {symbols}: {e}")
        return None
