import unittest


def quicksort(vec):
    def sort(vec, m, M):
        i = m
        j = M-1
        pivot = vec[M]
        while i < j:
            lower = vec[i]
            upper = vec[j]
            if lower > upper:
                vec[i] = upper
                vec[j] = lower
                lower = vec[i]
                upper = vec[j]
            if upper > pivot:
                j -= 1
            if lower < pivot:
                i += 1

        if vec[i] > pivot:
            vec[M] = vec[i]
            vec[i] = pivot

        return i

    def quick(vec, i, j, n):
        if n > 20:
            return
        if i < j:
            cross = sort(vec, i, j)
            quick(vec, i, cross-1, n+1)
            quick(vec, cross+1, j, n+1)

    quick(vec, 0, len(vec)-1, 0)
    return vec


def quicksortK(vec, K):
    def sort(vec, m, M):
        i = m
        j = M-1
        pivot = vec[M]
        while i < j:
            lower = vec[i]
            upper = vec[j]
            if lower > upper:
                vec[i] = upper
                vec[j] = lower
                lower = vec[i]
                upper = vec[j]
            if upper > pivot:
                j -= 1
            if lower < pivot:
                i += 1

        if vec[i] > pivot:
            vec[M] = vec[i]
            vec[i] = pivot

        return i

    def quick(vec, i, j, n):
        if n > 3:
            return
        if i < j:
            cross = sort(vec, i, j)
            quick(vec, i, cross-1, n+1)
            if cross < K:
                quick(vec, cross+1, j, n+1)

    quick(vec, 0, len(vec)-1, 0)
    return vec[:K]


class TestStringMethods(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([4, 8, 5, 6, 1, 9, 7, 3, 2]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quicksortK(self):
        self.assertEqual(quicksortK([4, 8, 5, 6, 1, 9, 7, 3, 2], 3), [1, 2, 3])
        self.assertEqual(quicksortK([4, 8, 5, 6, 1, 9, 7, 3, 2], 3), [1, 2, 3])
        self.assertEqual(quicksortK([4, 8, 5, 6, 1, 9, 7, 3, 2], 3), [1, 2, 3])

        self.assertEqual(quicksortK([4, 8, 5, 6, 1, 9, 7, 3, 2], 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(quicksortK([4, 8, 5, 6, 1, 9, 7, 3, 2], 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(quicksortK([4, 8, 5, 6, 1, 9, 7, 3, 2], 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
