import numpy as np
from matplotlib import pyplot as plt
from valueIteration import valueIteration


def getTau():
    tau = np.array([[[0, 0, 0, 0, 1], [0, 1, 0, 0, 0]],
                    [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0]],
                    [[0, 1, 0, 0, 0], [0, 0, 0, 1, 0]],
                    [[0, 0, 1, 0, 0], [0, 0, 0, 0, 1]],
                    [[0, 0, 0, 1, 0], [0, 0, 0, 1, 0]]])

    return tau


def getRho():
    rho = np.array([[6, 0], [0, 0], [0, 0], [0, 0], [0, 1]])
    return rho


def main():
    sizeS = 5
    sizeA = 2
    tau = getTau()
    rho = getRho()
    gamma = 0.75
    V, Q = valueIteration(sizeS, sizeA, tau, rho, gamma)
    V1, Q1 = valueIteration(sizeS, sizeA, tau, rho, 0.5)
    V2, Q2 = valueIteration(sizeS, sizeA, tau, rho, 0.75)
    V3, Q3 = valueIteration(sizeS, sizeA, tau, rho, 0.85)

    all_gamma = [0.5 + (x / 100.0) for x in range(49)]
    v_s0 = []
    v_send = []
    for gamma in all_gamma:
        V, Q = valueIteration(sizeS, sizeA, tau, rho, gamma)
        v_s0.append(V[4])
        v_send.append(V[0])

    # print(v_s0)

    plt.figure()
    plt.plot(all_gamma, v_s0, 'b', all_gamma, v_send, 'r')
    plt.show()


if __name__ == "__main__":
    main()
