# 01 | CropHarvest 的真实工作流（你现在正在跑的那条）

你现在跑通的是 **CropHarvest 的“离线基准工作流”**：数据已经被预处理成特征文件（.h5），你只是在本地加载它们做训练/评估。

## A. 你现在用的三类“必须文件”

在 `crop-ai/data/` 下：

1) `labels.geojson`
- 含样本点（经纬度/几何信息）+ 标签（crop / non-crop 等）
- 由 `geopandas.read_file()` 读取

2) `features/`
- 训练/验证使用的特征（`arrays/*.h5`）
- 以及 `normalizing_dict.h5`（归一化参数）

3) `test_features/`
- 测试集特征（用于 demo 里 test_data 评估）

> 如果这些缺失，`create_benchmark_datasets(..., download=True)` 会尝试从网络下载。你这里推荐 **download=False**。

## B. 模型拿到的 X/y 是什么

`X, y = dataset.as_array(flatten_x=True)`

- `y`：0/1（二分类；1 通常表示 “目标作物/作物”）
- `X`：每个样本一条 12×18 的时间序列特征

### 两种形态

- `flatten_x=True`：`(N, 216)` → 传统 ML（RandomForest）
- `flatten_x=False`：`(N, 12, 18)` → 时序模型（RNN/Transformer）

## C. “在线版本”工作流是什么（你暂时没走）

CropHarvest 也支持从 Earth Engine 获取 EO 数据并做工程化特征（`cropharvest/eo/*`），但这需要：

- earthengine-api（`pip install earthengine-api`）
- GEE 登录/授权
- 网络与配额

你当前阶段先别硬怼这条路：离线基准 + 可视化理解更划算。
