# py-simptree: process simplex trees in python
# AUTHOR: Sirio Bolaños Puchet <sirio.bolanospuchet@epfl.ch>
# LAST MODIFIED: 2021-04-21

import treelib
import tarfile
import brotli


def count_simplices(root):
    """
    Count simplices per dimension.
    """
    maxdim = root.depth()
    counts = [0] * (maxdim + 1)
    counts_max = [0] * (maxdim + 1)
    for nid in root.expand_tree(mode=treelib.Tree.DEPTH):
        level = root.depth(nid)
        counts[level] += 1
        if root[nid].data:  # is maximal
            counts_max[level] += 1
    return counts, counts_max


def print_simplices(root, maximal_only=False):
    """
    Print simplex members, source to sink, mark with '*' if maximal.
    """
    sink = root.root  # sink GID (tree root)
    gids = []
    for nid in root.expand_tree(mode=treelib.Tree.DEPTH):
        node = root[nid]
        if maximal_only and not node.data:  # skip if maximal only and not maximal
            continue
        gids.append(str(node.tag))
        parent = root.parent(nid)
        while parent is not None:  # backwards path traversal
            gids.append(str(parent.tag))
            nid = parent.identifier
            parent = root.parent(nid)
        print(' '.join(gids + ['*' if node.data and not maximal_only else '']))
        gids = []  # clear


# FIXME: faster python implementation possible?
def parse_simptree(bstr, maxdim=None):
    """
    Parse a treelib.Tree from a bytestring. Adapted from C implementation.
    """
    GIDMAX_DIGITS = 10  # maximum number of digits in a uint32
    DIGITS = [ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9')]

    # state vars
    numbuf = []
    nump = 0
    level = 1
    is_maximal = False

    root = treelib.Tree()  # tree object

    # last seen parent per level
    last = {}
    last[0] = None

    for c in bstr:
        if c in DIGITS:
            if nump > GIDMAX_DIGITS - 1:
                raise Exception("Number too long: length > {}".format(GIDMAX_DIGITS))
            numbuf.append(chr(c))
        elif c == ord(' '):
            level += 1
        elif c == ord('*'):
            is_maximal = True
        elif c == ord('\n'):
            gid = int(''.join(numbuf))  # char list to string to integer
            if maxdim is None or level <= maxdim + 1:
                last[level] = root.create_node(gid, parent=last[level - 1], data=is_maximal)
            # reset state vars
            numbuf = []
            nump = 0
            level = 1
            is_maximal = False
        else:
            raise Exception("Invalid character found: '{}'".format(chr(c)))

    return root


def load_simptrees(file_tar, maxdim=None, maxproc=None, verbose=False):
    """
    Load simplex trees from a TAR archive holding brotli-compressed text trees.
    """
    if verbose:
        import sys

    simptrees = []
    with tarfile.open(file_tar) as tf:
        for i, memb in enumerate(tf.getmembers()):
            if maxproc is not None and i >= maxproc:
                break
            if verbose:
                print("Now processing file {}".format(memb.name), file=sys.stderr)
            with tf.extractfile(memb) as f:
                compr_data = f.read()
                assert(len(compr_data) == memb.size)
                data = brotli.decompress(compr_data)
                tree = parse_simptree(data, maxdim)
                simptrees.append(tree)
    return simptrees


# convenience CLI
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("py-simptree")
    parser.add_argument("file_tar", nargs='+', help="TAR archive holding brotli-compressed text trees")
    parser.add_argument("-c","--count", default=True, action="store_true", help="Count simplices per dimension")
    parser.add_argument("-d","--maxdim", type=int, default=None, help="Maximum simplex dimension to process")
    parser.add_argument("-m","--maximal-only", default=False, action="store_true", help="Print maximal simplices only")
    parser.add_argument("-p","--print", default=False, action="store_true", help="Print simplices")
    parser.add_argument("-v","--verbose", default=False, action="store_true", help="Verbose messages")
    parser.add_argument("--maxproc", type=int, default=None, help="Process up to this number of files in total")

    import sys
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    tree_counts = []
    tree_counts_max = []
    maxproc = args.maxproc  # max files to process
    for fname in args.file_tar:
        simptrees = load_simptrees(fname, args.maxdim, maxproc, args.verbose)
        maxproc -= len(simptrees)

        if args.print:
            for tree in simptrees:
                print_simplices(tree, args.maximal_only)
        elif args.count:
            for tree in simptrees:
                counts, counts_max = count_simplices(tree)
                tree_counts.append(counts)
                tree_counts_max.append(counts_max)
        
        if maxproc == 0:
            break

    if args.print:
        pass
    elif args.count:
        import itertools
        counts = [sum(i) for i in itertools.zip_longest(*tree_counts, fillvalue=0)]
        counts_max = [sum(i) for i in itertools.zip_longest(*tree_counts_max, fillvalue=0)]
        for i, (c, cm) in enumerate(itertools.zip_longest(counts, counts_max, fillvalue=0)):
            print('{} {} {}'.format(i, c, cm))
