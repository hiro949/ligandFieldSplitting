# mulliken.py

from dataclasses import dataclass

# ============================================================
#  Point group → series
# ============================================================

PG_SERIES = {
    "C1":  "Cn",
    "Ci":  "Cnh",
    "C2":  "Cn",
    "Cs":  "Cnv",
    "C2h": "Cnh",
    "D2":  "Dn",
    "C2v": "Cnv",
    "D2h": "Dnh",
    "C4":  "Cn",
    "S4":  "Dnd",
    "C4h": "Cnh",
    "D4":  "Dn",
    "C4v": "Cnv",
    "D2d": "Dnd",
    "D4h": "Dnh",
    "C3":  "Cn",
    "C3i": "Cnh",
    "D3":  "Dn",
    "C3v": "Cnv",
    "D3d": "Dnd",
    "C6":  "Cn",
    "C3h": "Cnh",
    "C6h": "Cnh",
    "D6":  "Dn",
    "C6v": "Cnv",
    "D3h": "Dnh",
    "D6h": "Dnh",
    "T":   "T",
    "Th":  "Th",
    "O":   "O",
    "Td":  "Td",
    "Oh":  "Oh",
}

# ============================================================
#  操作インデックス
# ============================================================

@dataclass
class PGOps:
    idx_E: int
    idx_Cn: int | None = None
    idx_C2: int | None = None
    idx_C2x: int | None = None
    idx_C2y: int | None = None
    idx_C2z: int | None = None
    idx_sigma_v: int | None = None
    idx_sigma_d: int | None = None
    idx_sigma_h: int | None = None
    idx_S4: int | None = None
    idx_i: int | None = None
    idx_C4: int | None = None
    idx_C3: int | None = None


