#!/usr/bin/env python
# coding: utf-8



def Image(title_name,species_perturbed,species_plotted,result_file):
    import os
    import pandas as pd
    import plotly
    import plotly.graph_objs as go
    y = result_file
    with open(y) as myfile:
        headRow = next(myfile)
    columns = [x.strip('\n').strip('"') for x in headRow.split(',')]
    columns.insert(0,"count")
    var = species_perturbed
    for i in columns:
        if var+"_Amount" in i:
            var_name = i
    species = species_plotted
    for i in columns:
        if species+"_Amount" in i:
            species_name = i
    fig = go.Figure()
    na = y.replace('.csv','')
    data = pd.read_csv(y, names=columns, skiprows=1)
    fig.add_trace(go.Scatter(x=data.time, y=data[species_name],
                        mode='lines',name=na))
    fig.update_layout(title=title_name,
                       xaxis_title='Time (seconds)',
                       yaxis_title='Concentration (uM)')
    fig.update_layout(
        yaxis = dict(
            showexponent = 'all',
            exponentformat = 'e'
        )
    )
    fig.show()
