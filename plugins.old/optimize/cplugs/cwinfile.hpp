# include <stdio.h>
# include <iostream>
# include <string>
# include <fstream>
using namespace std;

string concatinate(string first, string second) {
    string endline = "\n";
    return first + endline + second;
}

string Cread(const char* filename) {
    ifstream file(filename);
    string line, lines;

    if (file.is_open()) {
        while (getline(file, line)) {
            lines = concatinate(lines, line);
        }
    } else {
        lines = "bad open";
    }
    file.close();
    return lines;
}

int Cwrite(const char* filename, const char* lines) {
    FILE* fm = fopen(filename, "wt");

    if (fm == NULL) {

        return 0;
    } else {

        fprintf(fm, "%s", lines);
        fclose(fm);

        return 1;
    }
}

bool exists(const char* filename) {
    ifstream file(filename);
    return file.good();
}