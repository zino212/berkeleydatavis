#!/usr/bin/env python
# coding: utf-8
import altair as alt
import pandas as pd
import panel as pn
import re
import urllib3 as url
import numpy as np
import datetime as dt
from itertools import product

class MainView():
    alt.data_transformers.disable_max_rows()
    pn.extension('vega')
    dataJune = []
    http = url.PoolManager()
    column = pn.Column()
    temp = 0;
    loadingSpinner = pn.indicators.LoadingSpinner(value = True)
    rangeSlider =  pn.widgets.RangeSlider(name = 'WIP: Date Range Slider', start = 1870, end = 2020, value = (1870, 2020), step = 1)
    country = pn.widgets.AutocompleteInput(name = 'Country', options = [], placeholder = 'Search for country', value = 'afghanistan')
    
    def getCountryList(self):
        r = self.http.request('GET', 'http://berkeleyearth.lbl.gov/country-list')
        countrylist = np.array(re.findall('<tr><td><a href="http://berkeleyearth.lbl.gov/regions/(.*?)">(.*?)</td>', str(r.data)))
        countrylist[:,0]; # liste der Links
        countrylist[:,1]; # liste der Namen der Länder #TODO: Encoding von Sonderzeichen in Ländernamen reparieren
        global country
        country = pn.widgets.AutocompleteInput(name = 'Country', options = countrylist[:,0].tolist(), placeholder = 'Search for country', value = 'afghanistan')



    def loadCountry(self, country_name):
        data = pd.read_csv("http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/" + country_name + "-TAVG-Trend.txt",sep="\s+",engine='python', comment = "%", names=["Year","Month","Monthly Anomaly","Monthly Uncertainty","Annual Anomaly","Annual Uncertainty","Five-year Anomaly","Five-year Uncertainty","Ten-year Anomaly","Ten-year Uncertainty","Twenty-year Anomaly","Twenty-year Uncertainty"]);
        data["YearT"]=pd.to_datetime(data[["Year"]].assign(day=1,month=1));
        temperature=self.http.request("GET","http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/" + country_name + "-TAVG-Trend.txt");
        absolute_temp=re.findall(r'Estimated Jan 1951-Dec 1980 absolute temperature \(C\): (-?\d+\.\d+) \+\/- (\d+\.\d+)',str(temperature.data));
        data["Total Temperature"]=data["Annual Anomaly"]+float(absolute_temp[0][0]);
        dataJune = data[data["Month"]==6];
        global temp
        temp = float(absolute_temp[0][0]);
        return dataJune

    def mainPlot(self, country_name):
        self.column.insert(0,self.loadingSpinner)
        dataJune = self.loadCountry(country_name)
        self.column.remove(self.loadingSpinner)
        return  alt.Chart(dataJune).mark_bar(size=4).encode(
            x = alt.X('YearT:T',title = 'Year', scale = alt.Scale(domain = ['1870-01-01','2021-01-01'], clamp = True)),
            y = alt.Y('Annual Anomaly', title = 'WIP: Deviation from Average (°C)'),
            color = alt.Color('Annual Anomaly', title = 'WIP: Deviation from Average (°C)', scale = alt.Scale(scheme = "redblue", reverse = True, domainMid = 0)),
            tooltip = ['Year','Total Temperature', 'Annual Anomaly','Annual Uncertainty']
            ).properties(
                title = 'WIP: Visualization of climate crisis',
                width = 1000,
                height = 400
            ).configure_legend(
                titleOrient = 'left',
                gradientLength = 400,
                gradientThickness = 30
            )

    @pn.depends(country.param.value)
    def output(self, country_name):
        return pn.Row(
            pn.Column(
                self.mainPlot(country_name),
                self.rangeSlider
            ), 
            pn.Column(
                country,
                pn.widgets.StaticText(name='Average Temp. 1951-1980', value = str(temp)+'°C'),
                pn.pane.HTML("&nbsp;Data Source: <a href='https://berkeleyearth.org/data/' target='_blank' style='color: #0645AD'>Berkeley Earth <img src='https://t3.ftcdn.net/jpg/02/87/13/96/360_F_287139698_MWcmLH0B9rNW12saEE1Q2qVSXnnljjKv.jpg' width=15 height=15></a>")
            ))

    def main(self):
        self.getCountryList()
        view = pn.Row(self.output)

        view.servable()

print('test')
mview = MainView()
MainView.main(mview)


