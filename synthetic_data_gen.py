import pandas as pd
import numpy as np

# Set seed for repeatable results
np.random.seed(42)

percent_by_year = {1997: 0.34, 2018: 0.43, 2019: 0.51}

years = list(range(1995, 2026))
age_groups = ['12-17', '18-25', '26-34', '35-49', '50+']
regions = ['North', 'South', 'East', 'West']
genders = ['Male', 'Female']

def generate_marijuana_use(year, n_people):
    if year in percent_by_year:
        n_true = int(round(n_people * percent_by_year[year]))
        n_false = n_people - n_true
        values = [True]*n_true + [False]*n_false
        np.random.shuffle(values)
        return values if n_people > 1 else values[0]
    else:
        return (np.random.rand(n_people) < 0.3) if n_people > 1 else (np.random.rand() < 0.3)

# Generate data using list comprehension
data = [
    [
        year, age, region, gender,
        v,
        np.random.choice(['High School', 'Bachelor', 'Master', 'PhD']),
        np.random.choice(['Low', 'Medium', 'High'])
    ]
    for year in years
    for age in age_groups
    for region in regions
    for gender in genders
    for n_people in [np.random.randint(5,60)]
    for v in generate_marijuana_use(year, n_people)
]

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'year', 'age_group', 'region', 'gender', 'have_tried_marijuana', 'education_level', 'income'
])

# Check the percentage of population who have tried marijuana for selected years
# special_years = [1997, 2018, 2019]
# percentages = df.groupby('year')['have_tried_marijuana'].mean().loc[special_years] * 100
# print(percentages)


# Save to csv file
df.to_csv('marijuana_data.csv', index = False)
