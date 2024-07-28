# Predict-solar-radiation-app
Web application that enables you to predict solar radiation based on parameters that you input.
Made using React and Python.
Note that measuring units were taken based on typical values of parameters.

Source of dataset used is https://www.kaggle.com/datasets/dronio/SolarEnergy, this dataset is made available under Open Database License (ODbL) license: https://opendatacommons.org/licenses/odbl/1-0/
and any rights in individual contents of the dataset are licensed under Database Contents License (DbCL): https://opendatacommons.org/licenses/dbcl/1-0/.

## How to run
Clone the repository:
```cmd
git clone https://github.com/Stakljar/Predict-solar-radiation-app.git
```
Download dataset from https://www.kaggle.com/datasets/dronio/SolarEnergy and put it inside _model/resources_ directory.
Navigate to the _model/src_ directory and execute following command:
```cmd
py api.py
```
Navigate to the _client_ directory and execute following commands:
```cmd
npm install -f
npm start
```
