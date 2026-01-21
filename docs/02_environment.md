# 02 | 环境与版本锁定（为什么你必须 pin 版本）

你已经踩过几次典型的“科学 Python 生态坑”：

- numpy 新版本（2.x） → pandas / geopandas 二进制 ABI 不匹配
- shapely 2.x → geopandas 0.9 里一些 API/行为变化导致导入失败
- fiona 新版本 → geopandas 0.9 期望的接口不一致

## A. 你已验证可用的版本组合（建议写进 requirements.lock）

- Python 3.10.12
- cropharvest==0.7.0
- numpy==1.26.4
- pandas==1.5.3
- geopandas==0.9.0
- shapely==1.8.5.post1
- fiona==1.8.22
- xarray==0.19.0

## B. 一条命令“回到稳定环境”（建议）

> 在 venv 里执行：

```bash
pip install -U "pip<24.3" "setuptools<81" wheel
pip install   cropharvest==0.7.0   "numpy==1.26.4"   "pandas==1.5.3"   "geopandas==0.9.0"   "shapely==1.8.5.post1"   "fiona==1.8.22"   "xarray==0.19.0"   "scikit-learn>=1.0"   matplotlib
```

## C. Dockerfile 里要不要 `pip install --upgrade pip setuptools wheel`？

建议：**可以升级，但要“带上上限”**，避免未来版本 breaking change：

```dockerfile
RUN pip install -U "pip<24.3" "setuptools<81" wheel
```

这样既能修复旧 pip 的问题，又不会升级到过新导致奇怪不兼容。
