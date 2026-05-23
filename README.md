# Malaysian Blood Donation Dashboard
Interactive Power BI dashboard exploring blood donation patterns across Malaysian states from 2006– 20 May 2026, using open data from DOSM.

## Project Overview
An interactive Power BI dashboard analysing Malaysian blood donation 
trends from 2020 to 20 May 2026. This project explores national trends, 
state-level patterns, blood type distributions, and the impact of public 
holidays on donation behaviour.

## Tools & Technologies
- Power BI Desktop - Dashboard development
- Python (pandas, numpy) - Data preparation and feature engineering
- Dataset - Open data from DOSM (Department of Statistics Malaysia)

## Dashboard Pages

|         Page          |                          Description                       |
|-----------------------|------------------------------------------------------------|
| National Overview     | Overall donation trends and key KPIs (2020 - 20 May 2026)  |
| State Analysis        | State-level comparison with interactive map                |
| Blood Type Analysis   | Blood type distribution and trends                         |          
| Public Holiday Impact | How holidays affect donation behaviour                     |
| Monthly Explorer      | Drill down by specific month and year                      |


## Key Insights
- Donations barely dropped during COVID-19 in 2020-2021, suggesting 
Malaysians maintained civic responsibility even during the pandemic. 
The sharpest growth happened in 2022, indicating a strong post-pandemic 
rebound.
- W.P. Kuala Lumpur contributes disproportionately high donations compared 
  to other states, likely driven by its high urban population density and 
  greater hospital accessibility. Notably, Sabah and Sarawak outperform 
  several Peninsular states in total donations.
- Type O dominates at 42.62%, consistent with global blood type distribution patterns.
  Type AB has the lowest donation rate at 5.66% reflecting its natural rarity in the
  population rather than low donor participation. Future versions could be enhanced if
  DOSM provides data separated by Rhesus factor (positive/negative).
- Contrary to the common perception that people prefer not to be disturbed 
  on holidays, blood donations are actually higher on public holidays than 
  on normal weekdays. Labour Day records the highest average donations among 
  all public holidays.
- Malaysians donate most on Sundays, followed by Saturdays, suggesting 
  weekends are the preferred donation days regardless of public holidays.

## Data Limitations
- Blood type data does not separate positive and negative (e.g. O+ vs O-)
- Only official public holidays are captured. Bridge holidays and extended 
  holiday periods declared by the government are not included in this dataset
- Blood demand and usage data is unavailable, therefore blood shortage 
  analysis cannot be performed
- Analysis is based on donation count only, not donor demographics

## Repository Structure
malaysia-blood-donation-analysis/
├── prepare_blood_data.py        
├── blood_donation_trend_dashboard.pbix    
├── blood_donation_trend_dashboard.pdf     
├── dashboard/
│   ├── page1_overview.png
│   ├── page2_byState.png
│   ├── page3_byBloodType.png
│   ├── page4_publicHolidayImpact.png
│   └── page5_explorer.png
└── README.md
