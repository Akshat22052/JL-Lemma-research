

    #include <iostream>
    #include <vector>
    #include <random>
    #include <cmath>
    #include <fstream>


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
        // const int n = 100000;   // Number of points
        // const int d = 1000;    // Number of dimensions

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

        // Calculate distances and ratios
        vector<pair<double, double> > distances;
        // int numDistancesToCalculate = 100000;

        for (int i = 0; i < numDistancesToCalculate; ++i) {
            int idx1 = rand() % n;
            int idx2 = rand() % n;
            while (idx1 == idx2) {
                idx2 = rand() % n;
            }
            double origDist = computeDistance(points[idx1], points[idx2]);
            double transDist = computeDistance(transformedPoints[idx1], transformedPoints[idx2]);
            distances.emplace_back(origDist, transDist);
        }

        ofstream outFile("ratios.txt");
        if (!outFile.is_open()) {
            cout << "Unable to create output file." << endl;
            return 1;
        }
        // outFile << "n = " << n << endl;
        // outFile << "d = " << d << endl;
        // outFile << "k = " << k << endl;
        // outFile << "epsilon = " << e << endl;

        for (size_t i = 0; i < distances.size(); ++i) {
            double ratio = distances[i].second / distances[i].first;
            outFile << "Pair " << i + 1 << ": Ratio = " << ratio << endl;
        }
        outFile.close();

        cout << "Ratios saved in 'ratios.txt' file." << endl;

        ofstream configOutFile("config.txt");
        if (!configOutFile.is_open()) {
            cout << "Unable to create config file." << endl;
            return 1;
        }
        configOutFile << "n = " << n << endl;
        configOutFile << "d = " << d << endl;
        configOutFile << "k = " << k << endl;
        configOutFile << "epsilon = " << e << endl;
        configOutFile.close();



        return 0;
    }
