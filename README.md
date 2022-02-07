# Visualisation of Climate Crisis with Berkeley Earth Data

# General Information

## Participants

Luis Günther, Maurice Seifert, Wenli Xu

## Context

This visualisation was developed in the context of a lecture on problem-driven visualisation at _Freie Universität Berlin_ in the winter term 2021/2022.

The problem which has been chosen for a visualisation is global warming.

Global warming has been observed since the pre-industrial period (between 1850 and 1900). Although there were different periods of climate change in the history of the earth, the current changes are not simply due to natural causes. It is a global problem, but people in different countries express various degrees of concerns.

## Links

Interactive Prototype:
- https://berkeleydatavis.herokuapp.com/start

Screencast of Prototype:
- https://youtu.be/KkbPHWmv08s

## Concept

The concept of this visualisation is to raise awareness for the generality of the problem global warming and to also provide more detailed information for a closer look.

# Reflection

## Problems

In the process of developing a visualisation with Python there were several problems, that need to be adressed.

### Linking Visualisations

The initial plan for the two different visualisations was to link them. The user was meant to click a datapoint of a country in the overview, which would load a detailed view for more information about the climate data of the selected country.

After different failed approaches with various techniques to achieve this functionality we were forced to use a simple button to switch between the two views.

### Missing Countries

The automatic download of Berkeley Earth Data did not work for every country. Special characters are encoded in a mysterious way and we failed to decode these characters in Python. Our only remaining solution was to remove the countries with these problems.

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

### Deployment

Deploying the visualisation turned out to be more difficult than anticipated.

The project was initially created as a GitLab Repository at https://git.imp.fu-berlin.de, a separeated GitLab of Freie Universität Berlin.
In this environment, there is no possibility of using GitLab Pages for deploying a project.
Therefore the project was migrated to a public GitLab repository. The deployment process failed here, so another migration to GitHub was done. GitHub Pages also did not work out because only static visualisation can be deployed with either GitLab Pages or GitHub Pages.

In the end the only working solution for a dynamic deployment was using https://heroku.com for deployment. For the deployment process, the pipeline detects changes at the GitHub repository and automatically deploys the visualisation to https://berkeleydatavis.herokuapp.com.

The many different exports and migrations are also the explanation for a shortened commit history.

## Used Libraries

The main library for visualising the data is altair. Additional libraries where needed and uses for various reasons:

- pandas - configuration of dataframes for the charts
- re - regular expressions for extracting data from Berkeley Earth Webpage
- panel - using updatable visuals with altair-charts
- urllib3, urllib, requests - requesting Berkely Earth Webpages for data extraction
- os, pathlib, csv - processing data as files
- numpy - processing data from files as multidimensional arrays

## Possible Improvements

In addition to linking the two visualisation there are a few imaginable improvements.

It is possible to provide more detailed information about climate change and its effects on the covered countries.
Additional information on the process of data gathering by Berkeley Earth could also be beneficial.

Besides that, there is no clear design concept for the web prototype. An appealing CSS styling could make using the visualisation more enjoyable.

# Domain Problem Characterisation
## Target Users

The target group for the visualisation is the interested general public. For the understanding of this visualisation no professional knowledge is needed, but decent experience in reading graphs is necessary.

The visualisation is meant to give a wide overview about the problem of climate change and the possibility to focus on certain countries or regions, based on the interests of users.

# Data and Task Abstraction
## Origin of Data

The dataset of this visualization is derived from Berkeley Earth (https://berkeleyearth.org), which is a non-profit organization focused on data science regarding the environment.

In the dataset which is used here, there are multiple tables with lists of temperature anomalies originating of a overall timespan from 1750 to 2020.

There are several gaps with lacking data in the earlier years of some countries, but generally the dataset is complete enough to analyse the problem of global warming.
In some cases the recording of temperature data startet not until e.g. 1956 (Antarctica), but this only applies to a few regions.

## Aggregation of Data

The data for each individual country is requested from the Berkeley Earth Webpages. Therefore a list of all countries at http://berkeleyearth.lbl.gov/country-list/ is crawled to extract all countries. Afterwards the individual url of each country is requested whose data table is then extracted and saved locally (example of url: http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/baker-island-TAVG-Trend.txt).

The first part of the file is removed to leave a clean data table for visualisation. Additionally the mean temperature of the country is extracted, which is part of the comment section at the start (example of mean temperature: _% Estimated Jan 1951-Dec 1980 absolute temperature (C): 26.61 +/- 1.91_). The temperature values in the following data table are so calles anomaly values, which are relative deviations from this mean temperature.

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

_Overview_
- climate stripe visual with every coúntry for a bigger picture on climate change at a glance
- sorting by continents for breaking down the mass of data and to avoid overcharging users

_Bar Chart_
- each bar represents a year  
- the height and color of bars represent the deviation from the mean temperature
- use of bar chart instead of line chart for possibility to use color coding and adopt the visual concept of climate stripes

_Colors for Temperature Difference_
- red-warm/blue-cold impression for an intuitive understanding* of temperature data

    \* studies on intuitive understanding of colors for visualisation of temperatures:
    - George A. Morgan et al. (1975): Age Differences in the Associations between Felt Temperatures and Color Choices, The American Journal of Psychology , Vol. 88, No. 1, pp. 125-130
    - Ho H-N, Van Doorn GH, Kawabe T, Watanabe J, Spence C (2014) Colour-Temperature Correspondences: When Reactions to Thermal Stimuli Are Influenced by Colour. PLoS ONE 9(3):
e91854. doi:10.1371/journal.pone.0091854

_Search Menu for different Countries_
- users can decide which countries to evaluate further based on their own interests
- more clearly arranged than a dropdown menu with all existent possibilities

_Uncertainty only shown in Tooltip_
- uncertainty makes the understanding of a simple graph more complex and difficult, but nevertheless it is important to inform the user about it

_Tooltip Information for Values_
- name of country, absolute temperature values as well as deviation/anomaly value, uncertainty
- detailed information about selected data point without the need to scroll back to axis for reading the corresponding labels

_Reference and Explanation for Data_
- reference to data source and FAQ with explanations for anomalies and uncertainty

## Definitions of used terms

### Anomaly

A temperature anomaly is the deviation from the average (baseline) temperature. We use the averaged absolute temperatures between Jan 1951 and Dec 1980 as the baseline temperature because all temperature data of Berkeley Earth is stored in this way.

A positive anomaly value indicates a warmer observed temperature in reference to the baseline and is coded in red color, while a negative anomaly value indicates a cooler observed temperature in reference to the baseline and is coded in blue color.  

Reference: https://www.ncdc.noaa.gov/monitoring-references/dyk/anomalies-vs-temperature  

### Uncertainty 

The temperatures from Berkeley Earth are observed and measured by a large collection of weather monitoring stations. These stations are located in different areas all around the country, so they may have different trends and baselines.

The uncertainty represents the 95% confidence interval for statistical noise and spatial undersampling effects as a adjustment for the differences between various weather monitoring stations.

# Algorithm Design

We decided to load the data from Berkeley Earth manually with a separate Python script. The tables from all countries are downloaded and need to be available at the repository for the other scripts to be operational.

Loading the data on call by users would take an estimated time of more than a minute.
