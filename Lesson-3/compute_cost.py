import numpy as np
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and values for our thetas.
    """
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write some code here that updates the values of theta a number of times equal to
    # num_iterations.  Everytime you have computed the cost for a given set of thetas,
    # you should append it to cost_history.  The function should return both the final
    # values of theta and the cost history.

    # YOUR CODE GOES HERE
    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        theta += alpha/m*np.dot(values-np.dot(features,theta),features)
        cost = compute_cost(features,values,theta)
        cost_history.append(cost)

    return theta, pandas.Series(cost_history)
