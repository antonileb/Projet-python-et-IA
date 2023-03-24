import random
import tqdm
import matplotlib.pyplot as plt
from more_itertools import chunked
import numpy

class LinearRegression:
	def __init__(self, data_prepartion_object):
		self.data_prepartion_object = data_prepartion_object


	def training_gradient_descent(self, number_epochs, learning_rate, batch_size):
		# on initialise les poids de notre modèle de manière aléatoire
		self.a = 0
		self.b = 0 # ça a du sens parce que les valeurs à prédire sont entre 0 et 1 (lié à la normalisation)

		train_length = len(self.data_prepartion_object.t_train)
		validation_length = len(self.data_prepartion_object.t_validation)


		linear_regression_forecast = lambda index_time : self.a * index_time + self.b  # a*t + b
		
		loss_function_mse_train = lambda predictions: sum([(predictions[index_time] - self.data_prepartion_object.y_train[index_time])**2 for index_time in range(0, train_length)]) / (2*train_length)
		loss_function_mse_validation = lambda predictions: sum([(predictions[index_time] - self.data_prepartion_object.y_validation[index_time])**2 for index_time in range(0, validation_length)]) / (2*validation_length)

		list_epochs = []
		list_mse_loss_values_for_train_per_epoch = []
		list_mse_loss_values_for_validation_per_epoch = []



		t_train_batches = numpy.array(list(chunked(self.data_prepartion_object.t_train, batch_size)))
		y_train_batches = numpy.array(list(chunked(self.data_prepartion_object.y_train, batch_size)))

		# print(numpy.concatenate(y_train_batches) == self.data_prepartion_object.y_train)

		number_of_batches = len(t_train_batches)

		for epoch in range(0, number_epochs):

			for index_batch in range(0, number_of_batches):
				number_of_element_current_batch = len(t_train_batches[index_batch])

				current_batch_train_predictions = list(map(linear_regression_forecast, t_train_batches[index_batch]))

				dloss_da = sum([index_time * (current_batch_train_predictions[index_time] - y_train_batches[index_batch][index_time]) for index_time in range(0, number_of_element_current_batch)]) / number_of_element_current_batch
				dloss_db = sum([current_batch_train_predictions[index_time] - y_train_batches[index_batch][index_time] for index_time in range(0, number_of_element_current_batch)]) / number_of_element_current_batch

				self.a -= learning_rate * dloss_da
				self.b -= learning_rate * dloss_db



			train_predictions_current_epoch = list(map(linear_regression_forecast, self.data_prepartion_object.t_train))
			validation_predictions_current_epoch = list(map(linear_regression_forecast, self.data_prepartion_object.t_validation))

			loss_train_current_epoch  = loss_function_mse_train(train_predictions_current_epoch)
			loss_validation_current_epoch = loss_function_mse_validation(validation_predictions_current_epoch)

			list_epochs.append(epoch)
			list_mse_loss_values_for_train_per_epoch.append(loss_train_current_epoch)
			list_mse_loss_values_for_validation_per_epoch.append(loss_validation_current_epoch)

			if epoch % 1000 ==0:
				print(f"epoch : {epoch}")
				print(loss_train_current_epoch, loss_validation_current_epoch)
				print(f"a : {self.a}, b : {self.b}")
				print("#"*20)

		# print(f"la valeur de ma mse est : {loss_function_mse_train(train_predictions_current_epoch)}")
		plt.figure(figsize=(15, 6))
		plt.plot(list_epochs[100:], list_mse_loss_values_for_train_per_epoch[100:], "b")
		plt.plot(list_epochs[100:], list_mse_loss_values_for_validation_per_epoch[100:], "r")
		plt.show()
		return None


	def show_linear_regression(self):
		if not hasattr(self, "a") or not hasattr(self, "b"):
			print("Error : you must first train your model !!")

		else:
			linear_regression_forecast = lambda index_time : self.a * index_time + self.b  # a*t + b

			train_predictions = list(map(linear_regression_forecast, self.data_prepartion_object.t_train))
			validation_predictions = list(map(linear_regression_forecast, self.data_prepartion_object.t_validation))
			test_predictions = list(map(linear_regression_forecast, self.data_prepartion_object.t_test))


			plt.figure(figsize=(15, 6))
			# train base
			plt.plot(self.data_prepartion_object.t_train, self.data_prepartion_object.y_train, "o", color="cyan")
			plt.plot(self.data_prepartion_object.t_train, train_predictions, "o", color="blue")

			# train validation
			plt.plot(self.data_prepartion_object.t_validation, self.data_prepartion_object.y_validation, "o", color="cyan")
			plt.plot(self.data_prepartion_object.t_validation, validation_predictions, "o", color="blue")
			#test base

			plt.plot(self.data_prepartion_object.t_test, self.data_prepartion_object.y_test, "o", color="orange")
			plt.plot(self.data_prepartion_object.t_test, test_predictions, "o", color="red")

			plt.show()

			return None