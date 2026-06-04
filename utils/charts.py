import plotly.express as px

# Population Growth Chart
def population_chart(df):

    fig = px.line(
        df,
        x="Year",
        y="Population",
        markers=True,
        title="India Population Growth"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    return fig


# Fertility Rate Chart
def fertility_chart(df):

    fig = px.bar(
        df,
        x="Year",
        y="Fertility Rate",
        color="Fertility Rate",
        title="Fertility Rate Analysis"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    return fig


# Urban Population Chart
def urban_chart(df):

    fig = px.area(
        df,
        x="Year",
        y="Urban Population",
        title="Urban Population Growth"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    return fig


# World Share Chart
def world_share_chart(df):

    fig = px.scatter(
        df,
        x="Year",
        y="Country's Share of World Pop",
        size="Population",
        color="Population",
        title="India Share in World Population"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    return fig
