# Necessary libraries

# Python Data reading/writing libraries 
import pandas as pd
import numpy as np

# Data plotting libraries
import matplotlib.pyplot as plt
%matplotlib inline
import plotly.express as px

#
import warnings
warnings.filterwarnings('ignore')

# Smoothing
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing,Holt
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Data_Series Stationary check tests
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss