// Win32Project1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <sstream>
#include <iostream>
#include <functional>

void quicksort(int vec[], int N) {
	auto sort = [](int vec[], int m, int M) {
		int i = m, j = M-1;
		int pivot = vec[M];

		while (i < j) {
			int upper = vec[j];
			int lower = vec[i];

			if (lower > upper) {
				vec[i] = upper;
				vec[j] = lower;
				upper = lower;
				lower = vec[i];
			}
			i += lower < pivot ? 1 : 0;
			j -= upper > pivot ? 1 : 0;
		}
		if (vec[i] > pivot) {
			vec[M] = vec[i];
			vec[i] = pivot;
		}

		return i;
	};

	std::function<void(int*, int, int)> quick = [&](int vec[], int i, int j) {
		if (i < j) {
			int cross = sort(vec, i, j);
			quick(vec, i, cross - 1);
			quick(vec, cross + 1, j);
		}
	};

	quick(vec, 0, N-1);
}

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int vec[] = { 4, 8, 5, 6, 1, 9, 7, 3, 2 };
	for (int i=0; i<sizeof(vec)/sizeof(int); i++) cout << vec[i];
	cout << "\n";
	quicksort(vec, sizeof(vec) / sizeof(int));
	for (int i = 0; i<sizeof(vec)/sizeof(int); i++) std::cout << vec[i];
	cout << "\n";
	std::string input;
	std::getline(std::cin, input);
	return 0;
}

