import plotly.graph_objects as go
import pandas as pd
import numpy as np

baseURL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"

def loadDataUS_details(fileName, columnName, drop_pop = True): 
    data = pd.read_csv(baseURL + fileName) #.drop(['Lat', 'Long_'], axis=1) 
    data.drop(columns=['UID','iso2','iso3','code3','FIPS','Combined_Key'],inplace=True, errors='ignore') 
    if drop_pop:
        data.drop(columns=['Population'],inplace=True, errors='ignore')
    data = data.groupby(['Province_State','Country_Region','Admin2','Lat', 'Long_']).sum().reset_index()                                                                                             
    data = data.melt(id_vars=['Province_State', 'Country_Region','Admin2','Lat', 'Long_'], var_name='date', value_name=columnName) \
             .astype({'date':'datetime64[ns]', columnName:'Int64'}, errors='ignore')
    data.rename(columns={'Province_State':'Province/State','Country_Region':'Country/Region','Admin2':'County'},inplace=True)
    data[columnName].fillna(0, inplace=True)
    data = data.query('date >="2020-03-01"')
    return data

USData_d = loadDataUS_details("time_series_covid19_confirmed_US.csv", "CumConfirmed") \
    .merge(loadDataUS_details("time_series_covid19_deaths_US.csv", "CumDeaths")) 

USData_pop = loadDataUS_details("time_series_covid19_deaths_US.csv", "Population", False).query('date == "Population"')

date_max = max(USData_d.date)
USData_m = USData_d.query('date == "{}"'.format(date_max))  

USData_m['text'] = USData_m['Province/State'] + ', ' + USData_m['County'] + ', ' + USData_m['CumConfirmed'].astype(str) \
        + ', ' +   USData_m['CumDeaths'].astype(str)

scl = [0,"rgb(150,0,90)"],[0.125,"rgb(0, 0, 200)"],[0.25,"rgb(0, 25, 255)"],\
[0.375,"rgb(0, 152, 255)"],[0.5,"rgb(44, 255, 150)"],[0.625,"rgb(151, 255, 0)"],\
[0.75,"rgb(255, 234, 0)"],[0.875,"rgb(255, 111, 0)"],[1,"rgb(255, 0, 0)"]

#metric = 'CumConfirmed'
metric = 'CumDeaths'

fig = go.Figure(data=go.Scattergeo(
        #locationmode = 'USA-states',
        lon = USData_m['Long_'],
        lat = USData_m['Lat'],
        text = USData_m['text'],
        mode = 'markers',
        #marker_color = USData_d['CumConfirmed'],
        marker = dict(
            size = 4,
            opacity = 0.95,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Electric', #scl, #'Blues',
            cmin = 0,
            color = USData_m[metric],
            cmax = np.percentile(USData_m[metric],[99.5])[0],
            colorbar_title="Confirmed <br>April 2020"
        )
))

fig.update_layout(
        title = 'Covid-19 US map <br>(Hover for status)',
        #geo_scope='usa',
        geo = dict(
            scope='usa',
            projection_type='albers usa',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        )
)
fig.show()