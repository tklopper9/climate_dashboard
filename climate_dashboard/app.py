import dash
import dash_bootstrap_components as dbc
from layout_utils.layouts import wrap_in_navbar, two_column_layout
from figures import bubble_map_species_by_year

external_stylesheets = ['styles/001_bootstrap.css', dbc.themes.BOOTSTRAP]

def main():
    fig1 = bubble_map_species_by_year(2015)
    fig2 = bubble_map_species_by_year(2021)
    fig3 = bubble_map_species_by_year(2022)
    fig4 = bubble_map_species_by_year(2023)

    app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

    app.layout = wrap_in_navbar(two_column_layout(fig1, fig2, fig3, fig4))

    app.run(host="0.0.0.0", port=8051, debug=True, use_reloader=False)


if __name__ == "__main__":

    main()