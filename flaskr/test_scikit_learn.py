from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor

# X = [[100, 0, 102, 1], [100, 0, 103, 1], [100, 0, 104, 1], [100, 0, 105, 1], [100, 0, 100, 1], [100, 0, 110, 1], [100, 0, 111, 1], [100, 0, 120, 1], [100, 0, 115, 1], [100, 0, 118, 1]]
# y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

XX = [[100, 0, 107, 1], [100, 0, 103, 1], [100, 0, 104, 1], [100, 0, 105, 1], [100, 0, 106, 1], [100, 0, 102, 1], [100, 0, 110, 1], [100, 0, 111, 1], [100, 0, 112, 1], [100, 0, 113, 1], [100, 0, 114, 1]]
yy = [100, 100, 100, 100, 100, 100, 110, 111, 112, 113, 114]

clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
clf.fit(XX, yy)


print("Predict[108,1]", str(clf.predict([[100, 0, 106, 1]])))

