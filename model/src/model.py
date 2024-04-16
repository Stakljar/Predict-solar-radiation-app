from pandas import read_csv
from pandas import concat
from numpy import concatenate
from pickle import dump
from data_modification import formatTime
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor, HistGradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
from column_names import unix_time, data_, radiation
from os import path

dataset_path = path.join("..", "resources", "SolarPrediction.csv")
scaler_path = path.join("..", "resources", "scaler.pkl")
model_path = path.join("..", "resources", "solar_radiation_prediction_model.pkl")

def prepareDataForTraining():
    data = read_csv(dataset_path)
    data.drop([unix_time, data_], inplace=True, axis=1)
    data = formatTime(data)

    X = data.drop(radiation, axis=1)
    y = data[radiation]

    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, shuffle=True)

    scaler = StandardScaler()
    global X_train_normalized
    X_train_normalized = scaler.fit_transform(X_train)
    global X_test_normalized 
    X_test_normalized = scaler.transform(X_test)
    dump(scaler, file=open(scaler_path, "wb"))

def trainAndSaveModel():
    prepareDataForTraining()
    et = ExtraTreesRegressor(n_estimators=30, max_depth=180, min_samples_split=10)
    dump(et.fit(concatenate((X_train_normalized, X_test_normalized), axis=0), concat([y_train, y_test], ignore_index=True)), file=open(model_path, "wb"))

def printStatistics(algorithmName, y_pred, y_test):
    mae = mean_absolute_error(y_pred, y_test)
    mse = mean_squared_error(y_pred, y_test)
    rmse = root_mean_squared_error(y_pred, y_test)
    r2 = r2_score(y_pred, y_test)
    print(f"{algorithmName}:")
    print(f"Mean Absolute Error: {mae}\nMean Squared Error: {mse}\nRoot Mean Squared Error: {rmse}\nCoefficient of Determination: {r2}\n")

def trainAndTestModels():
    rf = RandomForestRegressor(n_estimators=64, max_depth=100, min_samples_split=10)
    printStatistics(algorithmName="Random Forest Regressor", 
        y_pred=rf.fit(X_train_normalized, y_train).predict(X_test_normalized), y_test=y_test)

    et = ExtraTreesRegressor(n_estimators=30, max_depth=180, min_samples_split=10)
    printStatistics(algorithmName="Extra Trees Regressor",
        y_pred=et.fit(X_train_normalized, y_train).predict(X_test_normalized), y_test=y_test)

    gb = GradientBoostingRegressor(n_estimators=160, max_depth=10, min_samples_split=2)
    printStatistics(algorithmName="Gradient Boosting Regressor",
        y_pred=gb.fit(X_train_normalized, y_train).predict(X_test_normalized), y_test=y_test)

    hgb = HistGradientBoostingRegressor(max_iter=4000, max_leaf_nodes=100, min_samples_leaf=5)
    printStatistics(algorithmName="Hist Gradient Boosting Regressor",
        y_pred=hgb.fit(X_train_normalized, y_train).predict(X_test_normalized), y_test=y_test)

    mlp = MLPRegressor(hidden_layer_sizes=(100, 100, 100), max_iter=500)
    printStatistics(algorithmName="Multi-layer Perceptron Regressor",
        y_pred=mlp.fit(X_train_normalized, y_train).predict(X_test_normalized), y_test=y_test)

if(__name__ == "__main__"):
    prepareDataForTraining()
    print("Results of training:\n")
    trainAndTestModels()
