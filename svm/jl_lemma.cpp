#include <iostream>
#include <vector>
#include <random>
#include <fstream>
#include <cmath>

using namespace std;

// Function to compute the Euclidean distance between two points
double computeDistance(const vector<double>& point1, const vector<double>& point2) {
    double distance = 0.0;
    for (size_t i = 0; i < point1.size(); ++i) {
        distance += pow(point1[i] - point2[i], 2);
    }
    return sqrt(distance);
}

// Function to generate random points
vector<vector<double> > generateRandomPoints(int n, int d) {
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<double> dist(-100.0, 100.0); // Adjust the range of random values as needed

    vector<vector<double> > points(n, vector<double>(d));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < d; ++j) {
            points[i][j] = dist(gen);
        }
    }

    return points;
}

// Function to generate a random matrix
vector<vector<double> > generateRandomMatrix(int k, int D) {
    vector<vector<double> > matrix(k, vector<double>(D));

    random_device rd;
    mt19937 gen(rd());
    normal_distribution<double> dist(0.0, 1.0); // Standard normal distribution

    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < D; ++j) {
            matrix[i][j] = dist(gen); // Filling the matrix with random values
        }
    }

    return matrix;
}

int main() {
    int n, d, numDistancesToCalculate;

    cout << "Enter the number of points (n): ";
    cin >> n;

    cout << "Enter the number of dimensions (d): ";
    cin >> d;

    cout << "Enter the number of distances to calculate: ";
    cin >> numDistancesToCalculate;

    vector<vector<double> > points = generateRandomPoints(n, d);

    double e;
    do {
        cout << "Enter the value of e (between 0 and 1): ";
        cin >> e;
    } while (e <= 0 || e >= 1); // Keep prompting until e is between 0 and 1

    int k_min = 24 * log(n) / (3 * (pow(e, 2)) - 2 * (pow(e, 3)));

    cout << "Minimum value of k: " << k_min << endl;

    int k;
    cout << "Enter the value of k (min value should be " << k_min << "): ";
    cin >> k;

    cout << "Chosen value of k: " << k << endl;

    // Write the values to a file
    ofstream outfile("parameters.txt");
    if (outfile.is_open()) {
        outfile << n << " " << d << " " << e << " " << k << " " << k_min;
        outfile.close();
        cout << "Values written to 'parameters.txt' file." << endl;
    } else {
        cout << "Unable to open file for writing." << endl;
    }

    // Generating the random matrix M with dimensions k x D
    vector<vector<double> > M = generateRandomMatrix(k, d);
    vector<vector<double> > transformedPoints;

    for (const auto& point : points) {
        vector<double> transformedPoint(k, 0.0);
        for (int i = 0; i < k; ++i) {
            for (int j = 0; j < d; ++j) {
                transformedPoint[i] += M[i][j] * point[j];
            }
            transformedPoint[i] /= sqrt(k); // Scaling by 1/sqrt(k)
        }
        transformedPoints.push_back(transformedPoint);
    }

    // Save original points to a file
    ofstream originalFile("original_points.txt");
    if (originalFile.is_open()) {
        for (const auto& point : points) {
            for (const auto& coord : point) {
                originalFile << coord << " ";
            }
            originalFile << endl;
        }
        originalFile.close();
    } else {
        cout << "Unable to create 'original_points.txt' file." << endl;
        return 1;
    }

    // Save transformed points to a file
    ofstream transformedFile("transformed_points.txt");
    if (transformedFile.is_open()) {
        for (const auto& point : transformedPoints) {
            for (const auto& coord : point) {
                transformedFile << coord << " ";
            }
            transformedFile << endl;
        }
        transformedFile.close();
    } else {
        cout << "Unable to create 'transformed_points.txt' file." << endl;
        return 1;
    }

    cout << "Points saved in 'original_points.txt' and 'transformed_points.txt' files." << endl;

    return 0;
}
