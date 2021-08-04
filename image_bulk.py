#!/usr/bin/env python
# coding: utf-8


def Image_Bulk(species_perturbed,species_plotted,lst):
    import os
    import pandas as pd
    import plotly
    import plotly.graph_objs as go
    x = os.listdir()
    y = lst
    with open(y[0]) as myfile:
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
    for i in y:
        na = i.replace('.csv','')
        data = pd.read_csv(i, names=columns, skiprows=1)
        fig.add_trace(go.Scatter(x=data.time, y=data[species_name],
                        mode='lines',
                        name=na))
    fig.update_layout(xaxis_title='Time (seconds)',
                       yaxis_title='Concentration (uM)')
    fig.update_layout(
        yaxis = dict(
            showexponent = 'all',
            exponentformat = 'e'
        )
    )
    fig.show()




