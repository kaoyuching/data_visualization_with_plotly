# Data visualization with Plotly

Demonstrate data visialization with python package `plotly`.

## Dependencies
- python
    * [x] 3.8
- plotly
    * [x] 0.5.4

## Examples
### Features
1. Categorical variable
    Visualize the distribution of categorical data with bar plot. More details are in [categorical_feature_bar_plot.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/categorical_feature_bar_plot.ipynb)
2. Numerical variable: Visualize the distribution of numerical data with histogram. More details are in [numeric_feature_histogram.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/numeric_feature_histogram.ipynb)
3. Two variable comparison: Use scatter plot to represent values for two given variable. More details are in [feature_comparison.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/feature_comparison.ipynb)

### Pair plot
Visualize the relationship between each pair of features. On the diagonal shows the distribution of the feature itself. More details are in [pair_plot.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/pair_plot.ipynb).

### Missing values
1. Missing value by column
    Show the missing and non-missing value of each column(feature). More details are in [missing_value_by_column.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/missing_value_by_column.ipynb)
2. Missing value pattern
    Show the pattern of missing value with heatmap. More details are in [missing_value_pattern.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/missing_value_pattern.ipynb)
3. Missing value correlation
    Show the correlation of missing value. More details are in [missing_value_correlation.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/missing_value_correlation.ipynb)
4. Missing value by row
    There are two ways to visualize row's missing value.
    - Calculate each row's missing ratio, plot a line with filled area to show accumulated remained row counts.
    - Plot histogram to show row missing ratio summary.

    More details are in [missing_value_row_missing_rate_with_threshold.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/missing_value_row_missing_rate_with_threshold.ipynb).

### Outliers
See [outlier_numeric.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/outlier_numeric.ipynb) and [outlier_category.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/outlier_category.ipynb).

### Correlation matrix
The correlation matrix can break down to 3 parts. For two numerical features, use Pearson correlation. For two categorical features, use Cramer's V. To calculate the correlation between numerical and categorical, use correlation ratio (eta correlation). More details are in [correlation_matrix.ipynb](https://github.com/kaoyuching/plotly_example/blob/master/correlation_matrix.ipynb).

### Visualization for model evaluation
1. Feature importance
2. Confusion matrix
3. ROC curve
4. Precision-Recall curve (pr curve)
