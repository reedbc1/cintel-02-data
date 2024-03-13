import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Penguin Data - Brendan", fillable=True)

with ui.sidebar(bg="#f8f8f8", open='open'):
    ui.h2("Sidebar")
    ui.input_selectize("selected_attribute", "selected_attribute",
                       ["bill_length_mm", "bill_depth_mm", 
                        "flipper_length_mm", "body_mass_g"])
    ui.input_numeric("plotly_bin_count", "plotly_bin_count", 50)
    ui.input_slider("seaborn_bin_count", "seaborn_bin_count", 1, 100, 50)
    ui.input_checkbox_group("selected_species_list", "selected_species_list", 
                            ["Adelie", "Gentoo", "Chinstrap"], inline = False)
    ui.hr()
    ui.a("GitHub", href = "https://github.com/reedbc1/cintel-02-data/tree/main", target = "_blank")
    
