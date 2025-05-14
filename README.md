# 豆瓣年轮

基于开源项目[豆伴](https://github.com/doufen-org/tofu)将导出的豆瓣数据分析和可视化来总结个人观影、读书习惯和偏好，呈现一份可视、可读、可反思的精神轨迹。

## 项目结构

```
douban-data-analysis/
├── data/                             # 数据目录
│   ├── raw/                            # 原始数据文件
│   ├── interim/                        # 中间处理数据
│   ├── processed/                      # 最终处理后的数据
│   ├── eda_results/                    # 探索性分析结果
│   └── advanced_analysis_results/      # 高级分析结果
├── notebooks/                        # Jupyter Notebooks
│   ├── 00-setup.ipynb                  # 环境配置和依赖检查
│   ├── 01-data-ingest.ipynb           # 数据导入
│   ├── 02-cleaning.ipynb              # 数据清洗
│   ├── 03-eda.ipynb                   # 探索性数据分析
│   ├── 04-advanced-analysis.ipynb     # 高级数据分析
│   └── 05-visualize.ipynb            # 数据可视化
├── scripts/                          # 工具函数脚本
├── figures/                          # 输出图表
├── requirements.txt                  # Python 依赖
└── README.md                         # 项目说明
```

## 环境设置

1. 创建并激活虚拟环境（推荐）：

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

## 使用说明

1. 将豆瓣导出的数据文件放入 `data/raw/` 目录
2. 按顺序运行 notebooks 目录下的 Jupyter notebooks：
   - `00-setup.ipynb`: 环境配置和依赖检查
   - `01-data-ingest.ipynb`: 数据导入
   - `02-cleaning.ipynb`: 数据清洗
   - `03-eda.ipynb`: 探索性数据分析
   - `04-advanced-analysis.ipynb`: 高级数据分析
   - `05-visualize.ipynb`: 数据可视化
