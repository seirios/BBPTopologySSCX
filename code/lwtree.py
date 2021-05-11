import numpy
import pandas
import tqdm
import brotli
import collections
import tarfile
from io import StringIO


def maximal_simplices(T):
    if len(T) == 0:
        return [[]]
    ret = []
    for gid, C in T.items():
        ret.extend([[gid] + smpl for smpl in maximal_simplices(C)])
    return ret


def simplices(T):
    def recursive(T):
        ret = [[]]
        for gid, C in T.items():
            ret.extend([[gid] + smpl for smpl in recursive(C)])
        return ret
    ret = []
    for gid, C in T.items():
        ret.extend([[gid] + smpl for smpl in recursive(C)])
    return ret


def maximal_simplex_counts(T):
    if len(T) == 0:
        return {-1: 1}
    ret = {}
    for C in T.values():
        for dim, count in maximal_simplex_counts(C).items():
            ret[dim + 1] = ret.get(dim + 1, 0) + count
    return ret


def simplex_counts(T):
    def recursive(T):
        ret = {-1: 1}
        for C in T.values():
            for dim, count in recursive(C).items():
                ret[dim + 1] = ret.get(dim + 1, 0) + count
        return ret
    ret = {}
    for C in T.values():
        for dim, count in recursive(C).items():
            ret[dim + 1] = ret.get(dim + 1, 0) + count
    return ret


def LwTree():
    return collections.defaultdict(LwTree)


def build_tree_lw(lvls, gids):
    T = LwTree()
    parents = {0: T}
    for lvl, gid in zip(lvls, gids):
        t = parents[lvl]
        _ = t[gid]
        parents[lvl + 1] = t[gid]
    return T


def parse_lwtree_pd(bytes_struc, maxdim=10):
    raw = bytes_struc.decode("utf-8")
    data = pandas.read_csv(StringIO(raw.replace("*", "")),
                           sep=' ',
                           header=None,
                           names=[str(_x) for _x in range(maxdim)]).values
    x, lvls = numpy.nonzero(~numpy.isnan(data))
    gids = data[x, lvls].astype(int)
    return build_tree_lw(lvls, gids)


def parse_lwtree_np(bytes_struc):
    raw = bytes_struc.decode("utf-8").replace("*", "")
    raw_splt = raw.split("\n")
    lvls = [row.count(" ") for row in raw_splt]
    gids = [int(row) for row in raw_splt if len(row) > 0]
    return build_tree_lw(lvls, gids)


def load_lwtrees(file_tar, maxproc=None):
    """
    Load simplex trees from a TAR archive holding brotli-compressed text trees.
    """
    lwtrees = []
    with tarfile.open(file_tar, 'r:') as tf:
        membs = tf.getmembers()
        for i, memb in tqdm.tqdm(enumerate(membs), total=numpy.minimum(maxproc, len(membs))):
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
