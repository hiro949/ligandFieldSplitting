# Crystal Point Group Decomposition (GAP + SO(3) Characters)

このプロジェクトは、**結晶点群（32点群）に対する s/p/d/f 軌道の既約分解**を  
**GAP の CharacterTable** と **SO(3) の指標 χₗ(m,n)** を用いて  
**完全自動で計算する Python/Sage スクリプト**です。

---

## 🎯 目的

- 結晶点群の **共役類ごとの回転角 (m,n)** をデータベース化する  
- GAP の **CharacterTable(name)** から  
  - 共役類サイズ |Cⱼ|  
  - 既約表現の指標 χΓ(Cⱼ)  
  を自動取得する  
- SO(3) の指標 χₗ(Cⱼ) と内積を取り、  
  **s, p, d, f の既約分解を自動計算する**

---

## 📂 ディレクトリ構成

---

## 使い方

### 依存パッケージのダウンロード

```bash
make download
```

GAP の CharacterTable Library（ctbllib）・AtlasRep・utils を `downloads/` に取得します。

### Docker イメージのビルド

```bash
make build
```

### 実行

```bash
make run GROUP=<点群名>
```

例: `make run GROUP=Oh`

### その他

|コマンド|説明|
|---|---|
|`make shell`|Sage インタラクティブシェルを起動|
|`make gap`|GAP インタラクティブシェルを起動|
|`make test`|pytest でテストを実行|

---

## 依存ファイル

以下の3パッケージは `make download` で自動取得されます。

| パッケージ | 用途 |
| --- | --- |
| ctbllib | GAP の Character Table Library |
| atlasrep | GAP の Atlas of Group Representations |
| utils | GAP ユーティリティライブラリ |

Docker ビルド時にコンテナ内へコピーされます。
