# About
This is a notebook consisting of the analysis and model construction for the [Kaggle Spaceshipe Titanic competition](https://www.kaggle.com/competitions/spaceship-titanic).

## Required Packages and Environment
An `environment.yml` file is included for redroducability. To install and activate the encrionment, run
```conda
conda env create -f envioronment.yml
conda activate spaceship-titanic
```

## Download Data
To download the dataset, first [download an apikey from your Kaggle profile](https://www.kaggle.com/docs/api#authentication) to your home directory. Then from the command line run
```bash
python load_data.py
```
Alternatively, you may download the dataset from the [competition datasource](https://www.kaggle.com/competitions/spaceship-titanic/data).