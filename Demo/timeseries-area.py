
# coding: utf-8

# In[195]:


import plotly
plotly.__version__
plotly.tools.set_credentials_file(username='kyle777', api_key='aDZyXDOPFiN1j5S6btB2')
import plotly.plotly as py
import plotly.graph_objs as go
import json
from random import shuffle
from collections import OrderedDict 
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()




from random import randint
with open('timeseries.json') as f:
    data = json.load(f)
f.close()
print(len(data))
import random

# Global list of values. Each parameter will be set to one random value from each list

# CSS Colors recognized by plotly
# https://community.plot.ly/t/plotly-colours-list/11730/2
colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgrey", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "grey", "green", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgrey", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]
markerlinecolor = colors[randint(0, len(colors) - 1)]

fillcolors = ['rgba(255, 0, 0, 0.1)', 'rgba(0, 255, 0, 0.1)', 'rgba(0, 0, 255, 0.1)', 'rgba(255, 255, 0, 0.1)', 'rgba(0, 255, 255, 0.1)', 'rgba(255, 0, 255, 0.1)',]

# Font colors
fontcolors = ["white", "black"]

# Font sizes
# https://plot.ly/python/reference/#bar-textfont-size
fontsizes = [24, 25, 26, 27, 28, 29, 30, 31, 32]

# Font families
# https://plot.ly/python/reference/#bar-textfont-family
fontfamilies = ["Arial", "Balto", "Courier New", "Droid Sans", "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old Standard TT", "Open Sans", "Overpass", "PT Sans Narrow", "Raleway", "Times New Roman"]
fontfamily = fontfamilies[randint(0, len(fontfamilies) - 1)]
fontcolor = fontcolors[randint(0, len(fontcolors) - 1)]
fontsize = fontsizes[randint(0, len(fontsizes) - 1)]

# https://plot.ly/python/reference/#bar-textposition
textpositions = ['inside', 'none']
textposition = textpositions[randint(0, len(textpositions) - 1)]

# Bar widths
barwidths = [0, 1, 2, 3]
markerwidth = barwidths[randint(0, len(barwidths) - 1)]

# Orientations
# https://plot.ly/python/reference/#scatter-orientation
orientations = ['v']
orientation = orientations[randint(0, len(orientations) - 1)]

# Barmodes
# https://plot.ly/python/reference/#layout-barmode
barmodes = ["stack", "group"]

# Dashes
# https://plot.ly/python/reference/#scatter-line-dash
dashes = ["solid", "dot", "dash", "longdash", "dashdot", "longdashdot"]
dash = dashes[randint(0, len(dashes) - 1)]

# Shapes
# https://plot.ly/python/reference/#scatter-line-shape
shapes = ["linear", "spline"]
shape = shapes[randint(0, len(shapes) - 1)]

# Marker Symbols
# https://plot.ly/python/reference/#scatter-marker-symbol
markerSymbols = ["circle", "circle-open", "circle-dot", "circle-open-dot", "square", "square-open", "square-dot", "square-open-dot", "diamond", "diamond-open", "diamond-dot", "diamond-open-dot", "cross", "cross-open", "cross-dot", "cross-open-dot", "x", "x-open", "x-dot", "x-open-dot", "triangle-up", "triangle-up-open", "triangle-up-dot", "triangle-up-open-dot", "triangle-down", "triangle-down-open", "triangle-down-dot", "triangle-down-open-dot", "triangle-left", "triangle-left-open", "triangle-left-dot", "triangle-left-open-dot", "triangle-right", "triangle-right-open", "triangle-right-dot", "triangle-right-open-dot", "triangle-ne", "triangle-ne-open", "triangle-ne-dot", "triangle-ne-open-dot", "triangle-se", "triangle-se-open", "triangle-se-dot", "triangle-se-open-dot", "triangle-sw", "triangle-sw-open", "triangle-sw-dot", "triangle-sw-open-dot", "triangle-nw", "triangle-nw-open", "triangle-nw-dot", "triangle-nw-open-dot", "pentagon", "pentagon-open", "pentagon-dot", "pentagon-open-dot", "hexagon", "hexagon-open", "hexagon-dot", "hexagon-open-dot", "hexagon", "hexagon-open", "hexagon-dot", "hexagon-open-dot", "octagon", "octagon-open", "octagon-dot", "octagon-open-dot", "star", "star-open", "star-dot", "star-open-dot", "hexagram", "hexagram-open", "hexagram-dot", "hexagram-open-dot", "star-triangle-up", "star-triangle-up-open", "star-triangle-up-dot", "star-triangle-up-open-dot", "star-triangle-down", "star-triangle-down-open", "star-triangle-down-dot", "star-triangle-down-open-dot", "star-square", "star-square-open", "star-square-dot", "star-square-open-dot", "star-diamond", "star-diamond-open", "star-diamond-dot", "star-diamond-open-dot", "diamond-tall", "diamond-tall-open", "diamond-tall-dot", "diamond-tall-open-dot", "diamond-wide", "diamond-wide-open", "diamond-wide-dot", "diamond-wide-open-dot", "hourglass", "hourglass-open", "bowtie", "bowtie-open", "circle-cross", "circle-cross-open", "circle-x", "circle-x-open", "square-cross", "square-cross-open", "square-x", "square-x-open", "diamond-cross", "diamond-cross-open", "diamond-x", "diamond-x-open", "cross-thin", "cross-thin-open", "x-thin", "x-thin-open", "asterisk", "asterisk-open", "hash", "hash-open", "hash-dot", "hash-open-dot", "y-up", "y-up-open", "y-down", "y-down-open", "y-left", "y-left-open", "y-right", "y-right-open", "line-ew", "line-ew-open", "line-ns", "line-ns-open", "line-ne", "line-ne-open", "line-nw", "line-nw-open"]
markerSymbol = markerSymbols[randint(0, len(markerSymbols) - 1)]

