import pytest
from CrystalPointGroupMN import CrystalPointGroupMN
from irrReduce import decompose_spdf

pg = CrystalPointGroupMN()

# ============================================================
# expected（実装の軸定義に基づく multiplicity）
# ============================================================

TEST_CASES = {
    "C1": {
        "s": {"A": 1},
        "p": {"A": 3},
        "d": {"A": 5},
        "f": {"A": 7},
    },

    "Ci": {
        "s": {"Ag": 1},
        "p": {"Au": 3},
        "d": {"Ag": 5},
        "f": {"Au": 7},
    },

    "C2v": {
        "s": {"A1": 1},
        "p": {"A1": 1, "B1": 1, "B2": 1},
        "d": {"A1": 2, "A2": 1, "B1": 1, "B2": 1},
        "f": {"A1": 2, "A2": 1, "B1": 2, "B2": 2},
    },

    "D2h": {
        "s": {"Ag": 1},
        "p": {"Au": 1, "Bu": 1},
        "d": {"Ag": 1, "Bg": 1},
        "f": {"Au": 2, "Bu": 2},
    },

    "Td": {
        "s": {"A1": 1},
        "p": {"T2": 1},
        "d": {"E": 1, "T2": 1},
        "f": {"A1": 1, "T1": 1, "T2": 1},
    },

    "Oh": {
        "s": {"A1g": 1},
        "p": {"T1u": 1},
        "d": {"Eg": 1, "T2g": 1},
        "f": {"A2u": 1, "T1u": 1, "T2u": 1},
    },
}

# ============================================================
# 許されるラベル置換（群の自己同型による任意性）
# ============================================================

ALLOWED_PERMUTATIONS = {
    "C1": [{}],

    "Ci": [
        {},
        {"Ag": "Au", "Au": "Ag"},
    ],

    "C2v": [
        {},
        {"B1": "B2", "B2": "B1"},
        {"A1": "A2", "A2": "A1"},
        {"A1": "A2", "A2": "A1", "B1": "B2", "B2": "B1"},
    ],

    "D2h": [
        {},
        {"Ag": "Bg", "Bg": "Ag", "Au": "Bu", "Bu": "Au"},
    ],

    "Td": [
        {},
        {"A1": "A2", "A2": "A1"},
        {"T1": "T2", "T2": "T1"},
        {"A1": "A2", "A2": "A1", "T1": "T2", "T2": "T1"},
    ],

    "Oh": [
        {},
        {"T1g": "T2g", "T2g": "T1g", "T1u": "T2u", "T2u": "T1u"},
    ],
}

# ============================================================
# 置換適用関数
# ============================================================

def apply_perm(decomp, perm):
    out = {}
    for label, mult in decomp.items():
        new_label = perm.get(label, label)
        out[new_label] = out.get(new_label, 0) + mult
    return out

# ============================================================
# expected と actual の比較（任意性を許容）
# ============================================================

def equivalent_under_permutations(expected, actual, group):
    for perm in ALLOWED_PERMUTATIONS[group]:
        ok = True
        for l in ["s", "p", "d", "f"]:
            if apply_perm(expected[l], perm) != actual[l]:
                ok = False
                break
        if ok:
            return True
    return False

# ============================================================
# テスト本体
# ============================================================

@pytest.mark.parametrize("group", TEST_CASES.keys())
def test_spdf(group):
    result = decompose_spdf(group, pg)
    expected = TEST_CASES[group]
    assert equivalent_under_permutations(expected, result, group)
