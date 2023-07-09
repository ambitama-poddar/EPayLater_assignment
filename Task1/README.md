Sure! Here's a README file for the provided codes:

```markdown
# Housing Price Regression Model

This project consists of two Python scripts that build regression models to predict housing prices based on given features. The first script uses simple linear regression, while the second script employs multiple linear regression.

## Instructions

### Dataset

The dataset is provided in a CSV file called "housing_data.csv" in the code repository. It contains the following columns:

- Bedrooms: Number of bedrooms in the house
- Bathrooms: Number of bathrooms in the house
- SquareFootage: Total square footage of the house
- Location: Categorical variable representing the neighborhood of the house
- SalePrice: Sale price of the house in dollars

### Simple Linear Regression

1. Load and read the dataset from the CSV file.
2. Split the data into training and testing sets. The first 50 rows are used for training, and the remaining rows are used for testing.
3. Implement simple linear regression to predict the sale price based on the square footage feature.
4. Train the model using the training data.
5. Evaluate the performance of the model using the R-squared value.
6. Make predictions on the testing data and calculate the root mean squared error (RMSE) between the predicted prices and the actual prices.
7. Visualize the actual prices and predicted prices on a scatter plot.

### Multiple Linear Regression

1. Load and read the dataset from the CSV file.
2. Split the data into training and testing sets. The first 50 rows are used for training, and the remaining rows are used for testing.
3. Perform one-hot encoding on the categorical location feature.
4. Build a multiple linear regression model using all available features.
5. Train the model using the training data.
6. Evaluate the performance of the model using the R-squared value.
7. Make predictions on the testing data and calculate the root mean squared error (RMSE) between the predicted prices and the actual prices.
8. Visualize the predicted prices against the actual prices using a scatter plot.

## Dependencies

Both scripts require the following dependencies:

- matplotlib
- pandas
- joblib
- scikit-learn
- seaborn

You can install the dependencies using pip:
```bash
pip install matplotlib pandas joblib scikit-learn seaborn
```

## License

This project is licensed under the [MIT License](LICENSE).

```

Replace `[repository-url]` with the actual URL of your repository if you have it hosted online.

Make sure to update the README file with relevant information specific to your project.

Let me know if you need any further assistance!
