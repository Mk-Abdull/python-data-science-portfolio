Nigerian Inflation Analysis 

Objective:
Analyze and visualize Nigeria’s inflation trends using monthly and yearly Consumer Price Index (CPI) data, highlighting headline, food, and core inflation patterns over time.

Workflow & Key Steps:

1. Data Preparation:

Imported CPI data from Excel using pandas.

Combined tyear and tmonth into a proper datetime column (tperiod) to serve as the index.

Ensured all numeric columns were correctly typed and handled missing values.

2. Exploratory Analysis:

Computed monthly and yearly descriptive statistics (mean, max, min, growth rates).

Compared headline inflation (allItemsYearOn), food inflation (foodYearOn), and core inflation (allItemsLessFrmProdAndEnergyYearOn).

3. Trend Analysis & Visualization:

Plotted monthly inflation trends to capture short-term volatility.

Plotted yearly inflation trends to show long-term patterns and growth.

Identified extreme points, e.g., highest and lowest inflation in 2025, and annotated these on plots for clarity.

4. Insights:

Food inflation consistently remains the highest measure.

Core inflation (All Items Less Farm Produce & Energy) is more stable.

Spikes occur during:

exchange rate shocks

fuel subsidy removal

global supply chain volatility
5. Tools & Libraries:

Python (pandas, matplotlib)

Excel for data input

Portfolio Impact:
This project demonstrates data cleaning, time-series manipulation, statistical summarization, and professional visualization skills. The polished charts with annotated peaks and lows make it suitable for reports, presentations, or GitHub portfolio showcases.
