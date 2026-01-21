# 05 | Git / PyCharm / Docker 同步踩坑与建议（你已经踩过一次）

## A. 发生过什么

你用 PyCharm 远程解释器/部署时：
- 本地项目里（某些文件）是空的/损坏的
- PyCharm 自动同步（Upload changed files...）把空文件覆盖到了容器
- 导致容器里的脚本也被“清空”

## B. 立刻的防护建议（强烈建议）

### 1) 禁用自动上传

在 PyCharm：
`Settings -> Build, Execution, Deployment -> Deployment -> Options`

把：
- “自动将更改的文件上传到默认服务器” 设为 **从不**（Never）

### 2) 开启“上传前确认/提示”

同一页面里：
- 勾选 “确认上传文件” 或 “在有更新的文件情况下上传时发出警告”

### 3) 只用 Git 做“保底”

每次一个里程碑：
```bash
git status
git add -A
git commit -m "msg"
git tag v0.x-xxx
```

## C. 你问到的：为什么 PyCharm 里看见路径变成 /tmp/...

这是 PyCharm 运行配置/远程解释器的一种常见行为：
- IDE 会把项目同步到一个临时目录运行（如 /tmp/xxx）
- 如果“映射（Mappings）”没对上，就会出现“找不到 /tmp/.../crop-ai/src/...”

解决思路：
- 要么用 Docker 解释器直接指向容器里的真实路径（/workspace/crop-ai）
- 要么把 Deployment 的 Mappings 映射到 /workspace/crop-ai
- 最简单：容器内直接运行脚本（终端里跑），IDE 只编辑，不自动同步

## D. “加号里没有 Docker 选项”是正常的

你截图的那个加号是 **Deployment（SFTP/FTP/WebDAV）**，它不是 Docker。  
Docker 要在：
- `Settings -> Build, Execution, Deployment -> Docker` 里配置

Deployment 只管“文件上传”，Docker 只管“容器连接”。
