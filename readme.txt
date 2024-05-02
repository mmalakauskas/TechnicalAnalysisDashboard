Financial Technical Analysis Dashboard Project

Overview:

The Financial Dashboard is a Python application designed to provide real-time financial analysis and signals based on market data. It supports various functionalities such as displaying live data, logging analysis, and generating buy/sell recommendations.

Features:

Display Analysis: Show current financial data analysis.
Live Dashboard: Continuously update and display live data.
Check RSI Condition: Analyze RSI data to identify market conditions.
Buy/Sell Recommendations: Provide buying or selling recommendations based on the analysis.
Log Analysis: Log the results of the analysis for later review.


Configuration:

The config.py file contains configuration settings for the dashboard. You can set the symbols and intervals for the analysis:

To run the dashboard, use the following command in your terminal:

python main.py

Once started, the program will prompt you to select an option from the menu to perform actions like viewing live data, checking for signals, or generating recommendations.

How It Works:

main.py: Serves as the entry point for the application. It handles user interactions and triggers appropriate functionalities based on user input.
analysis.py: Contains functions to fetch and analyze financial data.
display.py: Manages the display of analysis results.
dashboard.py: Handles live updates and real-time data processing.
logger.py: Responsible for logging all analyses for audit and review.
config.py: Provides configuration variables like symbols and update intervals.