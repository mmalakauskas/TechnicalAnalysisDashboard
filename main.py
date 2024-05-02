from analysis import get_technical_analysis
from display import display_analysis, rsi_condition, recommendations
from logger import log_analysis
from config import symbols, interval
from dashboard import live_dashboard

def run_dashboard():
    current_symbols = symbols

    while True:
        print(f"Select the function for {current_symbols} symbol:")
        print("1. Display Analysis")
        print("2. Live Dashboard")
        print("3. RSI Condition")
        print("4. Buy/Sell Recommendations")
        print("5. Log Analysis")
        print("6. Change Symbol")
        print("7. Exit Program")

        choice = input("Enter your choice as number: ")
        selected = int(choice.strip())

        analysis = get_technical_analysis(current_symbols)
        if analysis is not None:
            if selected == 1:
                display_analysis(analysis)
            elif selected == 2:
                live_dashboard(current_symbols)
                continue
            elif selected == 3:
                rsi_condition(analysis)
            elif selected == 4:
                recommendations(analysis)
            elif selected == 5:
                log_analysis(analysis)
                print("Analysis logged.")
        else:
            print(f"Could not get analysis for {current_symbols}")
        if selected == 6:
            new_symbol = input("Enter new symbol: ")
            current_symbols = new_symbol
            print(f"Symbol changed to {current_symbols}.")
            continue
        if selected == 7:
            print("Program closed.")
            break


if __name__ == "__main__":
    run_dashboard()
