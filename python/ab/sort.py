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
        print i, j, n
        if i < j:
            cross = sort(vec, i, j)
            quick(vec, i, cross-1, n+1)
            quick(vec, cross+1, j, n+1)

    quick(vec, 0, len(vec)-1, 0)
