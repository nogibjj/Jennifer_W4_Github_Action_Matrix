from main import stats_overview, total_and_eth_value
import polars as pl
import polars.testing as plt

# Create a sample DataFrame
Data = {
    "Apps Received": [10, 20, 30, 40, 50],
    "Black": [1, 2, 3, 4, 5],
    "Hispanic": [2, 4, 6, 8, 10],
    "Asian": [3, 6, 9, 12, 15],
    "Caucasian": [4, 8, 12, 16, 20],
    "American Indian/ Alaskan Native": [5, 10, 15, 20, 25],
    "Filipino": [6, 12, 18, 24, 30],
    "Unknown_Ethnicity": [7, 14, 21, 28, 35],
}

sample_df = pl.DataFrame(Data)


# Function tests
def test_stats_overview():
    print("The expected statistic summary for sample data is: ")
    expected_output = sample_df.describe()
    print(expected_output)

    print("The actual statistic summary for sample data is: ")
    actual_output = stats_overview(sample_df)
    print(expected_output["Asian"][2])
    assert int(expected_output["Asian"][2]) == int(actual_output["Asian"][2])


def test_total_and_eth_value():
    print("The expected total applicants by gender for sample data is: ")
    expected_output = pl.DataFrame(
        {
            "statistic": ["total"],
            "Apps Received": [150],
            "Black": [15],
            "Hispanic": [30],
            "Asian": [45],
            "Caucasian": [60],
            "American Indian/ Alaskan Native": [75],
            "Filipino": [90],
            "Unknown_Ethnicity": [105],
        }
    )
    print(expected_output)
    print("The actual total applicants by gender for sample data is: ")
    actual_output = total_and_eth_value(sample_df)
    print(expected_output["Asian"][0])
    assert int(expected_output["Asian"][0]) == int(actual_output["Asian"][0])


if __name__ == "__main__":
    test_stats_overview()
    test_total_and_eth_value()
    print("All tests passed!")
