import data_preparation, linear_regression

data_preparation_object = data_preparation.DataPreparation(csv_path="number_of_travelers.csv", ratio=(0.7, 0.15))
# data_preparation_object.show_dataset()

linear_regression_object = linear_regression.LinearRegression(data_prepartion_object=data_preparation_object)
linear_regression_object.training_gradient_descent(number_epochs=80000, learning_rate=0.00015, batch_size=84)
linear_regression_object.show_linear_regression()

