This is the solution for the [Forest Cover Type Prediction](https://www.kaggle.com/competitions/forest-cover-type-prediction/) competition formated as a **Python package**. It uses [Forest train](https://www.kaggle.com/competitions/forest-cover-type-prediction/data?select=train.csv) dataset.

## Usage
This package allows you to train model for predicting the forest cover type (the predominant kind of tree cover) from strictly cartographic variables.
1. Clone this repository to your machine:
```
git clone https://github.com/MeSugar/forest_competition.git
```
2. Download [Forest train](https://www.kaggle.com/competitions/forest-cover-type-prediction/data?select=train.csv) dataset, save csv locally (default path is *data/train.csv* in repository's root).
3. Make sure Python 3.9 and [Poetry](https://python-poetry.org/docs/) are installed on your machine (I used Poetry 1.1.13).
4. Install the project dependencies (run this and following commands in a terminal, from the root of a cloned repository):
```
poetry install --no-dev
```
5. Run train with the following command:
```
poetry run train -d <path to csv with data> -s <path to save trained model>
```
You can configure additional options (e.g., the algorithm to be chosen for the task) in the CLI. To get a full list of them, use help:
```
poetry run train --help
```
6. To see the information about conducted experiments (algorithm, metrics, hyperparameters) run [MLflow UI](https://mlflow.org/docs/latest/index.html):
```
poetry run mlflow ui
```
![image](https://user-images.githubusercontent.com/75207011/168317447-aba16bc1-32fb-4081-8b05-cfe2c65c9827.png)

7. You can produce EDA report in .html format using [Pandas-Profiling](https://github.com/ydataai/pandas-profiling):
```
poetry run eda -d <path to csv with data> -s <path to save report>
```
To see the list of configure options in the CLI run with *--help* option

8. To make submission file with predictions run:
```
poetry run predict
```
To see the list of configure options in the CLI run:
```
poetry run predict --help
```




