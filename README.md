# TS_Forecasting_Project

# Time Series Forecasting with Multiple Neural Network Architectures

This repository provides a comprehensive comparison of both existing and novel neural network architectures for time series forecasting, implemented across three forecasting approaches: local, global, and clustering-based forecasting. The models are evaluated on multiple datasets, with performance metrics recorded for each model, dataset, and forecasting approach combination.

<img width="1261" alt="Capture d’écran 2025-02-17 à 14 07 51" src="https://github.com/user-attachments/assets/fab5bc7a-3336-4dec-9a21-c5e9a5797e0d" />


## Overview

Time series forecasting is a critical problem in many domains, such as finance, weather prediction, and energy consumption. This project aims to compare the performance of various neural network architectures, including traditional models like LSTM and GRU, as well as novel architectures designed for this task.

The following neural networks are evaluated on several publicly available time series datasets:

- **LSTM (Long Short-Term Memory)**
- **GRU (Gated Recurrent Units)**
- **Transformer-based architectures**
- **LTSF-Linear (NLinear,DLinear,Linear) (TCN)**
- **Attention-based models**
- **CNN_N_BEATS**
- **BEATS_CELL**
- **RLinear**
- **RMLP**
- **N-BEATS**
- **Multivariate M-N-BEATS**
- **SegRNN**
- **Other novel architectures (found in /Models)**

The goal is to determine which architecture performs best across different time series data characteristics, across three forecasting approaches (local, global and clustering). For the forecasting approach, the clustrering algorthms used include K-Means, Optics and SOM algorithms (found in /clustering_files). 

## Datasets 

This project evaluates the models on multiple time series datasets. These datasets are stored in the Datasets/ folder. You can download or place your time series datasets in this folder, ensuring they follow the appropriate format.

Datasets used include:

Energy Consumption Data
- electricity
- ETTh1.csv
- ETTh2.csv
- ETTm1.csv
- ETTm2.csv
  
Stock Market Data
- exchange_rate.csv 
  
Traffic Data 
- traffic.csv
  
Weather Data 
- weather.csv

All datasets used can be found on the kaggle plaform (https://www.kaggle.com/datasets/drparadox99/time-series-benchmark-datasets/data).

## Installation

To run the code, you will need Python 3.x and the required dependencies specified in the `requirements.txt` file.

To run code on CPU (default) : 
- bash run_all.sh

To run code on GPU : 
- specify GPU support in exec_1/main_exec.sh
- bash run_all 

 #Citing 
 
Implemented papers 
- Are Transformers Effective for Time Series Forecasting? (https://arxiv.org/pdf/2205.13504)
- SegRNN: Segment Recurrent Neural Network for Long-Term Time Series Forecasting (https://arxiv.org/abs/2308.11200)
- CNN-N-BEATS: Novel Hybrid Model for Time-Series Forecasting (https://link.springer.com/chapter/10.1007/978-3-031-66694-0_3)
- Deep Transformer Models for Time Series Forecasting: The Influenza Prevalence Case (https://arxiv.org/abs/2001.08317)
- ...
