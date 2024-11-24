from DataSimulator import DataSimulator
from DataVizualizer import DataVisualizer

simulator = DataSimulator(num_records=200)
data = simulator.generate_data()

visualizer = DataVisualizer(data)
visualizer.plot_bar_chart_countries()
visualizer.plot_bar_chart_cities()
visualizer.plot_interactive_map()
visualizer.plot_folium_map()

