import pandas as pd
from survey_analyzer import calculate_average_by_column, count_responses


def test_calculate_average_by_column():
    df = pd.DataFrame({
        'City': ['A', 'A', 'B', 'B'],
        'Age': [20, 30, 40, 60]
    })
    result = calculate_average_by_column(df, 'City', 'Age')
    assert result['A'] == 25
    assert result['B'] == 50


def test_count_responses():
    df = pd.DataFrame({
        'Satisfaction': ['Good', 'Bad', 'Good', 'Excellent', 'Good']
    })
    result = count_responses(df, 'Satisfaction')
    assert result['Good'] == 3
    assert result['Bad'] == 1
    assert result['Excellent'] == 1
