import pandas as pd

questions = pd.read_csv("survey_results_schema.csv", header=0)
df = pd.read_csv("survey_results_public.csv", header=0,
                 usecols=['WorkWeekHrs', 'CompTotal', 'CurrencySymbol',
                          'Age', 'Gender'])
df = df.dropna()
df = df.loc[df['CurrencySymbol'] == 'EUR']
# transformation of 'WorkWeekHrs' value to obtain Full Time Equivalent
df['WorkWeekHrs'] = df['WorkWeekHrs'] / 40
# estimation the Annual Total Salary
df['ATS'] = round(df['CompTotal'] / df['WorkWeekHrs'], 0)
