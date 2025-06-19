import pandas as pd
import matplotlib.pyplot as plt
import os


def load_csv_file(filename):
    """Load survey data from a CSV file into a DataFrame."""
    return pd.read_csv(filename)


def calculate_average_by_column(data, group_col, value_col):
    """Calculate the average of value_col grouped by group_col."""
    return data.groupby(group_col)[value_col].mean()


def count_responses(data, column_name):
    """Count how many times each unique value appears in a column."""
    return data[column_name].value_counts()


def generate_bar_chart(data, title, xlabel, ylabel):
    """Generate a bar chart from a Series."""
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()


def main():
    filename = input("Enter the survey CSV filename (or press Enter to use 'survey_data.csv'): ").strip()
    if filename == "":
        filename = "survey_data.csv"

    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        return

    data = load_csv_file(filename)

    print("\nAverage age by city:")
    avg_age = calculate_average_by_column(data, 'City', 'Age')
    print(avg_age)

    print("\nResponse count for 'Satisfaction':")
    counts = count_responses(data, 'Satisfaction')
    print(counts)

    generate_bar_chart(counts, 'Satisfaction Ratings', 'Rating', 'Count')


if __name__ == "__main__":
    main()
