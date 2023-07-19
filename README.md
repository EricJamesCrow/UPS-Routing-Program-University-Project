# Project: Efficient Routing and Delivery Distribution for WGUPS

## Table of Contents

1. [Introduction](#Introduction)
2. [Environment](#Environment)
3. [Assumptions](#Assumptions)
4. [Requirements](#Requirements)
5. [Usage](#Usage)
6. [Program Structure](#Program-Structure)
7. [Resources](#Resources)

## Introduction
The aim of this project is to implement an efficient algorithm for the Western Governors University Parcel Service (WGUPS) to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD). The goal is to ensure that all 40 packages are delivered on time, meeting each package's requirements and keeping the combined total distance traveled under 140 miles for both trucks.

This solution uses a self-adjusting algorithm and data structures to address these requirements, aiming to optimize the routing and delivery of packages.

## Environment
The project has been implemented using Python 3. The choice of Python is due to its simplicity, wide range of libraries, and its capabilities for implementing data structures and algorithms.

## Assumptions
The project is based on the following assumptions:

* Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
* The trucks travel at an average speed of 18 miles per hour.
* There are three trucks and two drivers available for deliveries.
* Drivers leave the hub no earlier than 8:00 a.m., and can return to the hub for packages if needed.
* The delivery and loading times are instantaneous.
* The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
* The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
* The day ends when all 40 packages have been delivered.

## Requirements
The project requirements dictate that the algorithm used should:

* Utilize non-linear data structures for efficient and maintainable software.
* Incorporate hashing techniques within an application to perform searching operations.
* Incorporate dictionaries and sets to organize data into key-value pairs.
* Evaluate the space and time complexity of self-adjusting data structures using big-O notation.
* Use self-adjusting heuristics to improve the performance of applications.
* Evaluate computational complexity theories to apply models to specific scenarios.

## Usage
To run the application:

1. Ensure that Python 3 is installed.
2. Navigate to the project directory.
3. Run the command `pip install -r requirements.txt`
4. Run the command `python main.py`.
5. Follow the on-screen prompts.

## Program Structure
The program is structured into several modules:

1. `main.py`: This is the main entry point of the application.
2. `utils/csv_reader.py`: This file parses package and distance data from CSV files into a HashMap and an Adjacency List respectively.
3. `models/hash_table.py`: This module implements the hash table used for storing and retrieving package data.
4. `models/graph.py`: This module defines the AdjacencyList class and related operations.
5. `models/truck.py`: This module defines the truck class and related operations.

## Resources
The project uses the following resources:

1. WGUPS Package File: Contains the package data.
2. Salt Lake City Downtown Map: Map of the delivery area.
3. WGUPS Distance Table: Contains the distances between different delivery points.
