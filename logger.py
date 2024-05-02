from datetime import datetime

def log_analysis(analysis):
    log_entry = f"{datetime.now()} - {analysis.symbol} Analysis - {analysis.indicators}\n"
    with open("logs/analysis_log.txt", "a") as log_file:
        log_file.write(log_entry)
