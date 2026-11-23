import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display


df=pd.read_csv("cosmetics.csv")
print(df.head(5))
print("products types:")
print(df["Label"].unique())

#one product one skintype
# Filter for moisturizers
moisturizers = df[df['Label'] == 'Moisturizer']

# Filter for dry skin as well
moisturizers_dry = moisturizers[moisturizers['Dry']== 1]
print(moisturizers_dry.head())

# Reset index
moisturizers_dry = moisturizers_dry.reset_index(drop = True)


#Tokenizing the ingredients
# Initialize dictionary, list, and initial index
ingredient_idx = {}
corpus = []
idx = 0

# For loop for tokenization
for i in range(len(moisturizers_dry)):
    ingredients = moisturizers_dry['Ingredients'][i]
    ingredients_lower = ingredients.lower()
    tokens = ingredients_lower.split(', ')
    corpus.append(tokens)
    for ingredient in tokens:
        if ingredient not in ingredient_idx:
            ingredient_idx[ingredient] = idx
            idx += 1

# Check the result
print("The index for decyl oleate is", ingredient_idx['decyl oleate'])


M = len(corpus)
N = len(ingredient_idx)
A = np.zeros((M,N))

#creating a counter function

def oh_encoder (tokens):
    x = np.zeros(N)
    for ingredient in tokens:
        idx = ingredient_idx[ingredient]
        x[idx]=1
    return x

i=0
for tokens in corpus:
    A[i] = oh_encoder(tokens)
    i += 1


#dimension reduction with T-SNE

from sklearn.manifold import TSNE

model = TSNE(n_components = 2, random_state = 42)
tsne_features = model.fit_transform(A)

moisturizers_dry['X'] = tsne_features[:,0]
moisturizers_dry['Y'] = tsne_features[:,1]


#map with Bokeh

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool


# Make a source and a scatter plot
source = ColumnDataSource(moisturizers_dry)
plot = figure(x_axis_label = 'T-SNE 1',
              y_axis_label = 'T-SNE 2',
              width = 500, height = 400)
plot.scatter(x = 'X',
    y = 'Y',
    source = source,
    size = 10, marker="circle", color = '#FF7373', alpha = 0.8)

show(plot)






# Create a HoverTool object
from bokeh.models import HoverTool
hover = HoverTool(tooltips = [("Name", "@Name"),
    ("Brand", "@Brand"),
    ("Price", "@Price"),
    ("Label", "@Label")])
plot.add_tools(hover)

output_file("tsne_plot.html")
show(plot)



# Plot the map
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

source = ColumnDataSource(moisturizers_dry)

plot = figure(
    width=500,
    height=400,
    x_axis_label="T-SNE 1",
    y_axis_label="T-SNE 2"
)

plot.scatter(
    x='X',
    y='Y',
    source=source,
    size=10,
    color="red"
)

show(plot)




# Print the ingredients of two similar cosmetics
cosmetic_1 = moisturizers_dry[moisturizers_dry['Name'] == "Color Control Cushion Compact Broad Spectrum SPF 50+"]
cosmetic_2 = moisturizers_dry[moisturizers_dry['Name'] == "BB Cushion Hydra Radiance SPF 50"]

# Display each item's data and ingredients
display(cosmetic_1)
print(cosmetic_1.Ingredients.values)
display(cosmetic_2)
print(cosmetic_2.Ingredients.values)

