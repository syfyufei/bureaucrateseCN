import pandas as pd
from pathlib import Path
from tqdm import tqdm
from bureaucratese.analyzer import BureaucrateseAnalyzer
from bureaucratese.bert_analyzer import BertBureaucrateseAnalyzer

def analyze_hknews_full(file_path, checkpoint_interval=1000):
    """分析香港新闻数据集中所有新闻的官方话语浓度
    
    Args:
        file_path (str): parquet文件路径
        checkpoint_interval (int): 每处理多少条数据保存一次checkpoint
    
    Returns:
        pd.DataFrame: 包含分析结果的数据框
    """
    # 读取parquet文件
    print("正在读取新闻数据...")
    df = pd.read_parquet(file_path)
    
    # 确保数据包含所需的列
    if 'content_simplified' not in df.columns:
        raise ValueError("数据集中缺少'content_simplified'列")
    
    # 添加年份列（假设数据中有日期列，需要根据实际数据调整）
    if 'date' in df.columns:
        df['year'] = pd.to_datetime(df['date']).dt.year
    else:
        raise ValueError("数据集中缺少日期列")
    
    # 初始化分析器
    print("初始化分析器...")
    analyzer = BureaucrateseAnalyzer()
    bert_analyzer = BertBureaucrateseAnalyzer()
    
    # 检查是否存在checkpoint文件
    checkpoint_path = Path('analysis_checkpoint.csv')
    start_idx = 0
    
    if checkpoint_path.exists():
        print("发现checkpoint文件，从断点处继续...")
        checkpoint_df = pd.read_csv(checkpoint_path)
        # 更新已处理的数据
        for col in ['basic_density', 'weighted_density', 'semantic_density', 'official_words']:
            df.loc[checkpoint_df.index, col] = checkpoint_df[col]
        start_idx = len(checkpoint_df)
    else:
        # 初始化新的列
        df['basic_density'] = 0.0
        df['weighted_density'] = 0.0
        df['semantic_density'] = 0.0
        df['official_words'] = ''
    
    # 显示总体进度条
    print("开始分析所有新闻...")
    total_samples = len(df)
    remaining_samples = total_samples - start_idx
    
    # 批量处理数据
    batch_size = 100  # 每批处理的数据量
    
    try:
        with tqdm(total=remaining_samples, desc="处理进度", initial=start_idx) as pbar:
            for idx in range(start_idx, total_samples, batch_size):
                end_idx = min(idx + batch_size, total_samples)
                batch = df.iloc[idx:end_idx]
                
                for batch_idx, row in batch.iterrows():
                    try:
                        content = row['content_simplified']
                        
                        # 处理空值
                        if pd.isna(content) or content is None:
                            print(f"警告：第{batch_idx}行的content_simplified为空")
                            continue
                        
                        # 分析官方话语浓度
                        basic_result = analyzer.analyze_text(content)
                        weighted_result = analyzer.analyze_text_weighted(content)
                        semantic_result = bert_analyzer.calculate_semantic_density(content)
                        
                        # 更新数据框
                        df.at[batch_idx, 'basic_density'] = basic_result['density']
                        df.at[batch_idx, 'weighted_density'] = weighted_result['weighted_density']
                        df.at[batch_idx, 'semantic_density'] = semantic_result['semantic_density']
                        df.at[batch_idx, 'official_words'] = ', '.join(basic_result['official_words'])
                        
                        pbar.update(1)
                    except Exception as e:
                        print(f"处理第{batch_idx}行时出错：{str(e)}")
                        continue
                
                # 定期保存checkpoint
                if (idx + batch_size - start_idx) % checkpoint_interval == 0:
                    checkpoint_df = df.iloc[:end_idx].copy()
                    checkpoint_df.to_csv(checkpoint_path, index=True, encoding='utf-8')
                    print(f"\nCheckpoint已保存到{checkpoint_path}")
    
    except KeyboardInterrupt:
        print("\n检测到用户中断，保存当前进度...")
        checkpoint_df = df.iloc[:idx].copy()
        checkpoint_df.to_csv(checkpoint_path, index=True, encoding='utf-8')
        print(f"进度已保存到{checkpoint_path}")
        return df
    
    # 保存最终结果
    output_path = Path('hknews_full_analysis_results.csv')
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"\n分析结果已保存到 {output_path}")
    
    # 清理checkpoint文件
    if checkpoint_path.exists():
        checkpoint_path.unlink()
        print("已清理checkpoint文件")
    
    return df

if __name__ == '__main__':
    # 设置输入文件路径
    input_file = '/Users/adrian/Desktop/HKNews/final_data/hknews_1995_2024_complete_simplified.parquet'
    
    # 运行分析
    results = analyze_hknews_full(input_file)
    
    # 打印摘要统计
    print("\n年度官方话语浓度统计：")
    summary = results.groupby('year')[
        ['basic_density', 'weighted_density', 'semantic_density']
    ].mean()
    print(summary)