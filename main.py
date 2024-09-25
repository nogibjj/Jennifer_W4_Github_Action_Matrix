import polars as pl
import matplotlib.pyplot as plt

# Load job applicant csv file into dataframe
job_applicants_df = pl.read_csv("Job_Applicants_by_Gender_and_Ethnicity.csv")
pl.Config.set_tbl_cols(100)


# Generate a summary of statistics
def stats_overview(df):
    summary_stats = df.select(
        [
            "Apps Received",
            "Black",
            "Hispanic",
            "Asian",
            "Caucasian",
            "American Indian/ Alaskan Native",
            "Filipino",
            "Unknown_Ethnicity",
        ]
    ).describe()
    print(summary_stats)
    return summary_stats


# Generate a table showing the total number of applicants by ethnicity
def total_and_eth_value(df):
    total_and_eth = df.select(
        [
            pl.sum("Apps Received").alias("Apps Received"),
            pl.sum("Black").alias("Black"),
            pl.sum("Hispanic").alias("Hispanic"),
            pl.sum("Asian").alias("Asian"),
            pl.sum("Caucasian").alias("Caucasian"),
            pl.sum("American Indian/ Alaskan Native").alias(
                "American Indian/ Alaskan Native"
            ),
            pl.sum("Filipino").alias("Filipino"),
            pl.sum("Unknown_Ethnicity").alias("Unknown_Ethnicity"),
        ]
    )

    # Add a row name for the total row
    total_and_eth = total_and_eth.with_columns(pl.lit("total").alias("statistic"))
    total_by_value = total_and_eth.select(
        ["statistic"] + [col for col in total_and_eth.columns if col != "statistic"]
    )
    print(total_by_value)
    return total_by_value


# calculate total number of applicants by ethinicity, for plotting
def ethnicity_total(df):
    eth_total = df[
        [
            "Black",
            "Hispanic",
            "Asian",
            "Caucasian",
            "American Indian/ Alaskan Native",
            "Filipino",
            "Unknown_Ethnicity",
        ]
    ].sum()
    return eth_total


# visualize the total number of applicants by ethnicity
def eth_chart(df):
    eth_and_total = ethnicity_total(df)
    eth_and_total = eth_and_total.to_pandas()
    eth_and_total.plot(kind="bar", stacked=False, title="Number of Applicants")
    plt.xlabel("Ethnicity")
    plt.ylabel("Number of Applicants")
    plt.show()
    return eth_chart


if __name__ == "__main__":
    stats_overview(job_applicants_df)
    total_and_eth_value(job_applicants_df)
    ethnicity_total(job_applicants_df)
    eth_chart(job_applicants_df)
