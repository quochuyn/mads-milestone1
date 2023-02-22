# mads-milestone1
This project is for the University of Michigan's Master of Applied Data Science (MADS) Milestone I (SIADS 593) course for the 2023 Winter semester.

# Team Members
- Quoc-Huy Nguyen
- Ning Xu
- Yifei Dong

# Description
The COVID-19 pandemic has impacted much of the global supply chain. In particular, we wish to investigate its impact on the US’s agricultural truck transportation supply chain and the price/volume of certain agricultural products. For example, we want to investigate the correlation between COVID-19 cases, truck volume, and agricultural product pricing in the state of California.

# Datasets
| **Name** | **Description** | **Main Variables** | **Details** | **Access** |
| ------------ | ------------- | ------------ | ------------- | ------------- |
| **Refrigerated Truck Volumes** | The primary data set on refrigerated truck volumes on various staple fruits and vegetables by region. Some of the data collection methods used includes Federal marketing orders, telephone interviews, faxes, emails, and access to other data sources. The time frame of interest will be from Jan. 1, 2015 to Dec. 31, 2022. | Date, region of origin, commodity, volume| **Size**: 108 MB **Shape**: 1M rows, 14 columns **Format**: CSV | [USDA](https://agtransport.usda.gov/Truck/Refrigerated-Truck-Volumes/rfpn-7etz) |
| **COVID-19 Cases** | The COVID-19 data set is a preprocessed clean data set with weekly updated COVID-19 total cases and death counts aggregated on the state level of 60 different states. The time frame covers Jan. 23, 2020 to Jan. 12, 2023. | Date, State, Total_cases| **Size**: 550 KB **Shape**: 9K rows, 10 columns **Format**: CSV | [CDC](https://data.cdc.gov/Case-Surveillance/Weekly-United-States-COVID-19-Cases-and-Deaths-by-/pwn4-m3yp) |
| **Fruit Prices** | The fruit prices data set comes from the Economic Research Service department of the USDA. The data allows for observations of the weekly economic performance of various fruits over time. The time frame covers May 2, 2020 to Apr. 23, 2022. | Week, commodity, retailed price | Size: 976 KB Shape: 2K rows & 3 columns Format: XLSX | [USDA](https://www.ers.usda.gov/data-products/fruit-and-tree-nuts-data/selected-weekly-fruit-movement-and-price/) |
