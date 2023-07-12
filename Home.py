import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


df = pd.read_csv('./assets/practice_dataset.csv')

# Visualizations

def pie_chart():
    plt.figure(figsize=(8, 8))
    labels = ['Engineering', 'Party', 'Liberal Arts', 'Ivy League', 'State']
    counts = df['type'].value_counts().tolist()
    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title('Distribution of School Types')
    st.pyplot()

def box_plot():
    plt.figure(figsize=(10, 8))
    plt.boxplot([df['mid_p50']])
    plt.xticks([1],
               ['50th Percentile'],
               rotation=45)
    plt.ylabel('Salary')
    plt.title('Distribution of Mid-Career Salaries')
    st.pyplot()

def violin_plot():
    plt.figure(figsize=(8, 6))
    plt.violinplot([df[df['type'] == 'Engineering']['mid_p50'],
                    df[df['type'] == 'Party']['mid_p50'],
                    df[df['type'] == 'Liberal Arts']['mid_p50'],
                    df[df['type'] == 'Ivy League']['mid_p50'],
                    df[df['type'] == 'State']['mid_p50']],
                   showmedians=True)
    plt.xticks([1, 2, 3, 4, 5], ['Engineering', 'Party', 'Liberal Arts', 'Ivy League', 'State'])
    plt.xlabel('School Type')
    plt.ylabel('Mid-Career Median Salary')
    plt.title('Distribution of Mid-Career Salaries for School Types')
    st.pyplot()


def area_chart():
    plt.figure(figsize=(10, 6))
    plt.stackplot(df['name'][:20], df["mid_p50"][:20], df["mid_p10"][:20], df["mid_p25"][:20], df["mid_p75"][:20], df["mid_p90"][:20], labels=['10th Percentile', '25th Percentile', 'Median', '75th Percentile', '90th Percentile'])
    plt.xticks(rotation=90)
    plt.xlabel('University')
    plt.ylabel('Salary')
    plt.title('Comparison of Mid-Career Salaries for Universities')
    plt.legend(loc='upper left')
    st.pyplot()




# Pages
def piechart():
    st.title("Pies Page")
    st.write("Here is a sample visualization:")
    pie_chart()

def boxplots():
    st.title("Boxs Page")
    st.write("Here is a sample visualization:")
    box_plot()
    
def areachart():
    st.title("Areas Page")
    st.write("Here is a sample visualization:")
    area_chart()

def violinplot():
    st.title("Violin Page")
    st.write("Here is a sample visualization:")
    violin_plot()



# Create a dictionary of the pages
pages = {
    "Pie Chart": piechart,
    "Box Chart": boxplots,
    "Violin Plot": violinplot,
    "Area Chart": areachart,
}

# Streamlit App
def main():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.selectbox("Select a visualization", tuple(pages.keys()))

    # Display the selected page
    pages[selected_page]()

if __name__ == "__main__":
    main()