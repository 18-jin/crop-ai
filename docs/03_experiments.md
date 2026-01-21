# 03 | 实验脚本说明（exp_01 / exp_02 / exp_03 / the-18）

本目录：`src/experiments/`

## exp_01_load_cropharvest.py

目的：确认数据目录结构正确、能离线加载 benchmark datasets。

关键点：
- `download=False`（不走网络）
- 打印任务（Task）列表，确认包含 Togo / China 等

## exp_02_togo_demo.py

目的：复刻官方 demo 的“训练 + 测试评估”流程（RandomForest baseline）。

步骤：
1) `create_benchmark_datasets(DATA_DIR, download=False)`
2) 取 `togo_dataset = datasets[-1]`
3) `as_array(flatten_x=True)` 得到 (N,216)
4) 训练 RandomForest
5) 遍历 `togo_dataset.test_data(...)` 得到测试预测并评估

输出：AUC / F1 / IoU / num_samples

## exp_03_plot_ndvi.py

目的：把 12 个月 NDVI 曲线画出来，直观理解“作物 vs 非作物”。

建议输出：
- 保存 `ndvi_togo.png`（因为容器里不一定能弹窗）
- 同时打印 `BANDS` 确认 NDVI 在第 18 个 band

## the-18.py

目的：确认“18 个 EO 特征”的来源与顺序（来自 `cropharvest.bands.BANDS`）。

注意：
- `togo.normalizing_dict` 里只有 `mean/std`（这不是特征名）
- 特征名应从 `cropharvest.bands import BANDS` 获取
