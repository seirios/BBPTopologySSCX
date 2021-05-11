# lwtree: lightweight trees
# AUTHOR: Michael Reimann <michael.reimann@epfl.ch>
# AUTHOR: Sirio Bolaños Puchet <sirio.bolanospuchet@epfl.ch>
# LAST MODIFIED: 2021-05-11

import numpy
import brotli
import tarfile
import collections

# tqdm is optional dependency
try:
    import tqdm
    iter_status_fun = lambda t, x, **kw: tqdm.tqdm(x, **kw) if t else x
except ImportError:
    iter_status_fun = lambda t, x, **kw: x


def simplices(T, maximal_only=False):
    """
    Recursively walk a tree and return a list of tuples, where:

    [0]: list of GIDs in simplex
    [1]: maximality indicator

    If maximal_only, only returns maximal simplices.
    """
    def recursive(T):
        ret = [[]]
        for (gid, m), C in T.items():
            ret.extend([[(gid, m)] + smpl for smpl in recursive(C)])
        return ret
    ret = recursive(T)[1:]
    ret = [([x[0] for x in simp], numpy.sum([x[1] for x in simp])) for simp in ret]
    return ret if not maximal_only else [x for x in ret if x[1]]


def simplex_counts(T, maximal_only=False):
    """
    Count simplices by accumulating while recursively walking a simplex tree
    """
    def recursive(T, is_max):
        if maximal_only and is_max:
            return {-1: 1}
        ret = {} if maximal_only else {-1: 1}
        for (_, is_max), C in T.items():
            for dim, count in recursive(C, is_max).items():
                ret[dim + 1] = ret.get(dim + 1, 0) + count
        return ret
    ret = recursive(T, False)
    ret.pop(-1, None) 
    return ret


# default factory for defaultdict
def LwTree():
    return collections.defaultdict(LwTree)


def build_tree_lw(lvls, gids, maxs):
    """
    Build tree as a dictionary of dictionaries,
    where keys are tuples (GID, is_maximal)
    """
    T = LwTree()
    parents = {0: T}  # temporary storage of last seen parent at some level
    for lvl, gid, m in zip(lvls, gids, maxs):
        t = parents[lvl]
        parents[lvl + 1] = t[(gid, m)]
    return T


def parse_lwtree_np(bytes_struc):
    """
    Parse text representation of a tree as a list of UTF-8 lines,
    extracting level, gid and maximal indicator from each line
    """
    raw = bytes_struc.decode("utf-8")
    raw_splt = raw.split("\n")
    lvls = [row.count(" ") for row in raw_splt]
    maxs = [row.count("*") for row in raw_splt]  # maximal simplex indicator
    gids = [int(row[:-1]) if maxs[i] else int(row) for i, row in enumerate(raw_splt) if len(row) > 0]
    return build_tree_lw(lvls, gids, maxs)


def load_lwtrees(file_tar, maxproc=None, show_progress=True):
    """
    Load simplex trees from a TAR archive holding brotli-compressed text trees.
    """
    lwtrees = []
    with tarfile.open(file_tar, 'r:') as tf:
        membs = tf.getmembers()
        for i, memb in iter_status_fun(show_progress, enumerate(membs),
                                       total=numpy.minimum(maxproc, len(membs))):
            if maxproc is not None and i >= maxproc:
                break
            with tf.extractfile(memb) as f:
                compr_data = f.read1(memb.size)
                assert(len(compr_data) == memb.size)
                data = brotli.decompress(compr_data)
                del compr_data  # free early
                tree = parse_lwtree_np(data)
                del data  # free early
                lwtrees.append(tree)

    return lwtrees
