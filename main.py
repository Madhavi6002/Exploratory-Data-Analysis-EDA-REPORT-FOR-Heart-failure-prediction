import pandas as pd
from pandas_profiling import ProfileReport


df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
print(df)

#Generate a report

profile = ProfileReport(df)
profile.to_file(output_file ="heart Fail.html")
