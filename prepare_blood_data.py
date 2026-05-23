import pandas as pd
import numpy as np

# ============================================================
# MALAYSIAN PUBLIC HOLIDAYS 2006-2026
# ============================================================
public_holidays = {
    # 2006
    "2006-01-01": "New Year's Day",
    "2006-01-29": "Chinese New Year",
    "2006-01-30": "Chinese New Year Holiday",
    "2006-04-11": "Hari Raya Aidilfitri",
    "2006-04-12": "Hari Raya Aidilfitri Holiday",
    "2006-05-01": "Labour Day",
    "2006-05-13": "Wesak Day",
    "2006-06-03": "Yang di-Pertuan Agong's Birthday",
    "2006-08-31": "National Day",
    "2006-10-21": "Deepavali",
    "2006-12-25": "Christmas Day",
    "2006-12-31": "Hari Raya Aidiladha",

    # 2007
    "2007-01-01": "New Year's Day",
    "2007-01-20": "Hari Raya Aidiladha",
    "2007-02-18": "Chinese New Year",
    "2007-02-19": "Chinese New Year Holiday",
    "2007-03-10": "Awal Muharram",
    "2007-05-01": "Labour Day",
    "2007-05-31": "Wesak Day",
    "2007-06-02": "Yang di-Pertuan Agong's Birthday",
    "2007-08-31": "National Day",
    "2007-10-20": "Deepavali",
    "2007-12-25": "Christmas Day",

    # 2008
    "2008-01-01": "New Year's Day",
    "2008-01-10": "Hari Raya Aidiladha",
    "2008-02-07": "Chinese New Year",
    "2008-02-08": "Chinese New Year Holiday",
    "2008-05-01": "Labour Day",
    "2008-05-19": "Wesak Day",
    "2008-06-07": "Yang di-Pertuan Agong's Birthday",
    "2008-08-31": "National Day",
    "2008-10-27": "Deepavali",
    "2008-12-25": "Christmas Day",

    # 2009
    "2009-01-01": "New Year's Day",
    "2009-01-26": "Chinese New Year",
    "2009-01-27": "Chinese New Year Holiday",
    "2009-05-01": "Labour Day",
    "2009-05-09": "Wesak Day",
    "2009-06-06": "Yang di-Pertuan Agong's Birthday",
    "2009-08-31": "National Day",
    "2009-09-16": "Malaysia Day",
    "2009-10-17": "Deepavali",
    "2009-12-25": "Christmas Day",

    # 2010
    "2010-01-01": "New Year's Day",
    "2010-02-14": "Chinese New Year",
    "2010-02-15": "Chinese New Year Holiday",
    "2010-05-01": "Labour Day",
    "2010-05-28": "Wesak Day",
    "2010-06-05": "Yang di-Pertuan Agong's Birthday",
    "2010-08-31": "National Day",
    "2010-09-16": "Malaysia Day",
    "2010-11-05": "Deepavali",
    "2010-12-25": "Christmas Day",

    # 2011
    "2011-01-01": "New Year's Day",
    "2011-02-03": "Chinese New Year",
    "2011-02-04": "Chinese New Year Holiday",
    "2011-05-01": "Labour Day",
    "2011-05-17": "Wesak Day",
    "2011-06-04": "Yang di-Pertuan Agong's Birthday",
    "2011-08-31": "National Day",
    "2011-09-16": "Malaysia Day",
    "2011-10-26": "Deepavali",
    "2011-12-25": "Christmas Day",

    # 2012
    "2012-01-01": "New Year's Day",
    "2012-01-23": "Chinese New Year",
    "2012-01-24": "Chinese New Year Holiday",
    "2012-05-01": "Labour Day",
    "2012-05-05": "Wesak Day",
    "2012-06-02": "Yang di-Pertuan Agong's Birthday",
    "2012-08-31": "National Day",
    "2012-09-16": "Malaysia Day",
    "2012-11-13": "Deepavali",
    "2012-12-25": "Christmas Day",

    # 2013
    "2013-01-01": "New Year's Day",
    "2013-02-10": "Chinese New Year",
    "2013-02-11": "Chinese New Year Holiday",
    "2013-05-01": "Labour Day",
    "2013-05-24": "Wesak Day",
    "2013-06-01": "Yang di-Pertuan Agong's Birthday",
    "2013-08-08": "Hari Raya Aidilfitri",
    "2013-08-09": "Hari Raya Aidilfitri Holiday",
    "2013-08-31": "National Day",
    "2013-09-16": "Malaysia Day",
    "2013-11-02": "Deepavali",
    "2013-12-25": "Christmas Day",

    # 2014
    "2014-01-01": "New Year's Day",
    "2014-01-31": "Chinese New Year",
    "2014-02-01": "Chinese New Year Holiday",
    "2014-05-01": "Labour Day",
    "2014-05-13": "Wesak Day",
    "2014-06-07": "Yang di-Pertuan Agong's Birthday",
    "2014-07-28": "Hari Raya Aidilfitri",
    "2014-07-29": "Hari Raya Aidilfitri Holiday",
    "2014-08-31": "National Day",
    "2014-09-16": "Malaysia Day",
    "2014-10-22": "Deepavali",
    "2014-12-25": "Christmas Day",

    # 2015
    "2015-01-01": "New Year's Day",
    "2015-02-19": "Chinese New Year",
    "2015-02-20": "Chinese New Year Holiday",
    "2015-05-01": "Labour Day",
    "2015-06-02": "Wesak Day",
    "2015-06-06": "Yang di-Pertuan Agong's Birthday",
    "2015-07-17": "Hari Raya Aidilfitri",
    "2015-07-18": "Hari Raya Aidilfitri Holiday",
    "2015-08-31": "National Day",
    "2015-09-16": "Malaysia Day",
    "2015-11-10": "Deepavali",
    "2015-12-25": "Christmas Day",

    # 2016
    "2016-01-01": "New Year's Day",
    "2016-02-08": "Chinese New Year",
    "2016-02-09": "Chinese New Year Holiday",
    "2016-05-01": "Labour Day",
    "2016-05-21": "Wesak Day",
    "2016-06-04": "Yang di-Pertuan Agong's Birthday",
    "2016-07-06": "Hari Raya Aidilfitri",
    "2016-07-07": "Hari Raya Aidilfitri Holiday",
    "2016-08-31": "National Day",
    "2016-09-16": "Malaysia Day",
    "2016-10-29": "Deepavali",
    "2016-12-25": "Christmas Day",

    # 2017
    "2017-01-01": "New Year's Day",
    "2017-01-28": "Chinese New Year",
    "2017-01-29": "Chinese New Year Holiday",
    "2017-05-01": "Labour Day",
    "2017-05-10": "Wesak Day",
    "2017-06-05": "Yang di-Pertuan Agong's Birthday",
    "2017-06-26": "Hari Raya Aidilfitri",
    "2017-06-27": "Hari Raya Aidilfitri Holiday",
    "2017-08-31": "National Day",
    "2017-09-16": "Malaysia Day",
    "2017-10-18": "Deepavali",
    "2017-12-25": "Christmas Day",

    # 2018
    "2018-01-01": "New Year's Day",
    "2018-02-16": "Chinese New Year",
    "2018-02-17": "Chinese New Year Holiday",
    "2018-05-01": "Labour Day",
    "2018-05-29": "Wesak Day",
    "2018-06-15": "Hari Raya Aidilfitri",
    "2018-06-16": "Hari Raya Aidilfitri Holiday",
    "2018-09-09": "Yang di-Pertuan Agong's Birthday",
    "2018-08-31": "National Day",
    "2018-09-16": "Malaysia Day",
    "2018-11-06": "Deepavali",
    "2018-12-25": "Christmas Day",

    # 2019
    "2019-01-01": "New Year's Day",
    "2019-02-05": "Chinese New Year",
    "2019-02-06": "Chinese New Year Holiday",
    "2019-05-01": "Labour Day",
    "2019-05-19": "Wesak Day",
    "2019-06-05": "Hari Raya Aidilfitri",
    "2019-06-06": "Hari Raya Aidilfitri Holiday",
    "2019-07-22": "Yang di-Pertuan Agong's Birthday",
    "2019-08-31": "National Day",
    "2019-09-16": "Malaysia Day",
    "2019-10-27": "Deepavali",
    "2019-12-25": "Christmas Day",

    # 2020
    "2020-01-01": "New Year's Day",
    "2020-01-25": "Chinese New Year",
    "2020-01-26": "Chinese New Year Holiday",
    "2020-05-01": "Labour Day",
    "2020-05-07": "Wesak Day",
    "2020-05-24": "Hari Raya Aidilfitri",
    "2020-05-25": "Hari Raya Aidilfitri Holiday",
    "2020-06-08": "Yang di-Pertuan Agong's Birthday",
    "2020-08-31": "National Day",
    "2020-09-16": "Malaysia Day",
    "2020-11-14": "Deepavali",
    "2020-12-25": "Christmas Day",

    # 2021
    "2021-01-01": "New Year's Day",
    "2021-02-12": "Chinese New Year",
    "2021-02-13": "Chinese New Year Holiday",
    "2021-05-01": "Labour Day",
    "2021-05-13": "Hari Raya Aidilfitri",
    "2021-05-14": "Hari Raya Aidilfitri Holiday",
    "2021-05-26": "Wesak Day",
    "2021-06-07": "Yang di-Pertuan Agong's Birthday",
    "2021-08-31": "National Day",
    "2021-09-16": "Malaysia Day",
    "2021-11-04": "Deepavali",
    "2021-12-25": "Christmas Day",

    # 2022
    "2022-01-01": "New Year's Day",
    "2022-02-01": "Chinese New Year",
    "2022-02-02": "Chinese New Year Holiday",
    "2022-05-01": "Labour Day",
    "2022-05-02": "Hari Raya Aidilfitri",
    "2022-05-03": "Hari Raya Aidilfitri Holiday",
    "2022-05-15": "Wesak Day",
    "2022-06-06": "Yang di-Pertuan Agong's Birthday",
    "2022-08-31": "National Day",
    "2022-09-16": "Malaysia Day",
    "2022-10-24": "Deepavali",
    "2022-12-25": "Christmas Day",

    # 2023
    "2023-01-01": "New Year's Day",
    "2023-01-22": "Chinese New Year",
    "2023-01-23": "Chinese New Year Holiday",
    "2023-04-21": "Hari Raya Aidilfitri",
    "2023-04-22": "Hari Raya Aidilfitri Holiday",
    "2023-05-01": "Labour Day",
    "2023-05-04": "Wesak Day",
    "2023-06-05": "Yang di-Pertuan Agong's Birthday",
    "2023-08-31": "National Day",
    "2023-09-16": "Malaysia Day",
    "2023-11-12": "Deepavali",
    "2023-12-25": "Christmas Day",

    # 2024
    "2024-01-01": "New Year's Day",
    "2024-02-10": "Chinese New Year",
    "2024-02-11": "Chinese New Year Holiday",
    "2024-04-10": "Hari Raya Aidilfitri",
    "2024-04-11": "Hari Raya Aidilfitri Holiday",
    "2024-05-01": "Labour Day",
    "2024-05-22": "Wesak Day",
    "2024-06-03": "Yang di-Pertuan Agong's Birthday",
    "2024-08-31": "National Day",
    "2024-09-16": "Malaysia Day",
    "2024-10-31": "Deepavali",
    "2024-12-25": "Christmas Day",

    # 2025
    "2025-01-01": "New Year's Day",
    "2025-01-29": "Chinese New Year",
    "2025-01-30": "Chinese New Year Holiday",
    "2025-03-31": "Hari Raya Aidilfitri",
    "2025-04-01": "Hari Raya Aidilfitri Holiday",
    "2025-05-01": "Labour Day",
    "2025-05-12": "Wesak Day",
    "2025-06-02": "Yang di-Pertuan Agong's Birthday",
    "2025-08-31": "National Day",
    "2025-09-16": "Malaysia Day",
    "2025-10-20": "Deepavali",
    "2025-12-25": "Christmas Day",

    # 2026
    "2026-01-01": "New Year's Day",
    "2026-02-17": "Chinese New Year",
    "2026-02-18": "Chinese New Year Holiday",
    "2026-03-20": "Hari Raya Aidilfitri",
    "2026-03-21": "Hari Raya Aidilfitri Holiday",
    "2026-05-01": "Labour Day",
    "2026-06-01": "Yang di-Pertuan Agong's Birthday",
    "2026-08-31": "National Day",
    "2026-09-16": "Malaysia Day",
    "2026-12-25": "Christmas Day",
}



