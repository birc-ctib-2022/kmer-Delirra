"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('agtagtcg', 4)
    ['agta', 'gtag', 'tagt', 'agtc', 'gtcg']

    >>> kmer('agtagctagt', 0)
    []
    """
    if k > 0 and len(x) > 0:
        kmers = [x[i:i + k] for i in range(len(x)-k+1)]
    else:
        return []
    return kmers



def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'gtc', 'tag', 'tcg']

    >>> unique_kmers('gatcgatcgatc', 4)
    ['atcg', 'cgat', 'gatc', 'tcga']
    """

    if k > 0 and len(x) > 0:
        kmers = {x[i:i+k] for i in range(len(x) - k + 1)}
    else:
        return []
    return sorted(list(kmers))


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('gatcgatcgatc', 4)
    {'gatc': 3, 'atcg': 2, 'tcga': 2, 'cgat': 2}
    """
    kmer_count = {}

    if k > 0 and len(x) > 0:
        for i in range(len(x) - k + 1):
            if x[i:i + k] not in kmer_count:
                kmer_count[x[i:i + k]] = 1
            else:
                kmer_count[x[i:i + k]] += 1
        return kmer_count
    else:
        return {}
