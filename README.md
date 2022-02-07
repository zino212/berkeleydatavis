# BerkeleyDataVis  
Group 3: Luis Günther, Maurice Seifert, Wenli Xu

## User

general public without professional knowledge but basic experience in reading graphs  

## Context

Global warming has been observed since the pre-industrial period (between 1850 and 1900). Although there were different periods of climate change in the history of the earth, the current changes are not simply due to natural causes. It is a global problem, but people in different countries express various degrees of concerns.

## Origin of the dataset

The dataset of this visualization is derived from Berkeley Earth, which is a non-profit organization focused on data science regarding the environment. In this dataset there are multiple tables with lists of temperature anomalies over a timespan from 1750 to 2020. We used this data for visualizing the change and rise of these temperature values and therefore making aware of global warming.  
http://berkeleyearth.lbl.gov/country-list/

## special mark to data quality
There are several gaps (lack of data) in the early years in some countries, but generally the dataset is complete enough to analyse the problem of global warming.

## Task

* visualizing global warming in a understandable and convincing way  
* impressing people with objective evidence  
* In our visualization, user first have an overview of temperature anomalies between 1920 and 2021 in all countries over the world. Then they can have a detail view of each country with a colored bar chart.

## Purpose

The general problem of global warming and climate change does affect every person on the planet, but not everyone is affected in the same way and the same time.
Some countries are currently struggling harder with the outcomes of climate change and some countries will feel the consequences much later.
But as a matter of fact, all countries are or will be affected in some way.  

In this context, the purpose of this visualization is to inform the interested user about the equality and generality of the problem 'global' warming. Therefore all countries can be selected and their data be displayed with the aim to give a wide overview and the possibility of further information at the same time.

## Design relationales


- bar chart  
each bar stands for a year  
the height of bars stands for the value of temperature   
bars to print colors

- colors for temperature difference  
red-warm/blue-cold impression, supported by studies*

- search menu for different countries   
one country at a time, no blend out - destroy the color stripes

- uncertainty not shown   
it will destroy the shape of the bars and make the graph difficult to understand  
user can read it in the tooltip information

- tooltip information for values  
for people who want more precision

- reference and explanation for data
to keep convincing and understandable

## Info Page

- What does temperature anomaly mean?  

A temperature anomaly is the difference from the average (baseline) temperature. We use the averaged absolute temperatures between Jan 1951 and Dec 1980 as the baseline temperature. A positive anomaly indicates the observed temperature was warmer than the baseline (with red color), while a negative anomaly indicates the observed temperature was cooler than the baseline (with blue color).  

Reference: https://www.ncdc.noaa.gov/monitoring-references/dyk/anomalies-vs-temperature  

- What does uncertainty mean?  

The temperatures from Berkeley Earth are observed from a large collection of weather monitoring stations. These stations locate in different areas all around the country, so they have different trends and baselines. The uncertainty represents the 95% confidence interval for statistical noise and spatial undersampling effects.


## Not successfully implemented

On the overview page, we planned to have an interactive graph, where user can klick on each country and enter the detail page for it. However, this feature is not successfully implemented due to lack of time and knowledge.
