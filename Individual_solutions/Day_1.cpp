#include <iostream>
#include <fstream>
#include <string>
#include <vector>


std::string day_1_solution () {
    std::ifstream f;
    f.open("../inputs/Day_1_input.txt", std::ios::in);
    std::string result;
    if (f.is_open()) {
        char data[100]{};
        std::string line;
        std::vector<int> numbers;
        while (f.good()) {
            std::getline(f, line);
            int line_int = std::stoi(line, nullptr);
            numbers.push_back(line_int);
        }
        f.close();
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                for (int k = j + 1; k < numbers.size(); k++) {
                    if ((numbers[i] + numbers[j] + numbers[k]) == 2020) {
                        std::string result = std::to_string(numbers[j] * numbers[i] * numbers[k]);
                        std::cout << std::to_string(numbers[i]) + "+" + std::to_string(numbers[j]) + "+" + std::to_string(numbers[k]) + "=" + result;
                    }
                }
            }
        }
    }
    else {
        return "File not found!";
    }
    return result;
}