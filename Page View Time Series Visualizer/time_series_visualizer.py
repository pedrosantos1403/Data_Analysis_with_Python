import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv")

# Transforming 'date' column values in datetime type
df['date'] = pd.to_datetime(df['date'])

# Make sure to parse dates. Consider setting index column to 'date'
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) &
        (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    
    # Definindo figure e axis
    fig, ax = plt.subplots(figsize=(20, 6))

    # Definindo o título do plot
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Definindo as labels
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Plotando o line chart
    plt.plot(df.index, df['value'], color='r', label='date')

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    # Criar colunas 'year' e 'month'
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month

    # Agrupar value por ano e por meses
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()

    # Definindo figure e axis
    fig, ax = plt.subplots(figsize=(8, 8))

    # Draw bar plot
    sns.barplot(x='year', y='value', hue='month', data=df_bar,
                palette=sns.color_palette(), width=0.5)
    
    # Definindo o desenho e a cor de cada mes na legenda
    handles = [plt.Rectangle((0, 0), 1, 1, color=sns.color_palette(n_colors=12)[i])
               for i in range(12)]
    
    # Criando array com o nome dos meses para a legenda
    legend_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                     'August', 'September', 'October', 'November', 'December']
    
    # Definindo a legenda
    plt.legend(handles, legend_months, title="Months", loc='upper left')

    # Definindo os labels
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.month for d in df_box.date]
    df_box.sort_values(by='month', inplace=True)
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Definindo figure e axis
    fig, ax= plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

    # Year wise box plot
    sns.boxplot(x='year', y='value', data=df_box, palette=sns.color_palette(), ax=ax[0],)

    # Definindo labels e title do primeiro plot
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    # Month wise box plot
    sns.boxplot(x='month', y='value', data=df_box, palette=sns.color_palette("Set2"), ax=ax[1])

    # Definindo labels e title do segundo plot
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    plt.savefig('box_plot.png')
    return fig
