
# coding: utf-8

# In[12]:


import plotly
plotly.__version__
plotly.tools.set_credentials_file(username='kyle777', api_key='aDZyXDOPFiN1j5S6btB2')
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()
import itertools
from random import shuffle
import random
from collections import OrderedDict 
import json

with open('comparative.json') as f:
    data = json.load(f)
f.close()
print(len(data))
from random import randint

# Global list of values. Each parameter will be set to one random value from each list

# CSS Colors recognized by plotly
# https://community.plot.ly/t/plotly-colours-list/11730/2
colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgrey", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "grey", "green", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgrey", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]
markerlinecolor = colors[randint(0, len(colors) - 1)]

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

# Values specific to data
# filename = 'filename_goes_here'
# title = "title_goes_here"
# xaxis_title = "xaxis_title_goes_here"
# yaxis_title = "yaxis_title_goes_here"
# labels = ['a','b','c','d','e','f']
# values1 = [randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16)]
# values2 = [randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16)]
xaxis_title = "countries"
for i in range(len(data)):
    filename=""
    values_dict={}
    labels=[]
    values1=[]
    values2=[]

    #print(data[i])
    for key in data[i]:
       filename=key
       title=key
       values_dict=data[i][key]

    b=list(values_dict.items())
    shuffle(b)
    values_dict=OrderedDict(b)
    value_dict={k: v for k, v in values_dict.items() if v}
    values_dict={}
    for key in value_dict:
        y= value_dict[key].split()
        if(y[0].endswith("%")):
            y[0]=y[0].replace("%","")
        if(float(y[0].replace(",",""))!=0):
            values_dict.update({key:value_dict[key]})
            
        
    values_dict=dict(itertools.islice(values_dict.items(), random.randint(5,12)))
    print(values_dict)

    labels=[]
    values1=[]
    values2=[]
    multipliers = {'thousand':1000, 'million':1000000, 'billion':1000000000, 'trillion':1000000000000}
    for key in values_dict:
        print(key)
        labels.append(key)
        values2.append(key)
        i=values_dict[key]
        if i is None:
            continue
        if(type(i)==int):
            value=i
        else:
            label=""
            y=i.split()
            if(y[0].endswith("%")):
                value=i[:i.index("%")]
                label=i[i.index("%"):]
                label=label.replace('%','Percentage')
                #print("value="+str(value)+", label="+label)
            else:
                value=y[0].replace(',','')
                if len(y) > 1:
                    if y[1] in multipliers:
                        mult = multipliers[y[1]] 
                        value=float(value)*int(mult)
                        if len(y) >2:
                            label=i[i.index(y[2]):]
                    else:
                        label=i[i.index(y[1]):]
                        #print("value="+str(value)+", label="+label)
        values1.append(value)
        yaxis_title = label
        


    trace1 = go.Scatter(
        #name = "name1_goes_here",
        x = labels if orientation == 'v' else values1,
        y = values1 if orientation == 'v' else labels,
        text = values1 if orientation == 'v' else labels,
        textfont = dict(
            family = fontfamily,
            color = fontcolor,
            size = fontsize
        ),
        mode = 'markers',
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
        orientation = orientation
    )

    trace2 = go.Scatter(
        name = "name1_goes_here",
        x = labels if orientation == 'v' else values2,
        y = values2 if orientation == 'v' else labels,
        text = values1 if orientation == 'v' else labels,
        textfont = dict(
            family = fontfamily,
            color = fontcolor,
            size = fontsize
        ),
        mode = 'markers',
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
        orientation = orientation
    )

    data_val = [trace1] #if randint(0, 1) == 0 else [trace1, trace2]

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
            l=130, 
            pad=2
        ),
        plot_bgcolor=colors[randint(0, len(colors) - 1)],
        showlegend=False,
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
            tickmode='auto',
            ticks='outside',
            tick0=0,
            dtick=1,
            ticklen=4,
            tickwidth=1,
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
            tickwidth=1,
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

    fig = go.Figure(data=data_val, layout=layout)
    filename=filename.replace("/","-")
    print(filename)

    plotly.offline.plot(fig, filename=filename, image = 'png', image_filename=filename,
                 output_type='file', image_width=800, image_height=600)

