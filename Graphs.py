from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd

"""
@Author: Jacob Sprouse
@Description: class Graphs utilizes matplotlib to create a figure 
              and associate that figure to a plot in order to add 
              the graphical data to the GUI.
@Date: 2024/04/21
"""


class Graphs:
    def __init__(self):
        pass

    def create_plot_canvas(self):
        figure = Figure()
        plot_canvas = FigureCanvas(figure)  # makes the figure object on a canvas to add graphical plots into GUI
        plot = figure.add_subplot(111)      # sub plot to add each individual data into the canvas figure
        return plot_canvas, plot            # sets a clean plot_canvas and plot object for each graph function use

    """
    company_cybercrime_data: dataframe containing cybercrime breaches of major companies
    plot.bar(creates the x-axis data which in this case is the name of the company, 
            company_data['Amount of users affected '] is what is measured as the y-axis.)
    plot.legend() creates a legend based on the label='' in each plot.bar or other plots
    returns the plot_canvas to add to the GUI as a visual plot of graphical data
    """
    def company_cybercrime_data(self):
        plot_canvas, plot = self.create_plot_canvas()
        company_data = pd.read_csv('Data/CompanyData.csv')
        bar_colors = ['tab:purple', 'tab:red', 'tab:blue', 'tab:pink', 'tab:green', 'tab:orange']

        plot.bar(company_data['Company Name'], company_data['Amount of Users Affected'],
                 label=company_data['Company Name'], color=bar_colors)
        plot.set_title('Major company Cyber Breaches')  # sets title of the graph
        plot.set_xlabel('Company Name')                 # sets the label of the x-axis
        plot.set_ylabel('Amount of Users Affected')     # sets the label of the y-axis
        plot.legend()                                   # creates the legend specific to the label=''

        # return canvas and to be added to the stacked widget
        return plot_canvas

    def united_states_cybercrime_data(self):
        plot_canvas, plot = self.create_plot_canvas()
        US_data = pd.read_csv('Data/US_Data.csv')

        plot.plot(US_data['Year'], US_data['Data Compromises'],
                       label='Data Compromises', color='tab:blue')
        plot.plot(US_data['Year'], US_data['Number of records exposed in millions'],
                       label='Number of records exposed in millions', color='tab:red')
        plot.plot(US_data['Year'], US_data['Amount of Users Affected in millions'],
                       label='Amount of Users Affected in millions', color='tab:purple')
        plot.set_title('United States Cyber Crime Data')
        plot.set_xlabel('Year')
        plot.set_ylabel('Number of compromises and impacted individuals')
        plot.legend()

        return plot_canvas

    def russian_cybercrime_data(self):
        plot_canvas, plot = self.create_plot_canvas()
        Russian_data = pd.read_csv('Data/RussiaData.csv')

        plot.bar(Russian_data['Year'], Russian_data['Amount of Users Affected in millions'],
                      label='Russian Cyber Crime Data')
        plot.set_title('Russian Cyber Crime Data')
        plot.set_xlabel('Year')
        plot.set_ylabel('Amount of Crimes exposed in millions')
        plot.legend()

        return plot_canvas

    def chinese_cybercrime_data(self):
        plot_canvas, plot = self.create_plot_canvas()
        China_data = pd.read_csv('Data/ChinaData.csv')

        plot.bar(China_data['Year'], China_data['Amount of Users Affected in millions'],
                      label='China Cyber Crimes', color='tab:red')
        plot.set_title('China Cyber Crime Data')
        plot.set_xlabel('Year')
        plot.set_ylabel('Number of crimes exposed in millions')
        plot.legend()

        return plot_canvas

    def uk_cybercrime_data(self):
        plot_canvas, plot = self.create_plot_canvas()
        United_Kingdom_data = pd.read_csv('Data/UK_Data.csv')

        plot.bar(United_Kingdom_data['Year'], United_Kingdom_data['Amount of Users Affected in millions'],
                      label='United Kingdom Cyber Crimes', color='tab:Orange')
        plot.set_title('United Kingdom Cyber Crimes Data from 2013-2023')
        plot.set_xlabel('Year')
        plot.set_ylabel('Number of crimes exposed in millions')
        plot.legend()

        return plot_canvas

