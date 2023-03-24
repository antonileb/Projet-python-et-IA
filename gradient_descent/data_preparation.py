import pandas
import matplotlib.pyplot as plt
import seaborn
import numpy

class DataPreparation:

	"""Cette classe me permet de gérer le jeu de données"""
	def __init__(self, csv_path, ratio):

		self.number_of_travelers_df = pandas.read_csv(csv_path, sep=",")
		self.dataset_length = len(self.number_of_travelers_df)

		self.ratio = ratio
		self.prepare_data()


	def prepare_data(self):
		# normalise mon jeu données tout en sauvegardant le coefficient de normalisation
		self.coefficient_normalisation = self.number_of_travelers_df["passengers"].values.max()
		self.number_of_travelers_df["passengers"] /= self.coefficient_normalisation

		# j'encode ma date sous forme d'entier
		self.number_of_travelers_df["index_time"] = numpy.array([index_date for index_date in range(0, self.dataset_length)])
		
		# J'effectue le split train / validation  /test
		index_split_1 = int(self.dataset_length * self.ratio[0])
		index_split_2 = int(self.dataset_length * (self.ratio[0]+ self.ratio[1]))



		train_dataset_df = self.number_of_travelers_df.loc[ : index_split_1-1]
		validation_dataset_df = self.number_of_travelers_df.loc[index_split_1 : index_split_2-1]
		test_dataset_df = self.number_of_travelers_df.loc[index_split_2 : ]


		self.t_train = train_dataset_df["index_time"].values
		self.t_validation = validation_dataset_df["index_time"].values
		self.t_test = test_dataset_df["index_time"].values


		self.y_train = train_dataset_df["passengers"].values
		self.y_validation = validation_dataset_df["passengers"].values
		self.y_test = test_dataset_df["passengers"].values

		return None


	def show_dataset(self):
		"""
		Etape 0
		Permet d'afficher le contenu de mon fichier csv sous la forme d'un graphique
		"""
		plt.figure(figsize=(15, 6))
		seaborn.scatterplot(x="index_time", y= "passengers", data=self.number_of_travelers_df)
		plt.show()


		return None
