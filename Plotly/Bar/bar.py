import plotly
plotly.__version__
plotly.tools.set_credentials_file(username='kyle444', api_key='R4d6KsQwyPfLG9MPJJ82')
import plotly.plotly as py
import plotly.graph_objs as go
import json
from pprint import pprint
import itertools

with open('comparative.json') as f:
    data = json.load(f)
f.close()
print(type(data[0]))
from random import randint
from math import ceil, log

ticks = [5, 10, 20, 25]
def getTicks(n):
    exp = log(n, 10)
    exp = ceil(exp)
    return 10**exp/ticks[randint(0, len(ticks) - 1)]

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
orientations = ['v', 'h']
orientation = orientations[randint(0, len(orientations) - 1)]

# Barmodes
# https://plot.ly/python/reference/#layout-barmode
barmodes = ["stack", "group"]

filename=""
values_dict={}
for key in data[0]:
   filename=key
   title=key
   values_dict=data[0][key]

values_dict=dict(itertools.islice(values_dict.items(), 6))


labels=[]
values1=[]
values2=[]
for key in values_dict:
    labels.append(key)
    print(key)
    values1.append(key)
    print(values_dict[key])
    values2.append(values_dict[key])


# # Values specific to data
# filename = key
# title = key
xaxis_title = "countries"
yaxis_title = title
# labels = [data[0][key],'b','c','d','e','f']
# values1 = [randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16)]
# values2 = [randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16)]


trace1 = go.Bar(
    name = "name1_goes_here",
    x = labels if orientation == 'v' else values1,
    y = values1 if orientation == 'v' else labels,
    text = values1 if orientation == 'v' else labels,
    textposition = textposition,
    textfont=dict(
        family = fontfamily,
        color = fontcolor,
        size = fontsize
    ),
    hoverinfo = "none",
    marker = dict(
        color = colors[randint(0, len(colors) - 1)],
        line = dict(
            color = markerlinecolor,
            width = markerwidth,
        ),
    ),
    orientation = orientation
)

trace2 = go.Bar(
    name = "name2_goes_here",
    x = labels if orientation == 'v' else values2,
    y = values2 if orientation == 'v' else labels,
    text = values2 if orientation == 'v' else labels,
    textposition = textposition,
    textfont=dict(
        family = fontfamily,
        color = fontcolor,
        size = fontsize
    ),
    hoverinfo = "none",
    marker = dict(
        color = colors[randint(0, len(colors) - 1)],
        line = dict(
            color = markerlinecolor,
            width = markerwidth,
        ),
    ),
    orientation = orientation
)

data = [trace1] if (randint(0, 1000) % 2) == 0 else [trace1, trace2]

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
    plot_bgcolor=colors[randint(0, len(colors) - 1)],
    showlegend=True,
    height=125*len(labels) if orientation == 'h' else 1000,
    width=125*len(labels) if orientation == 'v' else 1000,
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
        exponentformat='e',
        showexponent='all',
        tickmode='linear',
        ticks='outside',
        tick0=0,
        dtick=1 if orientation == 'v' else getTicks(max(max(values1), max(values2))),
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
        automargin=True,
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
        exponentformat='e',
        showexponent='all',
        tickmode='linear',
        ticks='outside',
        tick0=0,
        dtick=1 if orientation == 'h' else getTicks(max(max(values1), max(values2))),
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
        automargin=True,
    ),
)

fig = go.Figure(data=data, layout=layout)
print(filename)

py.plot(fig, filename=filename)
