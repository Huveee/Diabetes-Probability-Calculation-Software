
# Diabetes Probability Calculation Software

## Overview

This repository contains a Python-based desktop application designed to estimate the probability of a patient having diabetes. The program uses patient data and compares it to a pre-existing dataset (`diabetes.csv`) by calculating Euclidean distances to determine similarity and provide a probability percentage.

In addition to the Python application, implementations of Euclidean Distance calculation are also provided in **Go**, **Rust**, and **Ruby**.

## Features

- **Patient Data Input**: The program allows users to input patient data through a simple Graphical User Interface (GUI).
- **Data Validation**: The application ensures that inputted data falls within the valid ranges from the provided dataset.
- **Data Preprocessing**: The patient data is standardized (scaled between 0 and 1) before calculating distances.
- **Euclidean Distance Calculation**: The program calculates the Euclidean Distance between the input data and all records in the dataset, identifying the closest records.
- **Diabetes Probability Estimate**: Based on the closest records, the program provides a probability that the inputted patient has diabetes.

## Files

- **Python Implementation (`.py`)**: Contains the main application with GUI and diabetes probability estimation.
- **Go Implementation (`.go`)**: Euclidean distance calculation for two data points.
- **Rust Implementation (`.rs`)**: Euclidean distance calculation for two data points.
- **Ruby Implementation (`.rb`)**: Euclidean distance calculation for two data points.

## How to Use

### Python Application

1. Clone the repository:
    ```
    git clone https://github.com/Huveee/Diabetes-Probability-Calculation-Software.git
    cd Diabetes-Probability-Calculation-Software
    ```

2. Run the Python script:
    ```
    python diabetes_calculator.py
    ```

3. Input patient data into the provided fields in the GUI and run the program to get the probability estimate.

4. **Note**: The number of closest records to compare can be adjusted in the GUI.

### Additional Euclidean Distance Calculators

You can find implementations of Euclidean Distance in Go, Rust, and Ruby. Each script calculates the distance between two data points from the dataset. To run these scripts, use the following commands:

- **Go**:
    ```
    go run euclidean_distance.go
    ```

- **Rust**:
    ```
    cargo run euclidean_distance.rs
    ```

- **Ruby**:
    ```
    ruby euclidean_distance.rb
    ```

## Prerequisites

- **Python 3.x**
- **CSV Dataset** (`diabetes.csv`): Included in the repository.

For the additional language implementations, ensure you have Go, Rust, and Ruby installed.



 
