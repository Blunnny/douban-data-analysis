import os
import json
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def export_multiple_plots(plots_data):
    """
    批量导出多个图表
    
    Args:
        plots_data: 包含图表信息的列表，每个元素应该是一个字典，包含：
            - fig: Plotly图表对象
            - filename: 输出文件名
            - title: 图表标题（可选）
    """
    # 创建一个output_html文件夹，包含所有图表的链接
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
        output_path = os.path.join(output_dir, filename)
        pio.write_html(
            fig,
            output_path,
            include_plotlyjs='cdn',
            full_html=False,
            config={'displayModeBar': True, 'scrollZoom': True}
        )
        print(f"图表已导出到: {output_path}")
        
        # 添加到索引
        index_content.append(f'<li><a href="{filename}">{title}</a></li>')
    
    index_content.extend(["</ul>", "</body>", "</html>"])
    
    # 写入索引文件
    index_path = os.path.join(output_dir, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_content))
    print(f"索引页面已创建: {index_path}")

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    # 加载数据
    base_dir = os.path.dirname(os.path.dirname(__file__))
    movies_data = load_json(os.path.join(base_dir, 'data/eda_results/summary_movies_results.json'))
    books_data = load_json(os.path.join(base_dir, 'data/eda_results/summary_books_results.json'))
    games_data = load_json(os.path.join(base_dir, 'data/eda_results/summary_games_results.json'))
    advanced_analysis_results_data = load_json(os.path.join(base_dir, 'data/advanced_analysis_results/advanced_analysis_results.json'))

    plots_data = []

    # 处理电影数据
    for item in movies_data:
        sheet_name = item['sheet_name']
        
        # 创建时间按季度统计
        create_time = item['create_time']
        create_time_df = pd.DataFrame(list(create_time.items()), columns=['季度', '数量'])
        create_time_df['年份'] = create_time_df['季度'].apply(lambda x: x[:4])
        create_time_df['季度'] = create_time_df['季度'].apply(lambda x: x[4:])
        
        fig_create_time = px.bar(
            create_time_df,
            x='季度', y='数量', color='年份',
            title=f"{sheet_name} - 创建时间按季度统计",
            barmode='group'
        )
        plots_data.append({
            'fig': fig_create_time,
            'filename': f'movies_{sheet_name}_create_time.html',
            'title': f'{sheet_name} - 创建时间统计'
        })

        # 导演 Top 5
        director_top_5 = item['director']['top_5']
        director_df = pd.DataFrame(director_top_5)
        fig_director = px.bar(
            director_df,
            x='count', y='director', orientation='h',
            title=f"{sheet_name} - 导演 Top 5"
        )
        fig_director.update_layout(
            yaxis=dict(autorange='reversed'),
            xaxis_title="出现次数",
            yaxis_title="导演"
        )
        plots_data.append({
            'fig': fig_director,
            'filename': f'movies_{sheet_name}_director_top5.html',
            'title': f'{sheet_name} - 导演 Top 5'
        })

        # 演员 Top 5
        actor_top_5 = item['actor']['top_5']
        actor_df = pd.DataFrame(actor_top_5)
        fig_actor = px.bar(
            actor_df,
            x='count', y='actor', orientation='h',
            title=f"{sheet_name} - 演员 Top 5"
        )
        fig_actor.update_layout(
            yaxis=dict(autorange='reversed'),
            xaxis_title="出现次数",
            yaxis_title="演员"
        )
        plots_data.append({
            'fig': fig_actor,
            'filename': f'movies_{sheet_name}_actor_top5.html',
            'title': f'{sheet_name} - 演员 Top 5'
        })

    # 处理图书数据
    for item in books_data:
        sheet_name = item['sheet_name']
        
        # 创建时间按季度统计
        create_time = item['create_time']
        create_time_df = pd.DataFrame(list(create_time.items()), columns=['季度', '数量'])
        create_time_df['年份'] = create_time_df['季度'].apply(lambda x: x[:4])
        create_time_df['季度'] = create_time_df['季度'].apply(lambda x: x[4:])
        
        fig_create_time = px.bar(
            create_time_df,
            x='季度', y='数量', color='年份',
            title=f"{sheet_name} - 创建时间按季度统计",
            barmode='group'
        )
        plots_data.append({
            'fig': fig_create_time,
            'filename': f'books_{sheet_name}_create_time.html',
            'title': f'{sheet_name} - 创建时间统计'
        })

        # 作者 Top 5
        author_top_5 = item['author']['top_5']
        author_df = pd.DataFrame(author_top_5)
        fig_author = px.bar(
            author_df,
            x='count', y='author', orientation='h',
            title=f"{sheet_name} - 作者 Top 5"
        )
        fig_author.update_layout(
            yaxis=dict(autorange='reversed'),
            xaxis_title="出现次数",
            yaxis_title="作者"
        )
        plots_data.append({
            'fig': fig_author,
            'filename': f'books_{sheet_name}_author_top5.html',
            'title': f'{sheet_name} - 作者 Top 5'
        })

        # 出版社 Top 5
        publisher_top_5 = item['publisher']['top_5']
        publisher_df = pd.DataFrame(publisher_top_5)
        fig_publisher = px.bar(
            publisher_df,
            x='count', y='publisher', orientation='h',
            title=f"{sheet_name} - 出版社 Top 5"
        )
        fig_publisher.update_layout(
            yaxis=dict(autorange='reversed'),
            xaxis_title="出现次数",
            yaxis_title="出版社"
        )
        plots_data.append({
            'fig': fig_publisher,
            'filename': f'books_{sheet_name}_publisher_top5.html',
            'title': f'{sheet_name} - 出版社 Top 5'
        })

    # 处理游戏数据
    for item in games_data:
        sheet_name = item['sheet_name']
        
        # 创建时间按年份统计
        create_time = item['create_time']
        create_time_df = pd.DataFrame(list(create_time.items()), columns=['创建时间', '数量'])
        create_time_df['年份'] = create_time_df['创建时间'].apply(lambda x: x[:4])
        
        fig_create_time = px.bar(
            create_time_df,
            x='创建时间', y='数量', color='年份',
            title=f"{sheet_name} - 创建时间按年份",
            barmode='group'
        )
        plots_data.append({
            'fig': fig_create_time,
            'filename': f'games_{sheet_name}_create_time.html',
            'title': f'{sheet_name} - 创建时间统计'
        })

        # 游戏类型 Top 5
        genre_top_5 = item['genre']['top_5']
        genre_df = pd.DataFrame(genre_top_5)
        fig_genre = px.bar(
            genre_df,
            x='count', y='genre', orientation='h',
            title=f"{sheet_name} - 游戏类型 Top 5"
        )
        fig_genre.update_layout(
            yaxis=dict(autorange='reversed'),
            xaxis_title="出现次数",
            yaxis_title="游戏类型"
        )
        plots_data.append({
            'fig': fig_genre,
            'filename': f'games_{sheet_name}_genre_top5.html',
            'title': f'{sheet_name} - 游戏类型 Top 5'
        })

    # 处理高级分析结果
    # 1. 评分趋势
    fig_rating_trends = make_subplots(
        rows=3, cols=1,
        subplot_titles=('电影评分趋势', '图书评分趋势', '游戏评分趋势'),
        vertical_spacing=0.1,
        row_heights=[0.4, 0.4, 0.4]
    )

    for i, (media_type, trends) in enumerate(advanced_analysis_results_data['评分趋势'].items()):
        if trends:
            df_trends = pd.DataFrame(trends)
            fig_rating_trends.add_trace(
                go.Scatter(x=df_trends['创建年份'], y=df_trends['豆瓣评分'],
                          mode='lines+markers', name='豆瓣评分',
                          legendgroup=media_type),
                row=i + 1, col=1
            )
            fig_rating_trends.add_trace(
                go.Scatter(x=df_trends['创建年份'], y=df_trends['我的评分'] * 2,
                          mode='lines+markers', name='我的评分',
                          legendgroup=media_type),
                row=i + 1, col=1
            )

    fig_rating_trends.update_layout(
        title_text='评分趋势分析',
        showlegend=True,
        height=800
    )
    plots_data.append({
        'fig': fig_rating_trends,
        'filename': 'advanced_rating_trends.html',
        'title': '评分趋势分析'
    })

    # 2. 兴趣周期
    fig_interest_cycle = make_subplots(
        rows=3, cols=2,
        subplot_titles=('电影按月份创建数量', '电影按季度创建数量',
                       '图书按月份创建数量', '图书按季度创建数量',
                       '游戏按月份创建数量', '游戏按季度创建数量'),
        vertical_spacing=0.2
    )

    row_col_map = {
        '电影': (1, 1, 1, 2),
        '图书': (2, 1, 2, 2),
        '游戏': (3, 1, 3, 2),
    }

    for media_type, cycle_data in advanced_analysis_results_data['兴趣周期'].items():
        if cycle_data:
            row_month, col_month, row_quarter, col_quarter = row_col_map.get(media_type, (None, None, None, None))
            if '按月份' in cycle_data and row_month is not None:
                df_monthly = pd.DataFrame(list(cycle_data['按月份'].items()), columns=['月份', '数量']).sort_values(by='月份')
                fig_interest_cycle.add_trace(
                    go.Bar(x=df_monthly['月份'], y=df_monthly['数量'],
                          name=f'{media_type} 月份', showlegend=False),
                    row=row_month, col=col_month
                )

            if '按季度' in cycle_data and row_quarter is not None:
                df_quarterly = pd.DataFrame(list(cycle_data['按季度'].items()), columns=['季度', '数量']).sort_values(by='季度')
                fig_interest_cycle.add_trace(
                    go.Bar(x=df_quarterly['季度'], y=df_quarterly['数量'],
                          name=f'{media_type} 季度', showlegend=False),
                    row=row_quarter, col=col_quarter
                )

    fig_interest_cycle.update_layout(title_text='兴趣周期分析', height=900)
    plots_data.append({
        'fig': fig_interest_cycle,
        'filename': 'advanced_interest_cycle.html',
        'title': '兴趣周期分析'
    })

    # 3. 消费速度
    df_consumption_speed = pd.DataFrame(advanced_analysis_results_data['消费速度']).T.reset_index()
    df_consumption_speed.rename(columns={'index': '媒体类型'}, inplace=True)

    fig_consumption_speed = go.Figure()
    fig_consumption_speed.add_trace(
        go.Bar(x=df_consumption_speed['媒体类型'],
               y=df_consumption_speed['平均每年消费数量'],
               name='平均每年消费数量')
    )
    fig_consumption_speed.add_trace(
        go.Bar(x=df_consumption_speed['媒体类型'],
               y=df_consumption_speed['平均每季度消费数量'],
               name='平均每季度消费数量')
    )
    fig_consumption_speed.update_layout(title='平均消费速度', yaxis_title='数量')
    plots_data.append({
        'fig': fig_consumption_speed,
        'filename': 'advanced_consumption_speed.html',
        'title': '平均消费速度分析'
    })

    # 导出所有图表
    export_multiple_plots(plots_data)

if __name__ == "__main__":
    main() 