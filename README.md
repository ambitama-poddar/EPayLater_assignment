# EPayLater Assignment

```markdown

This repository contains the solutions for two tasks provided in the EPayLater assignment.

```

## Task 1: Housing Price Prediction

### Problem Statement

```markdown

You have been provided with a dataset containing information about housing prices in a particular city. The dataset includes features such as the number of bedrooms, square footage, location, and sale prices of houses. Your task is to build a regression model that can predict the sale price of a house based on the given features.

```

### Dataset

```markdown

The dataset is provided in a CSV file called "housing_data.csv". It contains the following columns:

- Bedrooms: Number of bedrooms in the house
- Bathrooms: Number of bathrooms in the house
- SquareFootage: Total square footage of the house
- Location: Categorical variable representing the neighborhood of the house
- SalePrice: Sale price of the house in dollars

```

### Solution

```markdown

- The code for this task is stored in the "Task1" folder.
- "housing_data.csv" file contains the dataset.
- "Task1.ipynb" is a Jupyter Notebook file that contains the code to load the dataset, perform data preprocessing, build and train regression models (linear regression and multiple linear regression), evaluate model performance, make predictions, calculate RMSE, and save the trained models.
- The trained models are saved in two separate files: "linear_regression_model.joblib" and "multiple_linear_regression_model.joblib".

```

## Task 2: Housing Price API

### Problem Statement

```markdown

You have been provided with the same housing price data as above in JSON format in a file called "housing_data.json". Your task is to build a REST API in Python (preferably Flask) that will take the JSON data as input and store it in a PostgreSQL database. The API should also provide the following outputs when called:

1. Average sale price of the house overall
2. Average sale price of the house per location
3. Maximum sale price
4. Minimum sale price

```

### Solution

```markdown

- The code for this task is stored in the "Task2" folder.
- "housing_data.json" file contains the dataset in JSON format.
- "app1.py" is a Python script that uses Flask and SQLAlchemy to build the REST API. It includes routes for storing the JSON data in the PostgreSQL database and retrieving the required outputs using SQL queries.
- "app2.py" is a Python script that uses Flask and psycopg2 to build the REST API. It includes routes for storing the JSON data in the PostgreSQL database and retrieving the required outputs using SQL queries.
- The database connection details are provided in the code, and you may need to modify them according to your setup.

```

## Repository Structure

```markdown

The repository is structured as follows:

- Task1/
  - housing_data.csv
  - Task1.ipynb
  - linear_regression_model.joblib
  - multiple_linear_regression_model.joblib
  - README.md
- Task2/
  - housing_data.json
  - app1.py
  - app2.py
  - README.md
- README.md

Please refer to the README files in the respective folders for more details about each task.

```

## Dependencies

```markdown

The code requires the following dependencies:

- For Task 1: pandas, matplotlib, scikit-learn, seaborn, joblib
- For Task 2: Flask, SQLAlchemy, psycopg2

You can install the dependencies using pip:

```bash
pip install pandas matplotlib scikit-learn seaborn joblib Flask SQLAlchemy psycopg2
```

## License

This project is licensed under the [MIT License](LICENSE).

```

Replace `[repository-url]` with the actual URL of your repository if you have it hosted online.

Make sure to update the README file with relevant information specific to your project.

Let me know if you need any further assistance!
