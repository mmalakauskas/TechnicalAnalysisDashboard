import keyboard
import time
from config import interval, symbols
from analysis import get_technical_analysis
from display import display_analysis

def live_dashboard(symbols):
    try:
        print(f"----Starting live dashboard for {symbols}----")
        while True:
            analysis = get_technical_analysis(symbols)
            if analysis is not None:
                display_analysis(analysis)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Live dashboard interrupted.")
