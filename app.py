import streamlit as st
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import emoji
from collections import Counter
import warnings

warnings.filterwarnings('ignore')

# Magic command for inline plotting
# %matplotlib inline

# Function to convert raw data to DataFrame
def raw_to_df(file, key):
    # Function implementation here

# Load data
df = raw_to_df('edited_chats.txt', '12hr')

# Title
st.title('WhatsApp Group Chat Analysis')

# Sidebar options
analysis_option = st.sidebar.selectbox('Select Analysis', ('Overall Frequency', 'Top 10 Active Days', 'Top 10 Active Users', 'Average Message Length', 'Top 10 Most Sent Media', 'Top 10 Most Used Emoji', 'Most Active Day, Hour, and Month', 'Word Cloud'))

# Main content based on selection
if analysis_option == 'Overall Frequency':
    # Overall frequency of the group
    st.subheader('Overall Frequency of the Group')
    # Plotting messages sent per day over a time period
    # Replace plt.plot() with Streamlit's native plotting function
    st.pyplot(plot_overall_frequency(df))

# Define functions for plotting and analysis
def plot_overall_frequency(df):
    df1 = df.copy()
    df1['message_count'] = 1

    if 'year' in df1.columns:
        df1.drop(columns='year', inplace=True)

    df1 = df1.groupby('date')['message_count'].sum().reset_index()

    # Plotting messages sent per day over a time period
    plt.plot(df1['date'], df1['message_count'])
    plt.title('Messages sent per day over a time period')
    plt.xlabel('Date')
    plt.ylabel('Message Count')
    return plt.gcf()
