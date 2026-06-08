class CrystalPointGroupMN:
    """32点群の各共役類の (m, n, parity) を保持するクラス。
    θ = 2πm/n は正則部の回転角。parity = +1 (正則) / -1 (不正則)。
    不正則操作 g の proper 部: i·g ∈ SO(3) の回転角を (m,n) に格納。"""

    SCHOENFLIES_TO_GAP_EXPR = {
        "C1":  '"C1"',
        "Ci":  '"C2"',
        "C2":  '"C2"',
        "Cs":  '"C2"',
        "C2h": '"V4"',
        "D2":  '"V4"',
        "C2v": '"V4"',
        "D2h": '"2^3"',
        "C4":  '"C4"',
        "S4":  '"C4"',
        "C4h": 'DirectProduct(CyclicGroup(4),CyclicGroup(2))',
        "D4":  '"D8"',
        "C4v": '"D8"',
        "D2d": '"D8"',
        "D4h": 'DirectProduct(DihedralGroup(8),CyclicGroup(2))',
        "C3":  '"C3"',
        "C3i": '"C6"',
        "D3":  '"S3"',
        "C3v": '"S3"',
        "D3d": '"D12"',
        "C6":  '"C6"',
        "C3h": '"C6"',
        "C6h": 'DirectProduct(CyclicGroup(6),CyclicGroup(2))',
        "D6":  '"D12"',
        "C6v": '"D12"',
        "D3h": '"D12"',
        "D6h": 'DirectProduct(DihedralGroup(12),CyclicGroup(2))',
        "T":   '"a4"',
        "Th":  'DirectProduct(AlternatingGroup(4),CyclicGroup(2))',
        "O":   '"Symm(4)"',
        "Td":  '"Symm(4)"',
        "Oh":  '"2xSymm(4)"',
    }

    # (m, n, parity): θ=2πm/n は正則部の回転角。parity=+1 正則, -1 不正則。
    # 不正則操作の proper 部 (i·g の回転角):
    #   i    → E    (0,1)   σ,σv,σd,σh → C2 (1,2)
    #   S4   → C4³  (1,4)   S6,S6⁵     → C3 (1,3)
    #   S3   → C6⁵  (1,6)   S3⁵        → C6 (1,6)
    data = {

        # C1: order=1, classes=1
        "C1": [
            (0, 1, +1),  # E
        ],

        # Ci: order=2, classes=2
        "Ci": [
            (0, 1, +1),  # E
            (0, 1, -1),  # i
        ],

        # C2: order=2, classes=2
        "C2": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
        ],

        # Cs: order=2, classes=2
        "Cs": [
            (0, 1, +1),  # E
            (1, 2, -1),  # σ
        ],

        # C2h: order=4, classes=4
        "C2h": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
            (0, 1, -1),  # i
            (1, 2, -1),  # σh
        ],

        # D2: order=4, classes=4
        "D2": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2(z)
            (1, 2, +1),  # C2(x)
            (1, 2, +1),  # C2(y)
        ],

        # C2v: order=4, classes=4
        "C2v": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
            (1, 2, -1),  # σv
            (1, 2, -1),  # σv'
        ],

        # D2h: order=8, classes=8
        "D2h": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2(z)
            (1, 2, +1),  # C2(y)
            (1, 2, +1),  # C2(x)
            (0, 1, -1),  # i
            (1, 2, -1),  # σ(xy)
            (1, 2, -1),  # σ(xz)
            (1, 2, -1),  # σ(yz)
        ],

        # C4: order=4, classes=4
        "C4": [
            (0, 1, +1),  # E
            (1, 4, +1),  # C4
            (1, 2, +1),  # C2
            (3, 4, +1),  # C4³
        ],

        # S4: order=4, classes=4
        "S4": [
            (0, 1, +1),  # E
            (1, 4, -1),  # S4   (proper部=C4³→(1,4))
            (1, 2, +1),  # C2
            (1, 4, -1),  # S4³  (proper部=C4→(1,4))
        ],

        # C4h: order=8, classes=8
        "C4h": [
            (0, 1, +1),  # E
            (1, 4, +1),  # C4
            (1, 2, +1),  # C2
            (3, 4, +1),  # C4³
            (0, 1, -1),  # i
            (1, 4, -1),  # S4³  (proper部=C4→(1,4))
            (1, 2, -1),  # σh
            (1, 4, -1),  # S4   (proper部=C4³→(1,4))
        ],

        # D4: order=8, classes=5
        "D4": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
            (1, 4, +1),  # 2C4
            (1, 2, +1),  # 2C2'
            (1, 2, +1),  # 2C2''
        ],

        # C4v: order=8, classes=5
        "C4v": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
            (1, 4, +1),  # 2C4
            (1, 2, -1),  # 2σv
            (1, 2, -1),  # 2σd
        ],

        # D2d: order=8, classes=5
        "D2d": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
            (1, 4, -1),  # 2S4
            (1, 2, +1),  # 2C2'
            (1, 2, -1),  # 2σd
        ],

        # D4h: order=16, classes=10
        "D4h": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
            (1, 4, +1),  # 2C4
            (1, 2, +1),  # 2C2'
            (1, 2, +1),  # 2C2''
            (0, 1, -1),  # i
            (1, 2, -1),  # σh
            (1, 4, -1),  # 2S4
            (1, 2, -1),  # 2σv
            (1, 2, -1),  # 2σd
        ],

        # C3: order=3, classes=3
        "C3": [
            (0, 1, +1),  # E
            (1, 3, +1),  # C3
            (2, 3, +1),  # C3²
        ],

        # C3i (S6): order=6, classes=6
        "C3i": [
            (0, 1, +1),  # E
            (1, 3, +1),  # C3
            (2, 3, +1),  # C3²
            (0, 1, -1),  # i
            (1, 3, -1),  # S6⁵  (proper部=C3→(1,3))
            (1, 3, -1),  # S6   (proper部=C3²→(1,3))
        ],

        # D3: order=6, classes=3
        "D3": [
            (0, 1, +1),  # E
            (1, 3, +1),  # 2C3
            (1, 2, +1),  # 3C2
        ],

        # C3v: order=6, classes=3
        "C3v": [
            (0, 1, +1),  # E
            (1, 3, +1),  # 2C3
            (1, 2, -1),  # 3σv
        ],

        # D3d: order=12, classes=6
        "D3d": [
            (0, 1, +1),  # E
            (0, 1, -1),  # i
            (1, 3, +1),  # 2C3
            (1, 3, -1),  # 2S6
            (1, 2, +1),  # 3C2
            (1, 2, -1),  # 3σd
        ],

        # C6: order=6, classes=6
        "C6": [
            (0, 1, +1),  # E
            (1, 6, +1),  # C6
            (1, 3, +1),  # C3
            (1, 2, +1),  # C2
            (2, 3, +1),  # C3²
            (5, 6, +1),  # C6⁵
        ],

        # C3h: order=6, classes=6
        "C3h": [
            (0, 1, +1),  # E
            (1, 2, -1),  # σh
            (1, 3, +1),  # C3
            (1, 6, -1),  # S3⁵  (proper部=C6→(1,6))
            (2, 3, +1),  # C3²
            (1, 6, -1),  # S3   (proper部=C6⁵→(1,6))
        ],

        # C6h: order=12, classes=12
        "C6h": [
            (0, 1, +1),  # E
            (1, 6, +1),  # C6
            (1, 3, +1),  # C3
            (1, 2, +1),  # C2
            (2, 3, +1),  # C3²
            (5, 6, +1),  # C6⁵
            (0, 1, -1),  # i
            (1, 6, -1),  # S3⁵  (proper部=C6→(1,6))
            (1, 3, -1),  # S6⁵  (proper部=C3→(1,3))
            (1, 2, -1),  # σh
            (1, 3, -1),  # S6   (proper部=C3²→(1,3))
            (1, 6, -1),  # S3   (proper部=C6⁵→(1,6))
        ],

        # D6: order=12, classes=6
        "D6": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
            (1, 6, +1),  # 2C6
            (1, 3, +1),  # 2C3
            (1, 2, +1),  # 3C2'
            (1, 2, +1),  # 3C2''
        ],

        # C6v: order=12, classes=6
        "C6v": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
            (1, 6, +1),  # 2C6
            (1, 3, +1),  # 2C3
            (1, 2, -1),  # 3σv
            (1, 2, -1),  # 3σd
        ],

        # D3h: order=12, classes=6
        "D3h": [
            (0, 1, +1),  # E
            (1, 2, -1),  # σh
            (1, 3, +1),  # 2C3
            (1, 6, -1),  # 2S3
            (1, 2, +1),  # 3C2
            (1, 2, -1),  # 3σv
        ],

        # D6h: order=24, classes=12
        "D6h": [
            (0, 1, +1),  # E
            (1, 2, +1),  # C2
            (1, 6, +1),  # 2C6
            (1, 3, +1),  # 2C3
            (1, 2, +1),  # 3C2'
            (1, 2, +1),  # 3C2''
            (0, 1, -1),  # i
            (1, 2, -1),  # σh
            (1, 6, -1),  # 2S3
            (1, 3, -1),  # 2S6
            (1, 2, -1),  # 3σd
            (1, 2, -1),  # 3σv
        ],

        # T (23): order=12, classes=4
        "T": [
            (0, 1, +1),  # E
            (1, 2, +1),  # 3C2
            (1, 3, +1),  # 4C3
            (2, 3, +1),  # 4C3²
        ],

        # Th (m3̄): order=24, classes=8
        "Th": [
            (0, 1, +1),  # E
            (1, 2, +1),  # 3C2
            (1, 3, +1),  # 4C3
            (2, 3, +1),  # 4C3²
            (0, 1, -1),  # i
            (1, 2, -1),  # 3σh
            (1, 3, -1),  # 4S6⁵  (proper部=C3→(1,3))
            (1, 3, -1),  # 4S6   (proper部=C3²→(1,3))
        ],

        # O (432): order=24, classes=5
        "O": [
            (0, 1, +1),  # E
            (1, 2, +1),  # 3C2 (= C4²)
            (1, 3, +1),  # 8C3
            (1, 4, +1),  # 6C4
            (1, 2, +1),  # 6C2'
        ],

        # Td (4̄3m): order=24, classes=5
        "Td": [
            (0, 1, +1),  # E
            (1, 2, +1),  # 3C2
            (1, 3, +1),  # 8C3
            (1, 4, -1),  # 6S4
            (1, 2, -1),  # 6σd
        ],

        # Oh (m3̄m): order=48, classes=10
        "Oh": [
            (0, 1, +1),  # E
            (0, 1, -1),  # i
            (1, 2, +1),  # 3C2 (= C4²)
            (1, 2, -1),  # 3σh
            (1, 3, +1),  # 8C3
            (1, 3, -1),  # 8S6
            (1, 4, +1),  # 6C4
            (1, 4, -1),  # 6S4
            (1, 2, +1),  # 6C2'
            (1, 2, -1),  # 6σd
        ],
    }

    def get_gap_expr(self, name: str) -> str:
        if name not in self.SCHOENFLIES_TO_GAP_EXPR:
            raise ValueError(f"Point group '{name}' not in SCHOENFLIES_TO_GAP_EXPR.")
        return self.SCHOENFLIES_TO_GAP_EXPR[name]

    def get_mn(self, name: str):
        if name not in self.data:
            raise ValueError(f"Point group '{name}' not registered.")
        return self.data[name]

    def has_group(self, name: str) -> bool:
        return name in self.data

    def list_groups(self):
        return sorted(self.data.keys())
