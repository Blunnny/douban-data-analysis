# 豆瓣年轮

基于开源项目豆伴（https://github.com/doufen-org/tofu）将导出的豆瓣据数据分析和可视化来总结个人观影、读书习惯和偏好，呈现一份可视、可读、可反思的精神轨迹。

## 项目结构

```
vediodata/
├── data/                               # 原始与处理后数据
│   ├── raw/                            # 原始 Excel 文件
│   └── processed/                      # 清洗、转换后的 CSV/Parquet 等
├── notebooks/                          # Jupyter Notebooks
│   ├── 00-setup.ipynb                  # 环境与依赖说明
│   ├── 01-data-ingest.ipynb            # 数据导入
│   ├── 02-cleaning.ipynb               # 数据清洗与预处理
│   ├── 03-eda.ipynb                    # 探索性数据分析
│   └── 04-visualization.ipynb          # 可视化与高级分析
├── scripts/                            # 如需封装为脚本的工具函数
├── figures/                            # 输出图表
├── requirements.txt                    # Python 依赖
└── README.md                           # 项目说明
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

1. 将豆瓣导出的 Excel 文件放入 `data/raw/` 目录
2. 按顺序运行 notebooks 目录下的 Jupyter notebooks：
   - `00-setup.ipynb`: 环境配置和依赖检查
   - `01-data-ingest.ipynb`: 数据导入
   - `02-cleaning.ipynb`: 数据清洗
   - `03-eda.ipynb`: 探索性数据分析
   - `04-visualization.ipynb`: 数据可视化

## 数据来源

数据来源于豆瓣个人书影音记录导出功能。请确保数据格式符合预期，包含必要的字段信息。
