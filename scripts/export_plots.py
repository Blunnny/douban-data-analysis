import plotly.io as pio
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def export_plot_to_html(fig, filename, title=None, include_plotlyjs='cdn'):
    """
    导出Plotly图表为HTML文件
    
    Args:
        fig: Plotly图表对象
        filename: 输出文件名
        title: 图表标题（可选）
        include_plotlyjs: 是否包含plotly.js库，可选值：
            - True: 包含完整的plotly.js库
            - 'cdn': 使用CDN加载plotly.js
            - False: 不包含plotly.js
    """
    # 确保输出目录存在
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output_html')
    os.makedirs(output_dir, exist_ok=True)
    
    # 设置完整的输出路径
    output_path = os.path.join(output_dir, filename)
    
    # 如果提供了标题，更新图表的布局
    if title:
        fig.update_layout(title=title)
    
    # 导出为HTML文件
    pio.write_html(
        fig,
        output_path,
        include_plotlyjs=include_plotlyjs,
        full_html=False,
        config={'displayModeBar': True, 'scrollZoom': True}
    )
    print(f"图表已导出到: {output_path}")

def export_multiple_plots(plots_data):
    """
    批量导出多个图表
    
    Args:
        plots_data: 包含图表信息的列表，每个元素应该是一个字典，包含：
            - fig: Plotly图表对象
            - filename: 输出文件名
            - title: 图表标题（可选）
    """
    # 创建一个index.html文件，包含所有图表的链接
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output_html')
    os.makedirs(output_dir, exist_ok=True)
    
    index_content = ["<!DOCTYPE html>", "<html>", "<head>",
                    "<title>数据可视化图表索引</title>",
                    "<style>",
                    "body { font-family: Arial, sans-serif; margin: 20px; }",
                    ".plot-list { list-style: none; padding: 0; }",
                    ".plot-list li { margin: 10px 0; }",
                    ".plot-list a { text-decoration: none; color: #2196F3; }",
                    ".plot-list a:hover { text-decoration: underline; }",
                    "</style>",
                    "</head>",
                    "<body>",
                    "<h1>数据可视化图表索引</h1>",
                    "<ul class='plot-list'>"]
    
    # 导出每个图表并添加到索引中
    for plot_data in plots_data:
        fig = plot_data['fig']
        filename = plot_data['filename']
        title = plot_data.get('title', filename)
        
        # 导出图表
        export_plot_to_html(fig, filename, title, include_plotlyjs='cdn')
        
        # 添加到索引
        index_content.append(f'<li><a href="{filename}">{title}</a></li>')
    
    index_content.extend(["</ul>", "</body>", "</html>"])
    
    # 写入索引文件
    index_path = os.path.join(output_dir, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_content))
    print(f"索引页面已创建: {index_path}")

# 使用示例
if __name__ == "__main__":
    # 创建示例图表
    fig1 = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 5, 6])])
    fig2 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 5, 6])])
    
    # 批量导出示例
    plots_data = [
        {'fig': fig1, 'filename': 'bar_chart.html', 'title': '示例柱状图'},
        {'fig': fig2, 'filename': 'line_chart.html', 'title': '示例折线图'}
    ]
    export_multiple_plots(plots_data) 