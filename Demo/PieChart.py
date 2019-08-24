
# coding: utf-8

# In[5]:


import plotly
plotly.__version__
plotly.tools.set_credentials_file(username='kyle777', api_key='aDZyXDOPFiN1j5S6btB2')
import json
import plotly.plotly as py
import plotly.graph_objs as go
from pprint import pprint
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()
import itertools
from random import shuffle
import random
from collections import OrderedDict 

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
fontsizes = [16, 17, 18, 19, 20, 21, 22, 23, 24]

# Font families
# https://plot.ly/python/reference/#bar-textfont-family
fontfamilies = ["Arial", "Balto", "Courier New", "Droid Sans", "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old Standard TT", "Open Sans", "Overpass", "PT Sans Narrow", "Raleway", "Times New Roman"]
fontfamily = fontfamilies[randint(0, len(fontfamilies) - 1)]
fontcolor = fontcolors[randint(0, len(fontcolors) - 1)]
fontsize = fontsizes[randint(0, len(fontsizes) - 1)]

# TextInfo
# https://plot.ly/python/reference/#pie-textinfo
textinfos = ["label+value", "label+percent", "label+value+percent"]

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
# filename = 'filename_goes_here'
# title = "title_goes_here"
# xaxis_title = "xaxis_title_goes_here"
# yaxis_title = "yaxis_title_goes_here"
# labels = ['a','b','c','d','e','f']
# values = [randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16), randint(4, 16)] 
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
    values=[]
    #values2=[]
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
        values.append(value)
        yaxis_title = label
        

        
        
#     for key in values_dict:
#         labels.append(key)
#         print("key"+key)
#         values2.append(key)
#         print(values_dict[key])
#         values1.append(values_dict[key])


# # Values specific to data
# filename = key
# title = key
    xaxis_title = "countries"
  
    trace = go.Pie(
        name = "name1_goes_here",
        labels = labels,
        values = values,
        textinfo = textinfos[randint(0, len(textinfos) - 1)],
        textposition = "outside",
        textfont = dict(
            size = fontsizes[randint(0, len(fontsizes) - 1)],
            color = colors[randint(0, len(colors) - 1)]
        ),
        sort = True,
        direction = directions[randint(0, len(directions) - 1)],
        rotation = randint(-360, 360),
        pull = pulls[randint(0, len(pulls) - 1)],
        hole = 0.5 if randint(0, 1) == 0 else 0,
        marker = dict(
            colors = [colors[randint(0, len(colors) - 1)] for x in labels],
            line = dict(
                color = colors[randint(0, len(colors) - 1)],
                width = markerWidths[randint(0, len(markerWidths) - 1)]
            )
        )
    )

    data_val = [trace]

    layout = go.Layout( 
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
    )

    fig = go.Figure(data=data_val, layout=layout)
    filename=filename.replace("/","-")
    print(filename)

    plotly.offline.plot(fig, filename=filename, image = 'png', image_filename=filename,
             output_type='file', image_width=800, image_height=600)
    

