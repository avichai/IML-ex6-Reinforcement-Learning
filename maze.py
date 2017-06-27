import numpy as np
from matplotlib import pyplot as plt
from valueIteration import valueIteration


def getTau():
    tau = np.array(
        [[[1, 0, 0, 0, 0, 0, 0, 0, 0], [0.2, 0.8, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]],

         [[0.8, 0.2, 0, 0, 0, 0, 0, 0, 0], [0, 0.2, 0.8, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0.2, 0, 0, 0.8, 0, 0, 0, 0]],

         [[0, 0.8, 0.2, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0.2, 0, 0, 0.8, 0, 0, 0]],

         [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]],

         [[0, 0, 0, 0.8, 0.2, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0.8, 0, 0, 0.2, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]],

         [[0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0.8, 0, 0, 0.2, 0, 0, 0], [0, 0, 0, 0, 0, 0.2, 0, 0, 0.8]],

         [[0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0.2, 0.8, 0],
          [0, 0, 0, 0, 0.8, 0, 0.2, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]],

         [[0, 0, 0, 0, 0, 0, 0.8, 0.2, 0], [0, 0, 0, 0, 0, 0, 0, 0.2, 0.8],
          [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]],

         [[0, 0, 0, 0, 0, 0, 0, 0.8, 0.2], [0, 0, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0.8, 0, 0, 0.2], [0, 0, 0, 0, 0, 0, 0, 0, 1]]])

    return tau


def getRho():
    rho = np.array(
        [[-6, -2.2, -6, -6], [-2.2, -2.2, -6, -2.2], [-2.2, -6, -6, -2.2],
         [0, 0, 0, 0], [-2.2, -6, -2.2, -6], [-6, -6, -2.2, -2.2],
         [-6, -2.2, -2.2, -6], [-2.2, -2.2, -6, -6], [-2.2, -6, -2.2, -6]])
    return rho


def main():
    sizeS = 9
    sizeA = 4
    tau = getTau()
    rho = getRho()
    gamma = 0.75
    V, Q = valueIteration(sizeS, sizeA, tau, rho, gamma)
    V1, Q1 = valueIteration(sizeS, sizeA, tau, rho, gamma, 1)
    V2, Q2 = valueIteration(sizeS, sizeA, tau, rho, gamma, 2)
    V3, Q3 = valueIteration(sizeS, sizeA, tau, rho, gamma, 3)
    V4, Q4 = valueIteration(sizeS, sizeA, tau, rho, gamma, 4)

    # print(V)
    # print(V.reshape((3,3)))

    plt.figure()
    plt.subplot(3, 2, 6)
    plt.imshow(V.reshape((3, 3)), cmap='hot')

    plt.subplot(3, 2, 1)
    plt.imshow(V1.reshape((3, 3)), cmap='hot')

    plt.subplot(3, 2, 2)
    plt.imshow(V2.reshape((3, 3)), cmap='hot')

    plt.subplot(3, 2, 3)
    plt.imshow(V3.reshape((3, 3)), cmap='hot')

    plt.subplot(3, 2, 4)
    plt.imshow(V4.reshape((3, 3)), cmap='hot')

    plt.show()


if __name__ == "__main__":
    main()
