from sage.all import libgap
from CrystalPointGroupMN import CrystalPointGroupMN

# SO(3) の指標 χ_l(θ) [θ = 2πm/n]。χ_l(θ) = χ_l(2π-θ) なので m と n-m は同値。
SO3_CHI_TABLE = {
    (0, 1): {0: 1, 1: 3, 2: 5, 3: 7},
    (1, 2): {0: 1, 1: -1, 2: 1, 3: -1},
    (1, 3): {0: 1, 1: 0, 2: -1, 3: 1},
    (1, 4): {0: 1, 1: 1, 2: -1, 3: -1},
    (1, 6): {0: 1, 1: 2, 2:  1, 3: -2},
}

def chi_o3(l, m, n, parity):
    """O(3) 上の χ_l(g)。g が不正則なら (-1)^l を乗じる。"""
    key = min(m % n, (-m) % n)
    return parity**l * SO3_CHI_TABLE[(key, n)][l]


def import_character_table(gap_expr):
    libgap.LoadPackage("ctbllib")
    T = libgap.eval(f"CharacterTable({gap_expr})")
    sizes = [int(s) for s in libgap.SizesConjugacyClasses(T)]
    irreps = [[int(v) for v in chi] for chi in libgap.RationalizedMat(libgap.Irr(T))]
    return sizes, irreps


def decompose_spdf(name, pgmn: CrystalPointGroupMN):
    gap_expr = pgmn.get_gap_expr(name)
    sizes, irreps = import_character_table(gap_expr)
    order = sum(sizes)
    k = len(sizes)

    class_mnp = pgmn.get_mn(name)
    if len(class_mnp) != k:
        raise ValueError(f"(m,n,p) length mismatch for {name}: {len(class_mnp)} vs {k}")

    so3 = {
        's': [chi_o3(0, m, n, p) for (m, n, p) in class_mnp],
        'p': [chi_o3(1, m, n, p) for (m, n, p) in class_mnp],
        'd': [chi_o3(2, m, n, p) for (m, n, p) in class_mnp],
        'f': [chi_o3(3, m, n, p) for (m, n, p) in class_mnp],
    }

    dims = [chi[0] for chi in irreps]  # χ(E) = 次元
    result = {l: {} for l in ['s', 'p', 'd', 'f']}
    for label in ['s', 'p', 'd', 'f']:
        chi_l = so3[label]
        for idx, chi_ir in enumerate(irreps):
            mult = sum(sizes[j] * chi_l[j] * chi_ir[j] for j in range(k)) // order
            if mult != 0:
                result[label][idx] = mult

    return result, dims


if __name__ == "__main__":
    import sys
    pg = CrystalPointGroupMN()
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        groups = pg.list_groups()
        for i, g in enumerate(groups, 1):
            print(f"  {i:2}. {g}")
        choice = input("点群を選択 (番号または名前): ").strip()
        name = groups[int(choice) - 1] if choice.isdigit() else choice

    result, dims = decompose_spdf(name, pg)
    print(f"\n{name} の s/p/d/f 分裂:")
    for label, decomp in result.items():
        if decomp:
            parts = [f"#{idx}(dim={dims[idx]})×{mult}" for idx, mult in decomp.items()]
            print(f"  {label}: {' + '.join(parts)}")
