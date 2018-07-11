import numpy as np

from data_set import data_line_computational, data_line_verify, data_line_computational_feature,\
    data_line_verify_feature
from square_error import square_error

'''
  Source: 
  http://reliawiki.org/index.php/Multiple_Linear_Regression_Analysis#Estimating_Regression_Models_Using_Least_Squares
  Compute the Bi argument:
  Let y be a vector of all the salary.
  Let X be a matrix of all the parameter : gender, rank, year, degree.
  Let B be the vector of all the Bi argument.
  Let E be the vector off all the error.

  First compute: new_B=(X'*X)^-1*X'*y (where ' means the transpose and ^-1 represents the matrix inverse)
  Then compute new_y = X*new_B
  Finally compute new_E = y-new_y
  '''


def compute_vector_y_and_x(y, x, data_set):
    for data_line in data_set:
        y.append(data_line.salary)
        x.append([1,
                  data_line.gender,
                  data_line.rank,
                  data_line.years,
                  data_line.degree])


def compute_vector_y_and_x_features(y_features, x_features, data_set_features):
    for data_line in data_set_features:
        y_features.append(data_line.salary)
        x_features.append([1,
                           data_line.gender,
                           data_line.rank,
                           data_line.years,
                           data_line.degree,
                           data_line.university,
                           data_line.nationality])


# data_set is a list of DataLine object. -> compute the B's
def compute_linear_regression(y_compute, x_compute):
    x_compute = np.matrix(x_compute, dtype='float64')
    y_compute = np.array(y_compute, dtype='float64')
    return np.matmul(np.matmul(np.matmul(np.transpose(x_compute), x_compute).I, np.transpose(x_compute)), y_compute)


def verify_linear_regression(x, b_verify):
    x = np.matrix(x, dtype='float64')
    b_verify = np.matrix(b_verify, dtype='float64')
    return np.matmul(x, np.transpose(b_verify))


if __name__ == "__main__":
    # Compute B with 70% of the data.
    y_computational = []
    x_computational = []
    compute_vector_y_and_x(y_computational, x_computational, data_line_computational)

    b = compute_linear_regression(y_computational, x_computational)

    # Verify B with 30% of the data.
    y_verify = []
    x_verify = []
    compute_vector_y_and_x(y_verify, x_verify, data_line_verify)

    new_y_verify = verify_linear_regression(x_verify, b)

    # print("new y: \n", new_y_verify)

    error = square_error(new_y_verify, y_verify)

    print("error: ", error)

    '''From here we're dealing with the data set adding features. '''

    # Compute B with 70% of the data.
    y_computational_feature = []
    x_computational_feature = []
    compute_vector_y_and_x_features(y_computational_feature, x_computational_feature, data_line_computational_feature)

    b_feature = compute_linear_regression(y_computational_feature, x_computational_feature)

    # Verify B with 30% of the data.
    y_verify_feature = []
    x_verify_feature = []
    compute_vector_y_and_x_features(y_verify_feature, x_verify_feature, data_line_verify_feature)

    new_y_verify_feature = verify_linear_regression(x_verify_feature, b_feature)

    # print("new y: \n", new_y_verify)

    error_feature = square_error(new_y_verify_feature, y_verify_feature)

    print("error_feature: ", error_feature)

    '''
    Adding features do not improve the error cause the features we add are not relevant, and not based on
    the real life. 
    We here show that wrong information are detected.
    '''
