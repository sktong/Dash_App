#!/usr/bin/env python
# coding: utf-8

# In[1]:
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px

# In[4]:
df_dates_only=pd.read_excel('First_Dash_Memo.xlsx')
# In[5]:

#app = JupyterDash(__name__)
app = dash.Dash(__name__)
server = app.server
# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("My First Dash Demo", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_name",
                 options=[
                     {"label": "ARVIND LIMITED", "value": "ARVIND LIMITED"},
                     {"label": "GBX TRADING FZE", "value": "GBX TRADING FZE"},
                     {"label": "CRESCENT BAHUMAN LTD", "value": "CRESCENT BAHUMAN LTD"}],
                 multi=False,
                 value="ARVIND LIMITED",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='boxplot', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='boxplot', component_property='figure')],
    [Input(component_id='slct_name', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The seller name chosen by user was: {}".format(option_slctd)
    dff = df_dates_only.copy()
    dff = dff[dff["Seller Name"] == option_slctd]


    # Plotly Express
    fig = go.Figure()
    fig.add_trace(go.Box(
    x=dff['Seller Name'],
    y=dff['PAD PMT Days'],
    name='PAD PMT Days',
    marker_color='#ffbe00'))
    fig.update_layout(title={
        'text': "Tenor Days Per Seller Entity",
        'y':0.95,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'bottom'},
        xaxis_title='Seller Name',
        yaxis_title='PAD PMT Days',
        legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1),
    boxmode='group')
    

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

#app.run_server(mode='external')


# In[ ]:




