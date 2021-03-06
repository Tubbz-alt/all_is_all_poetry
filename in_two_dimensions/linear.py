# import matplotlib.pyplot as plt
import numpy as np


def sample_between(a, b, n):
    g = np.random.normal

    # Vector pointing towards b
    c = (b - a)

    # Distance between them
    d = np.linalg.norm(c)

    # Halfway between a and b
    h = (c / 2) + a
    points = []
    for i in range(n):
        points.append(h + g(0, scale = d / 100) * c / 2)

    # return np.linspace(0, 1, n) * c / 2 + h

    return np.array(points)


# def test_sample_between():
#
#     a = np.array([0, 0])
#     b = np.array([10, 10])
#
#     points = sample_between(a, b, 10)
#
#     plt.scatter(points[:, 0], points[:, 1])
#     plt.show()
#
# test_sample_between()