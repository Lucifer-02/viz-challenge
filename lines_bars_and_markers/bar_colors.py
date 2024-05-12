import altair as alt
import pandas as pd

alt.renderers.enable("browser")

fruits = ["apple", "blueberry", "cherry", "orange"]
counts = [40, 100, 30, 55]
fruit_colors = ["red", "blue", "red", "orange"]



data = pd.DataFrame({"x": fruits, "y": counts})

chart = (
    alt.Chart(data=data)
    .mark_bar()
    .encode(
        x=alt.X("x", title=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y("y", title="fruit supply"),
        color=alt.Color(
            "x",
            title="Fruit color",
            scale=alt.Scale(
                domain=fruits,
                range=fruit_colors,
            ),
        ),
    )
    .properties(
        title="Fruit supply by kind and color",
        height=300,
        width=400,
    )
)
chart.show()
