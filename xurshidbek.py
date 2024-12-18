import pandas as pd

file_path = '/WHO COVID-19 cases.csv'
data = pd.read_csv(file_path)

total_new_cases = data['New_cases'].sum(skipna=True)

print(f"Jami yangi virus holatlari soni: {int(total_new_cases)}")
