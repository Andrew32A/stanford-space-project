from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, Range1d

# calculations
measured_stdrows_mc = dfs[itl].stdrows_mc
expected_stdrows_mc = dfs[itl].readnoise_mc/np.sqrt(509)
m_e_stdrows_mc = measured_stdrows_mc/expected_stdrows_mc # plot x

measured_stdrows_row = dfs[itl].stdrows_row
expected_stdrows_row = dfs[itl].readnoise_mc * np.sqrt(1./64. + 1./509.)
m_e_stdrows_row = measured_stdrows_row/expected_stdrows_row # plot y

# data input
source = ColumnDataSource(data = dict(
    m_e_stdrows_mc = measured_stdrows_mc/expected_stdrows_mc,
    m_e_stdrows_row = measured_stdrows_row/expected_stdrows_row
))

# instantiate figure properties
tools = "box_zoom, undo, crosshair, lasso_select"
p = figure(tools=tools,title='Row-by-Row Overscan: ITL', x_axis_label='Read Noise [ADU]', y_axis_label='StdDev of Row Means [ADU]') 

# add hovertool
p.add_tools(
    HoverTool(
        tooltips = [('x', "@m_e_stdrows_mc"),
                    ('y', '@m_e_stdrows_row')]
    )
)

# draw scatter plot
p.scatter("m_e_stdrows_mc", "m_e_stdrows_row", alpha=0.5, source=source)

# range values
p.x_range = Range1d(0, 15)
p.y_range = Range1d(0, 15)

# display plot
show(p)
