# Crop-AI × CropHarvest 学习与实验记录（必读）

> 给未来自己的“防迷路文档”  
> 目标：**能复现、能解释、能继续迭代**。

## 📌 目录（Table of Contents）

- [1️⃣ 当前已经跑通什么](#1️⃣-当前已经跑通什么)
- [2️⃣ 目录结构与数据放置](#2️⃣-目录结构与数据放置)
- [3️⃣ CropHarvest 的真实数据流](#3️⃣-cropharvest-的真实数据流)
- [4️⃣ 18 个 EO 特征与 12 个月](#4️⃣-18-个-eo-特征与-12-个月)
- [5️⃣ 为什么输入是 216 维](#5️⃣-为什么输入是-216-维)
- [6️⃣ 已验证的“稳定环境版本”](#6️⃣-已验证的稳定环境版本)
- [7️⃣ 已踩过的坑（不要再踩）](#7️⃣-已踩过的坑不要再踩)
- [8️⃣ 我现在应该从哪里继续学](#8️⃣-我现在应该从哪里继续学)
- [9️⃣ 延伸阅读与笔记](#9️⃣-延伸阅读与笔记)

---

## 1️⃣ 当前已经跑通什么

截至目前（以 `src/experiments/exp_02_togo_demo.py` 为准）：

- ✅ Docker + Python 3.10 + venv 中运行 CropHarvest
- ✅ 使用 PyPI 版本 `cropharvest==0.7.0`
- ✅ 离线加载 Benchmark 数据集（Togo）
- ✅ 训练并评估 RandomForest 基线模型（AUC≈0.85，F1≈0.82）
- ✅ 能从 (N, 12, 18) / (N, 216) 两种形态理解输入

快速验证：
```bash
cd /workspace/crop-ai/src/experiments
python exp_02_togo_demo.py
```

---

## 2️⃣ 目录结构与数据放置

**关键：`data/` 结构必须符合 CropHarvest 预期**（否则它会尝试重新下载）。

```
crop-ai/
├── data/
│   ├── features/
│   │   ├── arrays/              # 训练用 .h5（核心）
│   │   └── normalizing_dict.h5  # 归一化参数
│   ├── test_features/           # 测试集特征
│   └── labels.geojson           # 标签（GeoJSON）
│
└── src/experiments/
    ├── exp_01_load_cropharvest.py
    ├── exp_02_togo_demo.py
    ├── exp_03_plot_ndvi.py
    └── the-18.py
```

---

## 3️⃣ CropHarvest 的真实数据流

一句话版：

> **labels（样本点+标签） → 预处理特征（features/test_features） → Dataset API → 模型训练/评估 → 推理**

更详细解释见：[`docs/01_workflow.md`](docs/01_workflow.md)

---

## 4️⃣ 18 个 EO 特征与 12 个月

最终进入模型的 18 个 band（按包内定义）：

- Sentinel-1（雷达）：VV, VH（2）
- Sentinel-2（光学）：B2, B3, B4, B5, B6, B7, B8, B8A, B9, B11, B12（11）
- ERA5（气候）：temperature_2m, total_precipitation（2）
- SRTM（地形）：elevation, slope（2）
- 派生指数：NDVI（1）

详细解释与直觉见：[`docs/04_ndvi.md`](docs/04_ndvi.md)

---

## 5️⃣ 为什么输入是 216 维

- 时序长度：12（≈ 12 个月）
- 每个时间步特征：18 个 band

所以：`12 × 18 = 216`

- `flatten_x=True` → `(N, 216)`（适合 RandomForest / XGBoost）
- `flatten_x=False` → `(N, 12, 18)`（适合 RNN / Transformer）

---

## 6️⃣ 已验证的“稳定环境版本”

> 这套版本在你当前 Docker 环境中已经跑通。**尽量别乱升级**。

- Python 3.10.12
- cropharvest 0.7.0
- numpy 1.26.4
- pandas 1.5.3
- geopandas 0.9.0
- shapely 1.8.5.post1
- fiona 1.8.22
- xarray 0.19.0
- scikit-learn 1.7.x
- matplotlib 3.10.x（用于画图）

为什么要锁版本见：[`docs/02_environment.md`](docs/02_environment.md)

---

## 7️⃣ 已踩过的坑（不要再踩）

- ❌ `numpy >= 2.0` 触发 pandas / geopandas 二进制不兼容（你踩过）
- ❌ `shapely >= 2.0` 会破坏 `geopandas==0.9.0` 依赖
- ❌ `fiona` 版本过新导致 geopandas 读取异常（你踩过）
- ❌ 让 Dataset 自动 `download=True`：网络/Zenodo 不稳定 → 空文件/坏包
- ❌ PyCharm 远程同步把本地空文件覆盖容器（你踩过）

完整“防坑指南”见：[`docs/05_git_pycharm_sync.md`](docs/05_git_pycharm_sync.md)

---

## 8️⃣ 我现在应该从哪里继续学

推荐顺序：

1) `exp_03_plot_ndvi.py`：把 **Crop vs Non-crop** 的 NDVI 画出来（先“看见”差异）  
2) `the-18.py`：确认 18 个特征定义来自哪里（BANDS）  
3) 扩展：画更多 band（VV/VH、降水、温度）做对比  
4) 做一版 feature importance（RandomForest）理解“模型到底靠什么判断”

---

## 9️⃣ 延伸阅读与笔记

- 工作流：[`docs/01_workflow.md`](docs/01_workflow.md)
- 环境与版本：[`docs/02_environment.md`](docs/02_environment.md)
- 实验脚本说明：[`docs/03_experiments.md`](docs/03_experiments.md)
- NDVI 与物理直觉：[`docs/04_ndvi.md`](docs/04_ndvi.md)
- Git / PyCharm / Docker 同步踩坑：[`docs/05_git_pycharm_sync.md`](docs/05_git_pycharm_sync.md)

---

> 如果你迷路了：  
> `cd src/experiments && python exp_02_togo_demo.py`  
> 只要它还能跑，你就没白走。
