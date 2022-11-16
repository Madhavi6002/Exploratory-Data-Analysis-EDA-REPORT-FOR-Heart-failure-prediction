# Exploratory-Data-Analysis-EDA-REPORT-FOR-Heart-failure-prediction


Healthcare industries generate enormous amount of data, so called big data that accommodates hidden knowledge or pattern for decision making. The huge volume of data is used to make decision which is more accurate than intuition. Exploratory Data Analysis (EDA) detects mistakes, finds appropriate data, checks assumptions and determines the correlation among the explanatory variables.

In this case, I used pandas profiling library to do analysis in Python. With this, I will be able to perform analysis on any data set very easily.

Here is my code:


import pandas as pd
from pandas_profiling import ProfileReport


df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

print(df)

#Generate a report

profile = ProfileReport(df)
#profile = ProfileReport(df , minimal=True)
profile.to_file(output_file ="heart Fail.html")


_____________________________________________________


Html report:



Overview
Overview
Alerts 6
Reproduction
Dataset statistics

Number of variables	13
Number of observations	299
Missing cells	0
Missing cells (%)	0.0%
Duplicate rows	0
Duplicate rows (%)	0.0%
Total size in memory	30.5 KiB
Average record size in memory	104.4 B
Variable types

Numeric	7
Categorical	6
Variables

sex
sex
CategoricalHIGH CORRELATION
Distinct	2
Distinct (%)	0.7%
Missing	0
Missing (%)	0.0%
Memory size	2.5 KiB
1	194 
0	105 
Overview
Categories
Words
Characters
Length
Max length	1
Median length	1
Mean length	1
Min length	1
Characters and Unicode
Total characters	299
Distinct characters	2
Distinct categories	1?
Distinct scripts	1?
Distinct blocks	1?
The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables.
Unique
Unique	0?
Unique (%)	0.0%
Sample
1st row	1
2nd row	1
3rd row	1
4th row	1
5th row	0
Interactions
age
creatinine_phosphokinase
ejection_fraction
platelets
serum_creatinine
serum_sodium
time
time
age
creatinine_phosphokinase
ejection_fraction
platelets
serum_creatinine
serum_sodium
Correlations
Auto
Spearman's ρ
Pearson's r
Kendall's τ
Cramér's V (φc)
Phik (φk)
Missing values
Count
Matrix
A simple visualization of nullity by column.
Sample
First rows
age	anaemia	creatinine_phosphokinase	diabetes	ejection_fraction	high_blood_pressure	platelets	serum_creatinine	serum_sodium	sex	smoking	time	DEATH_EVENT
0	75.0	0	582	0	20	1	265000.00	1.9	130	1	0	4	1
1	55.0	0	7861	0	38	0	263358.03	1.1	136	1	0	6	1
2	65.0	0	146	0	20	0	162000.00	1.3	129	1	1	7	1
3	50.0	1	111	0	20	0	210000.00	1.9	137	1	0	7	1
4	65.0	1	160	1	20	0	327000.00	2.7	116	0	0	8	1
5	90.0	1	47	0	40	1	204000.00	2.1	132	1	1	8	1
6	75.0	1	246	0	15	0	127000.00	1.2	137	1	0	10	1
7	60.0	1	315	1	60	0	454000.00	1.1	131	1	1	10	1
8	65.0	0	157	0	65	0	263358.03	1.5	138	0	0	10	1
9	80.0	1	123	0	35	1	388000.00	9.4	133	1	1	10	1
Last rows
age	anaemia	creatinine_phosphokinase	diabetes	ejection_fraction	high_blood_pressure	platelets	serum_creatinine	serum_sodium	sex	smoking	time	DEATH_EVENT
289	90.0	1	337	0	38	0	390000.0	0.9	144	0	0	256	0
290	45.0	0	615	1	55	0	222000.0	0.8	141	0	0	257	0
291	60.0	0	320	0	35	0	133000.0	1.4	139	1	0	258	0
292	52.0	0	190	1	38	0	382000.0	1.0	140	1	1	258	0
293	63.0	1	103	1	35	0	179000.0	0.9	136	1	1	270	0
294	62.0	0	61	1	38	1	155000.0	1.1	143	1	1	270	0
295	55.0	0	1820	0	38	0	270000.0	1.2	139	0	0	271	0
296	45.0	0	2060	1	60	0	742000.0	0.8	138	0	0	278	0
297	45.0	0	2413	0	38	0	140000.0	1.4	140	1	1	280	0
298	50.0	0	196	0	45	0	395000.0	1.6	136	1	1	285	0

