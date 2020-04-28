import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
from datetime import datetime

def polynom_coeff(pX, pY):
    A = np.vander(pX)
    b = pY
    coeffs = np.linalg.solve(A, b)
    return coeffs

def lagrange_coeff(pX, pY):
    polynom = lagrange(pX, pY)
    coeffs = Polynomial(polynom).coef
    return coeffs

def new_values(coeffs, pX):
    N = len(coeffs)
    y_salida = np.zeros(len(pX))
    for i in range(len(pX)):
        for j in range(N):
            y_salida[i] += (coeffs[j] * (pX[i] ** (N - j - 1)))
    return y_salida