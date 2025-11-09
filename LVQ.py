import math

class LVQ:
    def winner(self, weights, sample):
        distances = [
            sum(math.pow(sample[i] - weight[i], 2) for i in range(len(sample)))
            for weight in weights
        ]
        return distances.index(min(distances))

    def update(self, weights, sample, J, alpha, actual):
        if actual == J:
            for i in range(len(weights[J])):
                weights[J][i] += alpha * (sample[i] - weights[J][i])
        else:
            for i in range(len(weights[J])):
                weights[J][i] -= alpha * (sample[i] - weights[J][i])


def main():
    X = [
        [0, 0, 1, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
    ]
    Y = [0, 1, 0, 1, 1, 1]

    m, n = len(X), len(X[0])

    weights = []
    weights.append(X.pop(0))
    weights.append(X.pop(0))

    m -= 2
    Y.pop(0)
    Y.pop(0)

    ob = LVQ()
    epochs = 3
    alpha = 0.1

    for _ in range(epochs):
        for j in range(m):
            T = X[j]
            J = ob.winner(weights, T)
            ob.update(weights, T, J, alpha, Y[j])

    T = [0, 0, 1, 0]
    J = ob.winner(weights, T)
    print("Sample T belongs to class:", J)
    print("Trained weights:", weights)


if __name__ == "__main__":
    main()
