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

## 依存ファイル

`ctbllib-1.3.11.tar.gz` は GAP の Character Table Library です。  
以下のページから手動でダウンロードし、プロジェクトルートに配置してください。

[https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/](https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/)

Docker ビルド時にコンテナ内へコピーされ、ワークディレクトリには残りません。
