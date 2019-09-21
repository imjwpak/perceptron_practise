import numpy as np

class Perceptron:
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self._eta = eta
        self._n_iter = n_iter
        self._random_state = random_state

    def fit(self, X, y):
        regen = np.random.RandomState(self._random_state)
        self.w_ = regen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []

        for _ in range(self._n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self._eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[1:] += update
                errors += int(update != 0.0)

            self.errors_.append(errors)

        return self

    def net_input(self, X):
        """ 최종 입력 계산 """
        return np.dot(X, self.w_[1:] + self.w_[0])

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)