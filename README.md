# GRR-SEA Precipitation Comparison

## Project Description

This project compares the precipitation (rainfall only?) to determine the differences between Seattle and Grand Rapids. 

## Project Overview

Provide a short and concise overview of the project. Mention the problem it solves, the data used, and the key outcomes or findings.

- **Objective:** Compare precipitation between Seattle and Grand Rapids.
- **Domain:** Weather, Climate
- **Key Techniques:** 

---

## Project Structure

```
├── data/                 # Raw and processed data
├── code/                 # Jupyter notebooks and Python scripts
├── reports/              # Generated reports and visualizations
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## Data

- **Source:** https://www.ncei.noaa.gov/cdo-web/search?datasetid=GHCND
- **Description:** Precipitation data from NOAA in CSV format
- **License:** NA

---

## Analysis


This project took data sets for both Seattle and Grand Rapids. The analysis consisted of taking the csv files and converting into two dataframes. We analyzed the data in those dataframes to ensure that the data was consistant and could give us the answers we were looking to get from the data. This was specifically the rainfall comared between Seattle and Grand Rapids. 

- Weather_Data.ipynb contains all the code necessary to run and analyze the data files. 
- grr_rain.csv and seattle_rain.csv located in the data directory are the only files used in the analysis. 
- clean_seattle_grandrapids_weather.csv will be created as a result of the analysis and contains the combined Seattle and Grand Rapids data. This file will be re-created anytime this jupyter notebook is run. 

---

## Results

=== RAINFALL COMPARISON ===

Seattle (SEA) - Average Precipitation: 0.1133 inches
Grand Rapids (GRR) - Average Precipitation: 0.1184 inches

Difference: 0.0051 inches
Grand Rapids gets 4.5% more precipitation

---

## Authors

- Paul Skentzos - [@gpskentzos](https://github.com/gpskentzos)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Data sets: 
  - https://www.ncei.noaa.gov/cdo-web/search?datasetid=GHCND

- Tutorials or papers referenced

- Inspiration or collaborators
	- Seattle University DATA 5100 Course