markerSizes = [6, 7, 8, 9, 10, 11, 12]
markerSize = markerSizes[randint(0, len(markerSizes) - 1)]

lineWidths = [1, 2, 3, 4, 5, 6]
lineWidth = lineWidths[randint(0, len(lineWidths) - 1)]

# # Values specific to data
# filename = 'filename_goes_here'
# title = "title_goes_here"
xaxis_title = "Time"
yaxis_title = ""
# labels = ['a','b','c','d','e','f']
# values1 = [randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16)]
# values2 = [randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16)]
dict_data={}
for i in data:
    #print(i)
    for key in i:
        #print(key)
        dict_data.update({key:i[key]})
        #dict_data.update({})
b=list(dict_data.items())
shuffle(b)
dict_data=OrderedDict(b)
    
topics=dict(itertools.islice(dict_data.items(),2))

legend_names=[]
#print(len(topics))
for topic in topics:
    legend_names.append(topic)

val1=topics.get(legend_names[0])
val2=topics.get(legend_names[1])


multipliers = {'thousand':1000, 'million':1000000, 'billion':1000000000, 'trillion':1000000000000}
for value in val1:
    values1=[]
    values2=[]
    labels=[]
    filename=title=value
    entry1=val1.get(value)
    entry2=val2.get(value)
    for entry in entry1:
        labels.append(entry[0])
        y=entry[1].split()
        if(y[0].endswith("%")):
            value=entry[1][:entry[1].index("%")]
            label=entry[1][entry[1].index("%"):]
            label=label.replace('%','Percentage')
                #print("value="+str(value)+", label="+label)
        else:
            value=y[0].replace(',','')
            if len(y) > 1:
                if y[1] in multipliers:
                    mult = multipliers[y[1]] 
                    if(value.find("$")!=-1 ):
                        label=str(mult)+" dollars"
                    else:
                        label=str(mult)
