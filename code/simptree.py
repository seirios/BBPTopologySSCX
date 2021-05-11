# py-simptree: process simplex trees in python
# AUTHOR: Sirio Bolaños Puchet <sirio.bolanospuchet@epfl.ch>
# LAST MODIFIED: 2021-05-11

import lwtree


def count_simplices(root):
    """
    Count simplices per dimension.
    """
    counts = lwtree.simplex_counts(root, False)
    counts_max = lwtree.simplex_counts(root, True)
    return counts, counts_max


def print_simplices(root, maximal_only=False):
    """
    Print simplex members, source to sink, mark with '*' if maximal.
    """
    simp = lwtree.simplices(root, maximal_only)
    for (s, m) in simp:
        [print(x, end=' ') for x in s[::-1]]
        print('*') if m and not maximal_only else print('')


def load_simptrees(file_tar, maxproc=None, show_progress=True):
    """
    Load simplex trees from a TAR archive holding brotli-compressed text trees.
    """
    return lwtree.load_lwtrees(file_tar, maxproc, show_progress)


# convenience CLI
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("py-simptree")
    parser.add_argument("file_tar", nargs='+', help="TAR archive holding brotli-compressed text trees")
    parser.add_argument("-c","--count", default=True, action="store_true", help="Count simplices per dimension")
    parser.add_argument("-m","--maximal-only", default=False, action="store_true", help="Print maximal simplices only")
    parser.add_argument("-p","--print", default=False, action="store_true", help="Print simplices")
    parser.add_argument("--no-progress", default=False, action="store_true", help="Do not show progress")
    parser.add_argument("--maxproc", type=int, default=None, help="Process up to this number of files in total")

    import sys
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    tree_counts = []
    tree_counts_max = []
    maxproc = args.maxproc  # max trees to process
    for fname in args.file_tar:
        simptrees = load_simptrees(fname, maxproc, not args.no_progress)
        if maxproc is not None:
            maxproc -= len(simptrees)

        if args.print:
            for tree in simptrees:
                print_simplices(tree, args.maximal_only)
        elif args.count:
            for tree in simptrees:
                counts, counts_max = count_simplices(tree)
                tree_counts.append(counts)
                tree_counts_max.append(counts_max)
        
        if maxproc is not None and maxproc == 0:
            break

    if args.print:
        pass
    elif args.count:
        from functools import reduce
        from collections import Counter
        counts = reduce(lambda x, y: Counter(x) + Counter(y), tree_counts)
        counts_max = reduce(lambda x, y: Counter(x) + Counter(y), tree_counts_max)
        for k in counts.keys():
            print('{} {} {}'.format(k, counts[k], counts_max.get(k, 0)))
