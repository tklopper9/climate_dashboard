from dash import dcc, html
import dash_bootstrap_components as dbc

def make_info(text):
    return html.Div([
        html.P([text],className="ml-5 text-right")
    ], className="row")
    
    #return dbc.Card(text, body=True, class_name="card text-right")

def wrap_in_navbar(page):
    return html.Div(
        [
            html.Div([create_simple_navbar()], className = 'row sticky-top'),
            page,
        ],
        style={"text-align": "left"},
    )

def create_simple_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Top", href="#")),
        ],
        brand="Ocean climate data",
        brand_href="#",
        color="primary",
        dark=True,
    )
    return navbar

def two_column_layout(fig1, fig2, fig3, fig4, id1="", id2="", id3="", id4="", text=None):
    layout = html.Div([ #outer frame
            html.Div([ #row
            
                html.Div([ #left column
                    dcc.Graph(
                            figure=fig1, id=id1, style={'height': '90vh'}
                        ),
                    html.P([text],className="ml-5"
                        ),
                    ], className="col-md-6"
                    ),
                
                html.Div([ #right column
                    dcc.Graph(
                            figure=fig2, id=id2, style={'height': '90vh'}
                        ) 
                    ], className='col-md-6'
                    )  
            ],className='row'),

            html.Div([ #2nd row
                    
                html.Div([ #left column
                    dcc.Graph(
                            figure=fig3, id=id3, style={'height': '90vh'}
                        ),
                    html.P([text],className="ml-5"
                        ),
                    ], className="col-md-6"
                    ),
                
                html.Div([ #right column
                    dcc.Graph(
                            figure=fig4, id=id4, style={'height': '90vh'}
                        ) 
                    ], className='col-md-6'
                    )  
            ],className='row')
     ]) 
    

    return layout

def two_x_three_layout(fig1, fig2, fig3, fig4, fig5, id1="", id2="", id3="", id4="", id5="", text=None):
    layout = html.Div([ #outer frame
            html.Div([ #row
            
                html.Div([ #left column
                    dcc.Graph(
                            figure=fig1, id=id1, style={'height': '90vh'}
                        ),
                    html.P([text],className="ml-5"
                        ),
                    ], className="col-md-6"
                    ),
                
                html.Div([ #right column
                    dcc.Graph(
                            figure=fig2, id=id2, style={'height': '90vh'}
                        ) 
                    ], className='col-md-6'
                    )  
            ],className='row'),

            html.Div([ #2nd row
                    
                html.Div([ #left column
                    dcc.Graph(
                            figure=fig3, id=id3, style={'height': '90vh'}
                        ),
                    html.P([text],className="ml-5"
                        ),
                    ], className="col-md-6"
                    ),
                
                html.Div([ #right column
                    dcc.Graph(
                            figure=fig4, id=id4, style={'height': '90vh'}
                        ) 
                    ], className='col-md-6'
                    )  
            ],className='row'),

            html.Div([ #3rd row
                    
                html.Div([ #left column
                    dcc.Graph(
                            figure=fig5, id=id5, style={'height': '90vh'}
                        ),
                    html.P([text],className="ml-5"
                        ),
                    ], className="col-md-6"
                    ),
                
                html.Div([ #empty right column
                    ], className='col-md-6'
                    )  
            ],className='row')
     ]) 
    

    return layout