# ============================================================
# DOWNLOAD DATA
# ============================================================
print("Downloading national blood donation data...")
df_national = pd.read_parquet('https://storage.data.gov.my/healthcare/blood_donations.parquet')
df_national['date'] = pd.to_datetime(df_national['date'])
df_national['state'] = 'Malaysia'

print("Downloading state level blood donation data...")
df_state = pd.read_parquet('https://storage.data.gov.my/healthcare/blood_donations_state.parquet')
df_state['date'] = pd.to_datetime(df_state['date'])

print("Combining datasets...")
df = pd.concat([df_national, df_state], ignore_index=True)

# ============================================================
# FEATURE ENGINEERING
# ============================================================
print("Adding features...")

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['month_name'] = df['date'].dt.strftime('%B')
df['day'] = df['date'].dt.day
df['day_of_week'] = df['date'].dt.dayofweek
df['day_name'] = df['date'].dt.strftime('%A')
df['week_number'] = df['date'].dt.isocalendar().week.astype(int)
df['is_weekend'] = df['day_of_week'].apply(lambda x: 'Yes' if x >= 5 else 'No')

# Public holidays
df['is_public_holiday'] = df['date'].dt.strftime('%Y-%m-%d').map(
    lambda x: 'Yes' if x in public_holidays else 'No'
)
df['holiday_name'] = df['date'].dt.strftime('%Y-%m-%d').map(
    lambda x: public_holidays.get(x, 'None')
)

# Sort by state, blood type, date
df_sorted = df.sort_values(['state', 'blood_type', 'date']).reset_index(drop=True)

# Keep only basic columns
df_final = df_sorted[[
    'date', 'state', 'blood_type', 'donations',
    'year', 'month', 'month_name', 'day',
    'day_of_week', 'day_name', 'week_number',
    'is_weekend', 'is_public_holiday', 'holiday_name'
]]

# ============================================================
# SAVE TO CSV
# ============================================================
output_path = 'blood_donations_final.csv'
df_final.to_csv(output_path, index=False)

print(f"\nDone! Saved to {output_path}")
print(f"Total rows: {df_final.shape[0]}")
print(f"Total columns: {df_final.shape[1]}")
print(f"\nColumns: {list(df_final.columns)}")
print(f"\nDate range: {df_final['date'].min()} to {df_final['date'].max()}")
print(f"\nStates: {df_final['state'].unique()}")
print(f"\nBlood types: {df_final['blood_type'].unique()}")