# Visualisation of Climate Crisis with Berkeley Earth Data

# General Information

## Participants

Luis Günther, Maurice Seifert, Wenli Xu

## Context

Global warming has been observed since the pre-industrial period (between 1850 and 1900). Although there were different periods of climate change in the history of the earth, the current changes are not simply due to natural causes. It is a global problem, but people in different countries express various degrees of concerns.

## Concept

# Reflection

## Problems

### Deployment

We ran into several unexpected problems while trying to deploy the visualisation.

The project was initially created as a GitLab Repository at https://git.imp.fu-berlin.de, a separeated GitLab of Freie Universität Berlin.
In this environment, there is no possibility of using GitLab Pages for deploying a project. Therefore the project was migrated to a public GitLab repository. The deployment process also failed here, so another migration to GitHub was done. GitHub Pages also did not work out.

In the end the only working solution was using https://heroku.com for deployment.

This is also the explanation for the very one-sided commit-history.

### Linking Visualisations

The initial plan for the two different visualisations was to link them. The user was meant to click a datapoint of a country in the overview, which would load a detailed view for more information about the climate data of the selected country.

After different failed approaches with various techniques to achieve this functionality we were forced to use a simple button to switch between the two views.

### Missing Countries

The automatic download of Berkeley Earth Data did not work for every country. Special characters are encoded in a mysterious way and we failed to decode these characters in Python. Our only remaining solution was to remove the three countries with these problems.

This applies to the following countries:
- Åland,
- Côte d'Ivoire,
- Curaçao,
- Saint Barthélemy.

Another problem for the overview were countries with little recorded data. The visualisation of all climate data only worked for countries with consistent data. We also hat to remove these countries for a working solution.

This applies to the following countries:
- Antarctica,
- French Southern and Antarctic Lands,
- Heard Island and McDonald Islands.

### Further Improvements

### Used Libraries

The main library for visualising the data is altair. Additional libraries where needed and uses for various reasons:
- pandas - configuration of dataframes for the charts
- re - regular expressions for extracting data from Berkeley Earth Webpage
- panel - using updatable visuals with altair-charts
- urllib3, urllib, requests - requesting Berkely Earth Webpages for data extraction
- os, pathlib, csv - processing data as files
- numpy - processing data from files as multidimensional arrays

# Domain Problem Characterisation
## Target Users

The target group for the visualisation is the interested general public. For the understanding of this visualisation no professional knowledge is needed, but decent experience in reading graphs is necessary.

The visualisation is meant to give a wide overview about the problem of climate change and the possibility to focus on certain countries or regions.

# Data and Task Abstraction
## Origin of data

The dataset of this visualization is derived from Berkeley Earth (https://berkeleyearth.org), which is a non-profit organization focused on data science regarding the environment. In this dataset there are multiple tables with lists of temperature anomalies over a timespan from 1750 to 2020.
Anomalies are deviations from the mean temperature of the years 1951 to 1980.

There are several gaps (lack of data) in the early years in some countries, but generally the dataset is complete enough to analyse the problem of global warming.

## Tasks

1. Visualizing global warming in a understandable and convincing way  
2. Impressing people with objective evidence  
3. Providing a general overview and more detailed information

## Purpose

The general problem of global warming and climate change does affect every person on the planet, but not everyone is affected in the same way and the same time.
Some countries are currently struggling harder with the outcomes of climate change and some countries will feel the consequences much later.
But as a matter of fact, all countries are or will be affected in some way.  

In this context, the purpose of this visualization is to inform the interested user about the equality and generality of the problem 'global' warming. Therefore all countries can be selected and their data be displayed with the aim to give a wide overview and the possibility of further information at the same time.

# Visual Encodings and Interaction Design
## Design relationales

- Bar Chart  
each bar represents a year  
the height of bars represents the deviation from the mean temperature   

- Colors for temperature difference  
red-warm/blue-cold impression for a intuitive understanding of data

- search menu for different countries   

- uncertainty only shown in tooltip   
uncertainty makes the understanding of a simple graph more complex and difficult, but nevertheless it is important to inform the user about it

- tooltip information for values  
name of country, absolute temperature values as well as deviation value, uncertainty

- reference and explanation for data
reference to data source and faq for explanations for anomalies and uncertainty

## Definitions of used terms

- What does temperature anomaly mean?  

A temperature anomaly is the difference from the average (baseline) temperature. We use the averaged absolute temperatures between Jan 1951 and Dec 1980 as the baseline temperature. A positive anomaly indicates the observed temperature was warmer than the baseline (with red color), while a negative anomaly indicates the observed temperature was cooler than the baseline (with blue color).  

Reference: https://www.ncdc.noaa.gov/monitoring-references/dyk/anomalies-vs-temperature  

- What does uncertainty mean?  

The temperatures from Berkeley Earth are observed from a large collection of weather monitoring stations. These stations locate in different areas all around the country, so they have different trends and baselines. The uncertainty represents the 95% confidence interval for statistical noise and spatial undersampling effects.

# Algorithm Design

We decided to load the data from Berkeley Earth manually with a separate Python script. The tables from all countries are downloaded and need to be available at the repository for the other scripts to be operational.

Loading the data on call by users would take an estimated time of more than a minute.