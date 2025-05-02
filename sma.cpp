#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>

using namespace std;

double calculateSMA(const double* prices, int size, int window) {
    if (window > size || window <= 0) {
        throw invalid_argument("Invalid window size.");
    }

    double sum = 0;
    for (int i = size - window; i < size; ++i) {
        sum += prices[i];
    }

    return sum / window;
}

string makeDecision(double currentPrice, double sma) {
    if (currentPrice > sma) return "Buy";
    if (currentPrice < sma) return "Sell";
    else return "Hold";
}


int main() {
    const int numDays = 5;
    double* prices = new double[numDays];

    cout <<  "Enter closing prices for the last "  << numDays << "days:\n";
    for (int i = 0; i < numDays; ++i) {
        cout << "Day " << i + 1 << ":";
        cin >> prices[i];
    }

    int window = 3; 
    try {
        double sma = calculateSMA(prices, numDays, window);
        double currentPrice = prices[numDays - 1];
        string decision = makeDecision(currentPrice, sma);

        cout << "\nSMA(" << window << "):" << sma << "\n";
        cout << "Current Prices: " << currentPrice << "\n";
        cout << "Trading Decision: " << decision << "\n";
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }

    delete[] prices;
    return 0;
}