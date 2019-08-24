### Requirements
```
plotly
jupyter
```

### Run
```
jupyter notebook main.ipynb
```

### Browse
```
localhost:8888
```

### Steps
* Run all function cells
* Plotly limits images to 100 per 24 hours. Change keys if this happens. Some keys can be found [here](https://github.com/hexhog/THE-QA/tree/graphgen/Plotly).
* Pass the correct parameters to `graph` function to generate image

### Sample parameters
```
graph("p", "GDP - composition, by sector of origin industry")
graph("s", "Industrial production growth rate")
graph("b", "Industrial production growth rate")
graph("t", "imports",["United Kingdom","United States"])
```
