import plotly.graph_objects as go

def plotly_table(dataframe):
    header_color = 'grey'
    row_even_color = 'lightgrey'
    row_odd_color = 'white'

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(dataframe.columns),
                    fill_color=header_color,
                    align='left'
                ),
                cells=dict(
                    values=[dataframe[col] for col in dataframe.columns],
                    fill_color=[[row_odd_color, row_even_color] * (len(dataframe) // 2 + 1)],
                    align='left'
                )
            )
        ]
    )

    fig.update_layout(
        height=400,
        margin=dict(l=10, r=10, t=10, b=10),
    )

    return fig  # ← THIS was missing
