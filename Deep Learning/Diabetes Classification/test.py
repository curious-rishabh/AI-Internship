from numpy import loadtxt
from keras.models import model_from_json

dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
print(dataset)
x = dataset[:,0:8]
y = dataset[:,8]

json_file = open('', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
model.load_weights("DL\Diabetes Classification\model.h5")
print("Loaded model from disk")

predictions = model.predict_classes(x)

for i in range(5,10):
	print('%s => %d (Original Class: %d)' % (x[i].tolist(), predictions[i], y[i]))
