# mads-milestone1
This project is for the University of Michigan's Master of Data Science (MADS) Milestone I for the 2023 Winter semester.

# Team Members
- Quoc-Huy Nguyen
- Ning Xu
- Yifei Dong

# Description
The trucking industry remains one of the most important means of transportation of goods in the US. This is especially the case with perishable items, which require quick and efficient transportation. The Agricultural Marketing Service of the USDA regularly issues reports to provide a consistent overview of the state of the agricultural market. One particular report tracks the daily refrigerated truck volume of fruits and vegetables from US domestic origins. Most movements are reported, but not all commodities nor origins are included. 

Food and product prices have been constantly increasing ever since COVID-19 hit the US in early 2020. Holding the hypothesis that the COVID-19 pandemic has impacted much of the food supply chain, thus increasing food prices, we want to conduct a study that can prove the relation between these three factors: COVID-19 cases, refrigerated truck volume, and refrigerated product prices.

# Datasets
| **Name** | **Description** | **Main Variables** | **Details** | **Access** |
| ------------ | ------------- | ------------ | ------------- | ------------- |
| **Refrigerated Truck Volumes** | The primary data set on refrigerated truck volumes on various staple fruits and vegetables by region. Some of the data collection methods used includes Federal marketing orders, telephone interviews, faxes, emails, and access to other data sources. The time frame of interest will be from Jan. 1, 2015 to Dec. 31, 2022. | Date, region of origin, commodity, volume| **Size**: 108 MB **Shape**: 1M rows, 14 columns **Format**: CSV | [USDA](https://agtransport.usda.gov/Truck/Refrigerated-Truck-Volumes/rfpn-7etz) |
| **COVID-19 Cases** | The COVID-19 data set is a preprocessed clean data set with weekly updated COVID-19 total cases and death counts aggregated on the state level of 60 different states. The time frame covers Jan. 23, 2020 to Jan. 12, 2023. | Date, State, Total_cases| **Size**: 550 KB **Shape**: 9K rows, 10 columns **Format**: CSV | [CDC](https://data.cdc.gov/Case-Surveillance/Weekly-United-States-COVID-19-Cases-and-Deaths-by-/pwn4-m3yp) |
| **Fruit Prices** | The fruit prices data set comes from the Economic Research Service department of the USDA. The data allows for observations of the weekly economic performance of various fruits over time. The time frame covers May 2, 2020 to Apr. 23, 2022. | Week, commodity, retailed price | Size: 976 KB Shape: 2K rows & 3 columns Format: XLSX | [USDA](https://www.ers.usda.gov/data-products/fruit-and-tree-nuts-data/selected-weekly-fruit-movement-and-price/) |
