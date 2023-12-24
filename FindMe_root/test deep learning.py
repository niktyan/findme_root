import sys, numpy as np
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

images, labels = (x_train[0:1000].reshape(1000, 28*28) / 255, y_train[0:1000])
one_hot_labels = np.zeros((len(labels), 10))

for i, l in enumerate(labels):
    one_hot_labels[i][l] = 1
labels = one_hot_labels

test_images = x_test.reshape(len(x_test), 28*28) / 255
test_labels = np.zeros((len(y_test), 10))
for i, l in enumerate(y_test):
    test_labels[i][l] = 1

np.random.seed(1)
relu = lambda x: (x >= 0) * x
relu2deriv = lambda x: x >= 0
alpha = 0.005
iterations = 350
hidden_size = 40
pixels_per_image = 784
num_labels = 10

weight_input_hidden = np.random.random((pixels_per_image, hidden_size))
weight_hidden_pred = np.random.random((hidden_size, num_labels))

for j in range(iterations):
    error, correct_cnt = (0.0, 0)
    for i in range(len(images)):
        input = images[i:i+1]
        dropout_mask = np.random.randint(2, size=hidden.shape)
        hidden = relu(np.dot(input, weight_input_hidden))
        hidden = hidden * dropout_mask * 2
        pred = np.dot(hidden, weight_hidden_pred)
        error += np.sum((labels[i:i+1] - pred) ** 2)
        correct_cnt += int(np.argmax(pred) == np.argmax(labels[i:i+1]))

        delta_pred = (labels[i:i+1] - pred)
        delta_hidden = relu2deriv(hidden) * delta_pred.dot(weight_hidden_pred.T)

        delta_hidden *= dropout_mask

        weight_hidden_pred += alpha * hidden.T.dot(delta_pred)
        weight_input_hidden += alpha * input.T.dot(delta_hidden)

    sys.stdout.write("\r" + "I:" + str(j) + "Error: " + str(error/float(len(images)))[0:5] + "Correct: " + str(correct_cnt/float(len(images))))
