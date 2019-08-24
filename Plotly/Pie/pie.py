import plotly
plotly.__version__
plotly.tools.set_credentials_file(username='kyle111', api_key='SHAeUJNMis7aXUb3wh4d')
import plotly.plotly as py
import plotly.graph_objs as go

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
fontsizes = [16, 17, 18, 19, 20, 21, 22, 23, 24]

# Font families
# https://plot.ly/python/reference/#bar-textfont-family
fontfamilies = ["Arial", "Balto", "Courier New", "Droid Sans", "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old Standard TT", "Open Sans", "Overpass", "PT Sans Narrow", "Raleway", "Times New Roman"]
fontfamily = fontfamilies[randint(0, len(fontfamilies) - 1)]
fontcolor = fontcolors[randint(0, len(fontcolors) - 1)]
fontsize = fontsizes[randint(0, len(fontsizes) - 1)]

# TextInfo
# https://plot.ly/python/reference/#pie-textinfo
textinfos = ["value", "percent", "value+percent"]

# Direction
# https://plot.ly/python/reference/#pie-direction
directions = ["clockwise", "counterclockwise"]

# Pull
# https://plot.ly/python/reference/#pie-pull
pulls = [0, 0.02, 0, 0.04, 0, 0.06, 0, 0.08, 0, 0.1]

# Marker width
# https://plot.ly/python/reference/#pie-marker-line-width
markerWidths = [0, 1, 2, 3, 4]

# Values specific to data
filename = 'filename_goes_here'
title = "title_goes_here"
xaxis_title = "xaxis_title_goes_here"
yaxis_title = "yaxis_title_goes_here"
labels = ['a','b','c','d','e','f']
values = [randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16)] 
  
trace = go.Pie(
    name = "name1_goes_here",
    labels = labels,
    values = values,
    textinfo = textinfos[randint(0, len(textinfos) - 1)],
    hoverinfo = "none",
    textposition = "auto",
    textfont = dict(
        size = fontsizes[randint(0, len(fontsizes) - 1)],
        color = colors[randint(0, len(colors) - 1)]
    ),
    sort = True,
    direction = directions[randint(0, len(directions) - 1)],
    rotation = randint(-360, 360),
    pull = pulls[randint(0, len(pulls) - 1)],
    hole = 0.5 if (randint(0, 1000) % 2) == 0 else 0,
    marker = dict(
        colors = [colors[randint(0, len(colors) - 1)] for x in labels],
        line = dict(
            color = colors[randint(0, len(colors) - 1)],
            width = markerWidths[randint(0, len(markerWidths) - 1)]
        )
    )
)

data = [trace]

title_locs = [(0.5,1.1,100,0),(0.5,-0.1,0,100)]
title_loc = title_locs[randint(0, 1000) % 2]

legend_locs = [(1.1, 0.1), (1.1, 0.9), (-0.1, 0.9), (-0.1, 0.1)]
legend_loc = legend_locs[randint(0, len(legend_locs) - 1)]

layout = go.Layout( 
    autosize=False,
    annotations=[
        dict(
            x=title_loc[0],
            y=title_loc[1],
            showarrow=False,
            text=title,
            xref='paper',
            yref='paper',
            font=dict(
              color="black",
              family=fontfamily,
              size=fontsizes[randint(0, len(fontsizes) - 1)]
          ),
        ),
    ],
    plot_bgcolor=colors[randint(0, len(colors) - 1)],
    showlegend=True,
    legend=dict(
        x=legend_loc[0],
        y=legend_loc[1],
    ),
    height=800,
    width=800,
    margin=dict(
        t=title_loc[2],
        b=title_loc[3],
    ),
)

fig = go.Figure(data=data, layout=layout)


py.iplot(fig, filename=filename)
