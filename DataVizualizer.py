import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
import webbrowser


class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_bar_chart_countries(self):
        plt.figure(figsize=(12, 8))
        sns.countplot(data=self.data, y='Country', order=self.data['Country'].value_counts().index)
        plt.title('Number of Students per Country')
        plt.xlabel('Number of Students')
        plt.ylabel('Country')
        plt.tight_layout()
        plt.show()

    def plot_bar_chart_cities(self, top_n=10):
        plt.figure(figsize=(12, 8))
        top_cities = self.data['City'].value_counts().nlargest(top_n).index
        sns.countplot(data=self.data[self.data['City'].isin(top_cities)], y='City', order=top_cities)
        plt.title(f'Top {top_n} Cities with Most Students')
        plt.xlabel('Number of Students')
        plt.ylabel('City')
        plt.tight_layout()
        plt.show()

    def plot_interactive_map(self):
        country_counts = self.data['Country'].value_counts().reset_index()
        country_counts.columns = ['Country', 'Count']

        fig = px.choropleth(country_counts, locations="Country",
                            locationmode='country names',
                            color="Count",
                            hover_name="Country",
                            color_continuous_scale=px.colors.sequential.Plasma,
                            title='Number of Students per Country')
        fig.show()

    def plot_folium_map(self):
        world_map = folium.Map(location=[20,0], zoom_start=2)

        marker_cluster = MarkerCluster().add_to(world_map)

        for idx, row in self.data.iterrows():
            try:
                folium.Marker(
                    location=[row['Latitude'], row['Longitude']],
                    popup=folium.Popup(f"<img src='{row['Avatar']}' width='50'>", max_width=100),
                    icon=folium.Icon(icon='user')
                ).add_to(marker_cluster)
            except:
                continue

        world_map.save("students_map.html")
        webbrowser.open("students_map.html")