#                     value=value.replace("$","")
#                     value=float(value)*int(mult)
                    if len(y) >2:
                        label=entry[1][entry[1].index(y[2]):]
                    else:
                        label=entry[1][entry[1].index(y[1]):]
        values1.append(value)
        yaxis_title=label
    for entry in entry2:
        labels.append(entry[0])
        y=entry[1].split()
        if(y[0].endswith("%")):
            value=entry[1][:entry[1].index("%")]
            label=entry[1][entry[1].index("%"):]
            label=label.replace('%','Percentage')
                #print("value="+str(value)+", label="+label)
        else:
            value=y[0].replace(',','')
            if len(y) > 1:
                if y[1] in multipliers:
                    mult = multipliers[y[1]] 
                    if(value.find("$")!=-1 ):
                        label=str(mult)+" dollars"
                    else:
                        label=str(mult)
                    #value=value.replace("$","")
                    #value=float(value)*int(mult)
                    if len(y) >2:
                        label=entry[1][entry[1].index(y[2]):]
                    else:
                        label=entry[1][entry[1].index(y[1]):]

        values2.append(value)
        yaxis_title=label
    print(labels)
    print(values1)
    print(values2)
    trace1 = go.Scatter(
        name = legend_names[0],
        x = labels if orientation == 'v' else values1,
        y = values1 if orientation == 'v' else labels,
        text = values1 if orientation == 'v' else labels,
        textfont = dict(
            family = fontfamily,
            color = fontcolor,
            size = fontsize
        ),
        mode = 'lines+markers',
        hoverinfo = "none",
        marker = dict(
            color = colors[randint(0, len(colors) - 1)],
            symbol = markerSymbol, 
            size = markerSize, 
        ),
        line = dict(
            color = colors[randint(0, len(colors) - 1)],
            width = lineWidth,
            dash = dash,
            shape = shape,
        ),
        fill = "tozeroy" if orientation == 'v' else "tozerox",
        fillcolor = fillcolors[randint(0, len(fillcolors) - 1)],
        orientation = orientation
    )

    trace2 = go.Scatter(
        name = legend_names[1],
        x = labels if orientation == 'v' else values2,
        y = values2 if orientation == 'v' else labels,
        text = values1 if orientation == 'v' else labels,
        textfont = dict(
            family = fontfamily,
            color = fontcolor,
            size = fontsize
        ),
        mode = 'lines+markers',
        hoverinfo = "none",
        marker = dict(
            color = colors[randint(0, len(colors) - 1)],
            symbol = markerSymbol, 
            size = markerSize, 
        ),
        line = dict(
            color = colors[randint(0, len(colors) - 1)],
            width = lineWidth,
            dash = dash,
            shape = shape,
        ),
        fill = "tozeroy" if orientation == 'v' else "tozerox",
        fillcolor = fillcolors[randint(0, len(fillcolors) - 1)],
        orientation = orientation
    )

    data = [trace1,trace2] #if randint(0, 1) == 0 else [trace1, trace2]

    layout = go.Layout( 
        barmode = barmodes[randint(0, len(barmodes) - 1)],
        bargap=0.3, 
        bargroupgap=0, 
        boxgap=0.3, 
        boxgroupgap=0.3, 
        boxmode="overlay", 
        autosize=False,
        title=title,
        titlefont=dict(
            color="black",
            family=fontfamily,
            size=fontsizes[randint(0, len(fontsizes) - 1)]
        ),
        margin=dict(
            r=80, 
            t=80, 
            b=80, 
            l=80, 
            pad=2
        ),
        plot_bgcolor=colors[randint(0, len(colors) - 1)],
        showlegend=True,
        height=800,
        width=800, 
        xaxis=dict(
            title=xaxis_title,
            titlefont=dict(
                family=fontfamily,
                size=18,
                color='black'
            ),
            showticklabels=True,
            tickfont=dict(
                family=fontfamily,
                size=14,
                color='black'
            ),
            exponentformat='none',
            showexponent='all',
            tickmode='linear',
            ticks='outside',
            tick0=0,
            dtick=1,
            ticklen=4,
            tickwidth=2,
            tickcolor='#000',
            mirror=True,
            showgrid=True,
            showline=True,
            gridcolor='#bdbdbd',
            gridwidth=1,
            linecolor='#636363',
            linewidth=2,
        ),
        yaxis=dict(
            title=yaxis_title,
            titlefont=dict(
                family=fontfamily,
                size=18,
                color='black'
            ),
            showticklabels=True,
            tickfont=dict(
                family=fontfamily,
                size=14,
                color='black'
            ),
            exponentformat='none',
            showexponent='all',
            tickmode='auto',
            ticks='outside',
            tick0=0,
            dtick=1,
            ticklen=4,
            tickwidth=2,
            tickcolor='#000',
            mirror=True,
            showgrid=True,
            showline=True,
            gridcolor='#bdbdbd',
            gridwidth=1,
            linecolor='#636363',
            linewidth=2,
        ),
    )

    fig = go.Figure(data=data, layout=layout)


    plotly.offline.plot(fig, filename=filename, image = 'png', image_filename=filename,
             output_type='file', image_width=800, image_height=600)
    


# In[194]:


import plotly
plotly.__version__
plotly.tools.set_credentials_file(username='kyle777', api_key='aDZyXDOPFiN1j5S6btB2')
import plotly.plotly as py
import plotly.graph_objs as go
import json
from random import shuffle
import itertools

from collections import OrderedDict 



from random import randint
with open('timeseries.json') as f:
    data = json.load(f)
f.close()
import random

dict_data={}
for i in data:
    #print(i)
    for key in i:
        #print(key)
        dict_data.update({key:i[key]})
        #dict_data.update({})
topics=dict(itertools.islice(dict_data.items(),2))

legend_names=[]
#print(len(topics))
for topic in topics:
    legend_names.append(topic)

values1=topics.get(legend_names[0])
values2=topics.get(legend_names[1])
values1plot=[]
values2plot=[]
labels=[]
#values=topics[0]
for value in values1:
    labels=[]
    
    filename=title=value
    entry1=values1.get(value)
    entry2=values2.get(value)
    for entry in entry1:
        labels.append(entry[0])
        values1.append(entry[1])
    for entry in entry2:
        labels.append(entry[0])
        values2plot.append(entry[1])
    print(labels)
    print(values1)
    print(values2plot)
            
                
        
#print(labels)
# print(values1)
# print(values2)
# topics={}
# countries={}
# for i in data:
#     for key in i:
#         countries.update({key:[]})

# #print(countries)
    
# for i in data:
#     for key in i:
#         for k in i[key]:
#             topics.update({k:countries})
            
# print(topics)

# for i in data:
#     for key in i:
#         for k in i[key]:
#             value=topics.get(k)
#             val=value.get(key)
#             #print(val)
#             #print(i[key][k])
#             #print(value)
#             #print(val)
#             #print(type(value))
#             #print(type(val))
#             #print(key)
#             #print(val)
#             val.append(i[key][k])
#             value.update({key:val})
#             #print(k)
#             print(value)
#             topics.update({k:value})

# topics=dict(itertools.islice(topics.items(), random.randint(4,6)))

# for topic in topics:
#     print((topics.get(topic)))
#     #countries=dict(itertools.islice(topics.get(topic).items(),2))
#     #print(countries)
    


# In[ ]:


str=(1990 est)

str.replace("(","")
str.replace("(","")
y=str.split("")
if y[1]==est
    

