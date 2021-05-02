from setuptools import setup

setup(
name='Pytsforecast',
version='0.0.1',
description='Python workflow of operationalizing time series forecast',
url='https://github.com/phillip1029/pytsforecast.git',
author='Phillip Peng',
author_email='ppeng08@gmail.com',
license="MIT",
packages=['py_forecasttime'],
install_requires=["pandas", "numpy", "seaborn", "matplotlib", "IPython", "joblib", "statsmodels",
                  "tensorflow==2.2.0", "keras==2.3.1", "pandas", "pystan==2.19.1.1", "fbprophet",
                  "scikit-learn==0.22", "shap==0.32.1", "ipywidgets", "yellowbrick==1.0.1", 
                  "xgboost", "sklearn", "pmdarima", "pycaret", "yfinance", "torch", "plotly>=4.4.1", 
                 ]
)