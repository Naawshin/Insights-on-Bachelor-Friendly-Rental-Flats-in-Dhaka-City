# Insights on Bachelor Friendly Rental Flats in Dhaka City
This Tableau dashboard provides a comprehensive analysis of bachelor-friendly rental properties in Dhaka City from June to November 2025.


Source: https://www.thetolet.com/bd/property-district/dhaka/dhaka?category=bachelor

Map Data Source: https://data.humdata.org/dataset/cod-ab-bgd 

## Project Overview
Every year many youngsters move to dhaka from different regions of the country for jobs or education. However, when searching for budget-friendly rental flats/rooms/seats in mess, they often face challenges. 

This project aims to solve such problems through an interactive tableau dashboard by analyzing scraped rental data. It provides insights on,
- Average rent in different areas of Dhaka city 
- Availability of rooms vs flat vs seats
- Gender specific accommodation options
- Monthly trend in rental vacancies

The dashboard also includes an interactive tool that allows the user to find areas based on their budget and preferred accommodation type.

## Key Insights from the [Dashboard](https://public.tableau.com/views/InsightsonBachelor-FriendlyRentalFlatsinDhakaCity/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
Amid a total of 1765 listings scraped over the months June to November 2025
- The most popular rental type is seat (69.05% of the listings)
- Most vacancies are suitable for men only
- The highest amount of vacancies were noticed in August with September being the next highest 
- Khilkhet had the highest amount of vacanies for rooms and seats amidst all areas based on room and seat type accommodation
- Most bachelor-friendly 'flats' are available in Mohammedpur with Uttara being the second highest

## Tools
- Selenium
- Python
- QGIS 
- Tableau Public

## Build From Sources and Run the Scraper

1. Clone the repo
```bash
git clone https://github.com/Naawshin/Insights-on-Bachelor-Friendly-Rental-Flats-in-Dhaka-City.git
```
2. Initialize and activate virtual environment
```bash
python venv venv
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download QGIS from https://qgis.org/download/

5. Run the scraper
```bash
python Selenium Scraper/data_scraper.py
```
6. You'll get a file named 'thetolet_properties.csv' 

7. Use QGIS to filter only the map data of Dhaka City with adm3_pcode starting with BD30

8. Add a new column in the thetolet_properties.csv file named adm3_pcode and add the respective codes of each area


## Dashboard Preview
<img width="1419" height="624" alt="image" src="https://github.com/user-attachments/assets/f06ea9d1-798c-4a9b-8fad-a1b806c996d5" />

[![Tableau Dashboard](https://img.shields.io/badge/📊_Tableau_Dashboard-View_Interactive_Viz-0078D4?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/views/InsightsonBachelor-FriendlyRentalFlatsinDhakaCity/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)












