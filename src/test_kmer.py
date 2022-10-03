# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from itertools import count
from kmer import(
    kmer,
    unique_kmers,
    count_kmers
)


def test_kmer():
    assert kmer('atcg', 1) == ['a', 't', 'c', 'g']
    assert kmer('acgtcgat', 3) == ['acg', 'cgt', 'gtc', 'tcg', 'cga', 'gat']
    assert kmer('', 3) == []
    assert kmer('ctgaatcg', 0) == []

def test_unique_kmers():
    assert unique_kmers('atcg', 1) == ['a', 't', 'c', 'g']
    assert unique_kmers('aaaaaaaaaaaa', 4) == ['aaaa']
    assert unique_kmers('gtaccgta', 3) == ['gta', 'tac', 'acc', 'ccg', 'cgt']
    assert unique_kmers('', 3) == []
    assert unique_kmers('ctgaatcg', 0) == []

def test_count_kmers():
    assert count_kmers('atcg', 1) == {'a': 1, 't': 1, 'c': 1, 'g': 1}
    assert count_kmers('aaaaaaaaaaa', 2) == {'aa': 10}
    assert count_kmers('gtcagtcacagt', 3) == {'gtc': 2, 'tca': 2, 'cag': 2, 'agt': 2, 'cac': 1, 'aca': 1}
    assert count_kmers('', 3) == {}
    assert count_kmers('cagtcagt', 0) == {}