PG_OPS: dict[str, PGOps] = {
    # インデックスは hiro の CrystalPointGroupMN.data の順番に対応

    "C1":  PGOps(idx_E=0),

    "Ci":  PGOps(idx_E=0, idx_i=1),

    "C2":  PGOps(idx_E=0, idx_Cn=1),

    "Cs":  PGOps(idx_E=0, idx_sigma_v=1),

    "C2h": PGOps(idx_E=0, idx_Cn=1, idx_i=2, idx_sigma_h=3),

    "D2":  PGOps(idx_E=0, idx_Cn=1, idx_C2x=2, idx_C2y=3),

    "C2v": PGOps(idx_E=0, idx_Cn=1, idx_sigma_v=2, idx_sigma_d=3),

    "D2h": PGOps(
        idx_E=0,
        idx_Cn=1,      # C2(z)
        idx_C2y=2,
        idx_C2x=3,
        idx_i=4,
        idx_sigma_h=5, # σ(xy)
        idx_sigma_v=6, # σ(xz)
        idx_sigma_d=7, # σ(yz)
    ),

    "C4":  PGOps(idx_E=0, idx_Cn=1, idx_C2=2, idx_C4=1),

    "S4":  PGOps(idx_E=0, idx_C2=2, idx_S4=1),

    "C4h": PGOps(
        idx_E=0,
        idx_Cn=1,
        idx_C2=2,
        idx_C4=1,
        idx_i=4,
        idx_sigma_h=6,
        idx_S4=5,
    ),

    "D4":  PGOps(
        idx_E=0,
        idx_Cn=1,   # C2(z)
        idx_C4=2,   # 2C4
        idx_C2x=3,  # 2C2'
        idx_C2y=4,  # 2C2''
    ),

    "C4v": PGOps(
        idx_E=0,
        idx_Cn=1,      # C2(z)
        idx_C4=2,      # 2C4
        idx_sigma_v=3, # 2σv
        idx_sigma_d=4, # 2σd
    ),

    "D2d": PGOps(
        idx_E=0,
        idx_Cn=1,      # C2(z)
        idx_S4=2,      # 2S4
        idx_C2x=3,     # 2C2'
        idx_sigma_d=4, # 2σd
    ),

    "D4h": PGOps(
        idx_E=0,
        idx_Cn=1,
        idx_C4=2,
        idx_C2x=3,
        idx_C2y=4,
        idx_i=5,
        idx_sigma_h=6,
        idx_S4=7,
        idx_sigma_v=8,
        idx_sigma_d=9,
    ),

    "C3":  PGOps(idx_E=0, idx_Cn=1, idx_C3=1),

    "C3i": PGOps(
        idx_E=0,
        idx_Cn=1,
        idx_C3=1,
        idx_i=3,
    ),

    "D3":  PGOps(
        idx_E=0,
        idx_Cn=1,  # 2C3
        idx_C3=1,
        idx_C2=2,  # 3C2
    ),

    "C3v": PGOps(
        idx_E=0,
        idx_Cn=1,      # 2C3
        idx_C3=1,
        idx_sigma_v=2, # 3σv
    ),

    "D3d": PGOps(
        idx_E=0,
        idx_i=1,
        idx_Cn=2,      # 2C3
        idx_C3=2,
        idx_S4=3,      # 2S6
        idx_C2=4,      # 3C2
        idx_sigma_d=5, # 3σd
    ),

    "C6":  PGOps(
        idx_E=0,
        idx_Cn=1,  # C6
        idx_C3=2,
        idx_C2=3,
    ),

    "C3h": PGOps(
        idx_E=0,
        idx_sigma_h=1,
        idx_Cn=2,  # C3
        idx_C3=2,
    ),

    "C6h": PGOps(
        idx_E=0,
        idx_Cn=1,  # C6
        idx_C3=2,
        idx_C2=3,
        idx_i=6,
        idx_sigma_h=9,
    ),

    "D6":  PGOps(
        idx_E=0,
        idx_C2=1,
        idx_Cn=2,  # 2C6
        idx_C3=3,  # 2C3
    ),

    "C6v": PGOps(
        idx_E=0,
        idx_C2=1,
        idx_Cn=2,      # 2C6
        idx_C3=3,      # 2C3
        idx_sigma_v=4, # 3σv
        idx_sigma_d=5, # 3σd
    ),

    "D3h": PGOps(
        idx_E=0,
        idx_sigma_h=1,
        idx_Cn=2,      # 2C3
        idx_C3=2,
        idx_S4=3,      # 2S3
        idx_C2=4,      # 3C2
        idx_sigma_v=5, # 3σv
    ),

    "D6h": PGOps(
        idx_E=0,
        idx_C2=1,
        idx_Cn=2,      # 2C6
        idx_C3=3,      # 2C3
        idx_C2x=4,     # 3C2'
        idx_C2y=5,     # 3C2''
        idx_i=6,
        idx_sigma_h=7,
        idx_S4=8,      # 2S3
        idx_C4=9,      # 2S6 (proper C3)
        idx_sigma_d=10,# 3σd
        idx_sigma_v=11,# 3σv
    ),

    "T": PGOps(
        idx_E=0,
        idx_C2=1,  # 3C2
        idx_C3=2,  # 4C3
    ),

    "Th": PGOps(
        idx_E=0,
        idx_C2=1,  # 3C2
        idx_C3=2,  # 4C3
        idx_i=4,
    ),

    "O": PGOps(
        idx_E=0,
        idx_C2=1,  # 3C2 (=C4^2)
        idx_C3=2,  # 8C3
        idx_C4=3,  # 6C4
    ),

    "Td": PGOps(
        idx_E=0,
        idx_C2=1,      # 3C2
        idx_C3=2,      # 8C3
        idx_S4=3,      # 6S4
        idx_sigma_d=4, # 6σd
    ),

"Oh": PGOps(
    idx_E=0,
    idx_i=1,
    idx_C2=8,      # ← ここを 2 → 8 に変更
    idx_sigma_h=3,
    idx_C3=4,
    idx_S4=7,
    idx_C4=6,
    idx_sigma_d=9,
),
}

# ============================================================
#  共通ヘルパ
# ============================================================

def parity_gu(chi, ops: PGOps) -> str:
    if ops.idx_i is None:
        return ""
    return "g" if chi[ops.idx_i] > 0 else "u"


# ============================================================
#  系列ごとのラベリング
# ============================================================

def label_Cn(chi, ops: PGOps) -> str:
    dim = chi[ops.idx_E]
    if dim == 1:
        if ops.idx_Cn is None:
            return "A"
        return "A" if chi[ops.idx_Cn] == 1 else "B"
    if dim == 2:
        return "E"
    if dim == 3:
        return "T"
    return "?"


def label_Cnv(chi, ops: PGOps) -> str:
    dim = chi[ops.idx_E]
    if dim == 2:
        return "E"
    base = "A" if (ops.idx_Cn is None or chi[ops.idx_Cn] == 1) else "B"
    if ops.idx_sigma_v is None:
        return base
    sub = "1" if chi[ops.idx_sigma_v] == 1 else "2"
    return base + sub


