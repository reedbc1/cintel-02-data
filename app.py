import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Penguin Data - Brendan", fillable=True)
