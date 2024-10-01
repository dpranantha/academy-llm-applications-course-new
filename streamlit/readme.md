# Streamlit

The slide deck introduced the streamlit app building library and gave an insight into what is possible. Now it is your turn to start building some apps with Python.

You can work your way through the exercises or, alternatively, take a look at the `widget_examples.py` file.

## Exercise one: A simple line chart

Build your first streamlit application with the code
:
```bash
streamlit run 1_sample_line_chart.py
```

## Exercise two: Interactive

Add some interactivity to your streamlit app by incorporating a [slider](https://docs.streamlit.io/library/api-reference/widgets/st.slider).

## Exercise three: The sidebar

Move your interactive sliders in your app to the sidebar.

## Exercise four: Pandas

Load a dataset into a streamlit app and add interactive filters.

## Exercise five: Pandas ASsignment

In this exercise you will plot the average weight of the chicks over time, per diet. You can use the existing pandas code to wrangle the data and plot it with `st.line_chart`.

1. Write a title for your streamlit app and add any other labels you would like.
2. Add a slidebar to be able to filter on the time column
    - Create variables to store the min and max time (`min_col = df['col'].min()`)
    - Use `st.sidebar.slider` with the min and max time to create streamlit variables
    - Use the `.loc` method to filter (`df.loc[df['col'] <= min_col`)
3. Add a multiselect checkbox to be able to filter on diet
    - Use `st.sidebar.multiselect` with the unique diet variables
    - Use the `.loc` method to filter (`df.loc[df['col'].isin(list_of_unique_values)

## Exercise six: Caching

Using the [`st.cache_data`](https://docs.streamlit.io/library/api-reference/performance/st.cache_data) decorator prevens you having to re-load the data when you make changes to a running application. This can be especially ueful when working with large datasets.

To demonstrate this, load and visualize the NYC Uber Taxi dataset.

Use the [st.date_input](https://docs.streamlit.io/library/api-reference/widgets/st.date_input) widget to select the range of dates you want to be shown.

Add a[st.checkbox](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox) to show the raw data.

## Widgets examples

Run this file to see a demonstration of more interactive widgets you can add to your streamlit apps.