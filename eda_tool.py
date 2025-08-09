import argparse
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(path)


def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for all columns."""
    return df.describe(include='all')


def plot_histograms(df: pd.DataFrame, output_dir: str) -> None:
    """Save histogram plots for numeric columns."""
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f'Histogram of {col}')
        plt.savefig(os.path.join(output_dir, f'hist_{col}.png'))
        plt.close()


def plot_correlation_matrix(df: pd.DataFrame, output_dir: str) -> None:
    """Save a heatmap of the correlation matrix for numeric columns."""
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.savefig(os.path.join(output_dir, "corr_matrix.png"))
    plt.close()


def pair_plot(df: pd.DataFrame, output_dir: str) -> None:
    """Save a pair plot for numeric columns if there is more than one."""
    numeric_df = df.select_dtypes(include='number')
    if numeric_df.shape[1] > 1:
        sns.pairplot(numeric_df)
        plt.savefig(os.path.join(output_dir, "pair_plot.png"))
        plt.close()


def generate_report(data_path: str, output_dir: str) -> None:
    """Generate summary statistics and plots for the dataset."""
    df = load_data(data_path)
    os.makedirs(output_dir, exist_ok=True)
    summary_statistics(df).to_csv(os.path.join(output_dir, "summary.csv"))
    plot_histograms(df, output_dir)
    plot_correlation_matrix(df, output_dir)
    pair_plot(df, output_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple EDA tool")
    parser.add_argument("input", help="Path to the CSV data file")
    parser.add_argument(
        "-o",
        "--output",
        default="eda_output",
        help="Directory where results will be saved",
    )
    args = parser.parse_args()
    generate_report(args.input, args.output)


if __name__ == "__main__":
    main()
