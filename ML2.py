from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris_dataset = load_iris()
#(150,4)
#75% 25% automatically
#test_size = 0.2 --> 80% 20%
x_train, x_test , y_train, y_test = train_test_split(iris_dataset["data"],iris_dataset["target"],test_size=0.2,random_state=0)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#150
#75% = 112
#25% = 38