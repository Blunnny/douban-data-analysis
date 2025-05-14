import json
import sys
from pathlib import Path

def clean_notebook(notebook_path):
    """清理 Jupyter notebook 的输出结果"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # 保存原始文件大小
    original_size = Path(notebook_path).stat().st_size / (1024 * 1024)  # MB
    
    # 清理每个单元格的输出
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            cell['outputs'] = []
            cell['execution_count'] = None
    
    # 保存清理后的 notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)
    
    # 计算新文件大小
    new_size = Path(notebook_path).stat().st_size / (1024 * 1024)  # MB
    
    print(f"清理完成！")
    print(f"原始文件大小: {original_size:.2f} MB")
    print(f"清理后文件大小: {new_size:.2f} MB")
    print(f"减小了: {original_size - new_size:.2f} MB ({((original_size - new_size) / original_size * 100):.1f}%)")

if __name__ == '__main__':
    notebook_path = 'notebooks/05-visualization.ipynb'
    clean_notebook(notebook_path) 