def label_Cnh(chi, ops: PGOps) -> str:
    dim = chi[ops.idx_E]
    base = "A" if (ops.idx_Cn is None or chi[ops.idx_Cn] == 1) else "B"
    prime = ""
    if ops.idx_sigma_h is not None:
        prime = "'" if chi[ops.idx_sigma_h] == 1 else "''"
    gu = parity_gu(chi, ops)
    if dim == 1:
        return base + prime + gu
    if dim == 2:
        return "E" + prime + gu
    if dim == 3:
        return "T" + prime + gu
    return "?"


def label_Dn(chi, ops: PGOps) -> str:
    dim = chi[ops.idx_E]
    if dim == 2:
        return "E"
    base = "A" if (ops.idx_Cn is None or chi[ops.idx_Cn] == 1) else "B"
    return base


def label_Dnh(chi, ops: PGOps) -> str:
    dim = chi[ops.idx_E]
    gu = parity_gu(chi, ops)
    if dim == 2:
        return "E" + gu
    base = "A" if (ops.idx_Cn is None or chi[ops.idx_Cn] == 1) else "B"
    return base + gu


def label_Dnd(chi, ops: PGOps) -> str:
    dim = chi[ops.idx_E]
    if dim == 2:
        return "E"
    base = "A" if (ops.idx_Cn is None or chi[ops.idx_Cn] == 1) else "B"
    return base


def label_T(chi, ops: PGOps) -> str:
    dim = chi[ops.idx_E]
    return {1: "A", 2: "E", 3: "T"}.get(dim, "?")


def label_Th(chi, ops: PGOps) -> str:
    base = label_T(chi, ops)
    gu = parity_gu(chi, ops)
    return base + gu


def label_Td(chi, ops: PGOps) -> str:
    dim = chi[ops.idx_E]

    # 1次元：A1 / A2 を S4 の符号で区別
    if dim == 1:
        if ops.idx_S4 is None:
            return "A1"
        return "A1" if chi[ops.idx_S4] == 1 else "A2"

    # 2次元：E
    if dim == 2:
        return "E"

    # 3次元：T1 / T2 を S4 の符号で区別
    if dim == 3:
        if ops.idx_S4 is None:
            return "T"
        return "T1" if chi[ops.idx_S4] == 1 else "T2"

    return "?"


def label_O(chi, ops: PGOps) -> str:
    dim = chi[ops.idx_E]
    if dim == 1:
        if ops.idx_C2 is None:
            return "A1"
        return "A1" if chi[ops.idx_C2] == 1 else "A2"
    if dim == 2:
        return "E"
    if dim == 3:
        if ops.idx_C4 is None:
            return "T"
        return "T1" if chi[ops.idx_C4] == 1 else "T2"
    return "?"


def label_Oh(chi, ops: PGOps) -> str:
    base = label_O(chi, ops)
    gu = parity_gu(chi, ops)
    return base + gu


# ============================================================
#  ディスパッチャ
# ============================================================

SERIES_LABELER = {
    "Cn":  label_Cn,
    "Cnv": label_Cnv,
    "Cnh": label_Cnh,
    "Dn":  label_Dn,
    "Dnh": label_Dnh,
    "Dnd": label_Dnd,
    "T":   label_T,
    "Th":  label_Th,
    "Td":  label_Td,
    "O":   label_O,
    "Oh":  label_Oh,
}


def mulliken_label(pg_name: str, chi) -> str:
    """
    pg_name: Schoenflies 記号（"Oh", "C2v" など）
    chi:     その既約表現の指標ベクトル（クラス順は CrystalPointGroupMN.data と同じ）
    """
    series = PG_SERIES[pg_name]
    ops = PG_OPS[pg_name]
    f = SERIES_LABELER[series]
    return f(chi, ops)

if __name__ == "__main__":
    from sage.all import libgap
    from CrystalPointGroupMN import CrystalPointGroupMN

    pg = CrystalPointGroupMN()

    # テストしたい点群をここに並べる
    TEST_GROUPS = ["C2v", "D2h", "C3v", "Td", "Oh"]

    for name in TEST_GROUPS:
        print("\n==============================")
        print(f"Testing point group: {name}")
        print("==============================")

        # GAP の CharacterTable を取得
        T = libgap.eval(f"CharacterTable({pg.get_gap_expr(name)})")
        irr = libgap.Irr(T)

        # 各既約表現について Mulliken 記号を表示
        for i, chi in enumerate(irr):
            chi_list = list(chi)
            label = mulliken_label(name, chi_list)
            print(f"irrep {i}: chi = {chi_list} → {label}")