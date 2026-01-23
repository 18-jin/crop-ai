# Experiment 05–06: Crop vs Non-Crop Temporal NDVI Dynamics

> 本实验聚焦于 **作物（Crop）与非作物（Non-crop）** 在时间维度上的 EO 特征差异，  
> 尤其是 **NDVI 及其变化率（ΔNDVI）** 如何体现人类农业活动。

---

## 1. 实验目的

在完成 Togo 基准任务后（RandomForest AUC ≈ 0.85），
我们希望回答一个更“物理”的问题：

> **模型究竟是通过什么时序特征来区分作物与非作物？**

本实验从三个角度展开：

1. Feature × Time 的均值响应（热力图）
2. Crop vs Non-crop 的对比
3. NDVI 的 **变化率（ΔNDVI）** 分析

---

## 2. 数据与设置

- 数据集：CropHarvest Togo benchmark
- 样本数量：
  - Crop: 2299
  - Non-crop: 1843
- 特征维度：
  - 时间步：12（月）
  - EO 特征：18
- 输入形状：
  ```text
  X: (4142, 12, 18)
  y: (4142,)

3. Experiment 05：Feature × Time Mean Heatmap
3.1 方法

对 Crop 与 Non-crop 样本分别计算：

mean over samples → (12 × 18)


并绘制 Feature × Month 的二维热力图。

输出文件：

feature_time_heatmap_togo_crop.png

feature_time_heatmap_togo_non_crop.png

3.2 主要观察
（1）静态特征（Elevation / Slope）

在时间维度上保持常数

对 Crop / Non-crop 区分度有限

更偏向 空间约束特征

（2）光学与雷达波段（B2–B12, VV/VH）

两类区域均存在季节性变化

但 Crop 区域的响应幅度更大

尤其在生长季（M4–M7）更明显

（3）NDVI（均值层面）

Crop 与 Non-crop 在 绝对 NDVI 值 上差异并不总是显著

单纯使用 NDVI 均值容易产生混淆

➡️ 这提示我们：
区分信息可能隐藏在“变化过程”而非“静态值”中

4. Experiment 06：NDVI Change Rate（ΔNDVI）
4.1 定义

对 NDVI 做时间一阶差分：

ΔNDVI(t) = NDVI(t) - NDVI(t-1)


该量刻画的是 植被状态的变化速度，而非绝对水平。

4.2 结果可视化

输出图像：

delta_ndvi_togo_crop_vs_non_crop.png

图中展示了 Crop 与 Non-crop 的 月际 NDVI 变化率曲线。

4.3 核心发现（非常关键）
✔ 作物区域（Crop）

生长阶段：ΔNDVI 快速上升

收割 / 枯萎阶段：ΔNDVI 急剧下降

整体呈现：

高振幅、陡峭、脉冲式变化

✔ 非作物区域（Non-crop）

变化趋势存在，但幅度明显更小

更接近：

平滑、连续、气候驱动的自然变化

5. 农学与遥感解释
现象	解释
Crop ΔNDVI 更陡	人类强干预（播种 / 施肥 / 收割）
Non-crop ΔNDVI 平缓	自然植被或非植被覆盖
均值 NDVI 区分力有限	静态绿度不足以识别农业活动
ΔNDVI 区分力强	捕捉“生长–收割”时间结构
6. 对模型的意义

本实验揭示了一个关键事实：

模型真正利用的不是“是否更绿”，
而是“绿得有多快，退得有多狠”。

这也解释了：

RandomForest 在不使用深度模型的情况下

仍能在 Togo 任务上取得较高 AUC

因为：

决策树天然擅长捕捉 突变与斜率

7. 小结

NDVI 均值 ≠ 最优判别特征

NDVI 的时间变化率（ΔNDVI）是作物识别的核心信号之一

农业活动在时间维度上表现为：

高频、高幅度、非平稳过程
