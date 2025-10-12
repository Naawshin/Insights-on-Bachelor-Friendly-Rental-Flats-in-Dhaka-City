# Insights on Bachelor Friendly Rental Flats in Dhaka City
This Tableau dashboard provides a comprehensive analysis of bachelor-friendly rental properties in Dhaka City from June to November 2025.


Source: https://www.thetolet.com/bd/property-district/dhaka/dhaka?category=bachelor

Map Data Source: https://data.humdata.org/dataset/cod-ab-bgd 

## Project Overview
Every year many youngsters move to dhaka from different regions of the country for jobs or education. However, when searching for budget-friendly rental flats/rooms/seats in mess, they often face challenges. 

This project aims to solve such problems through an interactive tableau dashboard by analyzing scraped rental data. It provides insights on,
1. **Geographic Distribution Map** - Rental listings across Dhaka
2. **Temporal Listings Trend** - Monthly availability (2023-2025)  
3. **Gender Demographics** - Male vs Female rental preferences
4. **Rent Price Segmentation** - Market distribution across price ranges
5. **Supply-Demand Analysis** - Area-wise rent vs availability correlation 

The dashboard also includes an interactive tool that allows the user to find areas based on their budget and preferred accommodation type.

## Key Insights from the [Dashboard](https://public.tableau.com/views/InsightsonBachelorFriendlyRentalPropertiesinDhaka/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link):
Amid a total of 20665 listings scraped over the years 2022 to 2026
- 18,741 entries remained after data processing with Rent_Type, Title, Location, Rent, Bedrooms, Bathrooms, and Gender identified as the most relevant features for bachelor rentals.
- The average rent is approximately BDT 4734 with a significant standard deviation of about BDT 3073, indicating a wide range of rental prices.
- Most vacancies are available for men only
- The highest amount of vacancies were noticed in August 2025 with March 2025 being the next highest 
- Uttara had the highest amount of vacanies amidst all rental listings
- Most bachelor-friendly 'rooms' are available in Mohammedpur and 'seat' in Lalbagh

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
6. I ran the scraper for each specific area. The area specific csv files can be found in /data/Scraped Data folder. 

7. Merge the files and clean the data following the data_cleaning.ipynb in /src/Data Processing. The final preocessed data can be found in /data/Processed Data.

8. Use QGIS to filter only the map data of Dhaka City with adm3_pcode starting with BD30

9. Add a new column in the bachelor_rental_cleaned.csv file named adm3_pcode and add the respective codes of each area


## Dashboard Preview
<img width="1846" height="730" alt="image" src="https://github.com/user-attachments/assets/cddb10de-71f1-422e-b721-e1061037d84d" />


[![Tableau Dashboard](https://img.shields.io/badge/Tableau-Dashboard-orange?logo=tableau&logoColor=white)](https://public.tableau.com/views/InsightsonBachelorFriendlyRentalPropertiesinDhaka/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)













