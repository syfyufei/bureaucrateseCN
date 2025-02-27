import os
import pandas as pd
import jieba
from pathlib import Path

class BureaucrateseAnalyzer:
    def __init__(self, custom_dict_path=None, use_bert=False):
        self.official_words = set()
        self.word_types = {}
        self.word_frequencies = {}
        self.use_bert = use_bert
        self._load_dictionary(custom_dict_path)
        
        if self.use_bert:
            from .bert_analyzer import BertBureaucrateseAnalyzer
            self.bert_analyzer = BertBureaucrateseAnalyzer()

    def _load_dictionary(self, custom_dict_path=None):
        if custom_dict_path is None:
            # 使用默认的词典文件
            package_dir = Path(__file__).parent
            custom_dict_path = package_dir / '../data/RAWdataset.csv'

        df = pd.read_csv(custom_dict_path)
        # 只保留官方话语的词
        official_words_df = df[df['typeOfWord'] == '官方话语']
        self.official_words = set(official_words_df['Word'].tolist())
        
        # 保存词语类型信息
        self.word_types = dict(zip(df['Word'], df['typeOfWord']))
        
        # 将词典添加到jieba分词器中
        for word in df['Word']:
            jieba.add_word(word)
        
        # 将词典添加到jieba分词器中，并设置词频权重
        for word, freq in zip(df['Word'], df['Frequency']):
            jieba.add_word(word, freq=freq)
        
        # 保存词频信息
        self.word_frequencies = dict(zip(df['Word'], df['Frequency']))

    def analyze_text(self, text):
        """分析文本中的官方话语密度"""
        if not text.strip():
            return {
                'density': 0.0,
                'official_words': [],
                'total_words': 0,
                'official_word_count': 0
            }

        # 使用结巴分词
        words = [word for word in jieba.cut(text) if word.strip()]
        total_words = len(words)
        
        # 统计官方话语词汇
        official_words_found = [word for word in words if word in self.official_words]
        official_word_count = len(official_words_found)
        
        # 计算密度
        density = official_word_count / total_words if total_words > 0 else 0
        
        return {
            'density': density,
            'official_words': official_words_found,
            'total_words': total_words,
            'official_word_count': official_word_count
        }

    def get_word_type(self, word):
        """获取词语的类型（官方话语/日常话语）"""
        return self.word_types.get(word, '未知')

    def analyze_text_weighted(self, text):
        """使用词频权重分析文本中的官方话语浓度"""
        if not text.strip():
            return {
                'weighted_density': 0.0,
                'official_words': [],
                'total_words': 0,
                'official_word_count': 0
            }

        # 使用结巴分词
        words = [word for word in jieba.cut(text) if word.strip()]
        total_words = len(words)
        
        # 统计官方话语词汇及其权重
        official_words_found = [word for word in words if word in self.official_words]
        official_word_count = len(official_words_found)
        
        # 计算加权浓度
        total_frequency = sum(self.word_frequencies.get(word, 1) for word in words)
        official_frequency = sum(self.word_frequencies.get(word, 1) for word in official_words_found)
        
        weighted_density = official_frequency / total_frequency if total_frequency > 0 else 0
        
        return {
            'weighted_density': weighted_density,
            'official_words': official_words_found,
            'total_words': total_words,
            'official_word_count': official_word_count
        }

    def analyze_text_with_options(self, text, mode='weighted', output_type='simple'):
        """使用指定选项分析文本中的官方话语浓度

        Args:
            text (str): 要分析的文本
            mode (str): 分析模式，可选值：
                - 'basic': 基础分析模式
                - 'weighted': 加权分析模式
                - 'bert': BERT语义分析模式
            output_type (str): 输出类型，'simple'表示只输出浓度值，'full'表示输出完整分析信息

        Returns:
            dict: 分析结果
        """
        """使用指定选项分析文本中的官方话语浓度

        Args:
            text (str): 要分析的文本
            method (str): 分析方法，'weighted'表示使用加权分析，'basic'表示使用基础分析
            output_type (str): 输出类型，'simple'表示只输出浓度值，'full'表示输出完整分析信息

        Returns:
            dict: 分析结果
        """
        # 根据mode选择分析方法
        if mode == 'bert':
            from .bert_analyzer import BertBureaucrateseAnalyzer
            bert_analyzer = BertBureaucrateseAnalyzer()
            result = bert_analyzer.calculate_semantic_density(text)
            density_key = 'semantic_density'
        elif mode == 'weighted':
            result = self.analyze_text_weighted(text)
            density_key = 'weighted_density'
        else:  # basic mode
            result = self.analyze_text(text)
            density_key = 'density'
        
        # 根据output_type返回相应的结果
        if output_type == 'simple':
            return {'density': result[density_key]}
        
        return result

    def preprocess_text(self, text, remove_special_chars=True, remove_extra_spaces=True, custom_rules=None):
        """文本预处理功能

        Args:
            text (str): 要处理的文本
            remove_special_chars (bool): 是否移除特殊字符
            remove_extra_spaces (bool): 是否移除多余空格
            custom_rules (list): 自定义处理规则列表，每个规则是一个(pattern, replacement)元组

        Returns:
            str: 预处理后的文本
        """
        if not text:
            return text

        # 移除特殊字符
        if remove_special_chars:
            text = ''.join(char for char in text if char.isprintable())

        # 移除多余空格
        if remove_extra_spaces:
            text = ' '.join(text.split())

        # 应用自定义规则
        if custom_rules:
            for pattern, replacement in custom_rules:
                text = text.replace(pattern, replacement)

        return text

    def analyze_file(self, file_path, text_column='text', weighted=False, as_dataframe=False):
        """分析文件中的文本
        
        Args:
            file_path (str): 输入文件路径
            text_column (str): 文本列的列名，默认为'text'
            weighted (bool): 是否使用加权分析
            as_dataframe (bool): 是否返回DataFrame格式的结果
            
        Returns:
            list or pd.DataFrame: 分析结果
        """
        # 读取文件
        df = pd.read_csv(file_path)
        if text_column not in df.columns:
            raise ValueError(f"找不到列名 '{text_column}'")
        
        # 分析每个文本
        results = []
        for text in df[text_column]:
            result = self.analyze_text_weighted(text) if weighted else self.analyze_text(text)
            if self.use_bert:
                bert_result = self.bert_analyzer.calculate_semantic_density(text)
                result['semantic_density'] = bert_result['semantic_density']
            results.append(result)
        
        if as_dataframe:
            return pd.DataFrame(results)
        return results

    def analyze_directory(self, dir_path, text_column='text', weighted=False, as_dataframe=False):
        """分析目录中所有文件的文本
        
        Args:
            dir_path (str): 输入目录路径
            text_column (str): 文本列的列名，默认为'text'
            weighted (bool): 是否使用加权分析
            as_dataframe (bool): 是否返回DataFrame格式的结果
            
        Returns:
            dict or pd.DataFrame: 分析结果，键为文件名
        """
        dir_path = Path(dir_path)
        if not dir_path.exists() or not dir_path.is_dir():
            raise ValueError(f"目录 '{dir_path}' 不存在或不是一个目录")
        
        results = {}
        for file_path in dir_path.glob('*.csv'):
            try:
                file_results = self.analyze_file(
                    file_path, 
                    text_column=text_column,
                    weighted=weighted,
                    as_dataframe=as_dataframe
                )
                results[file_path.name] = file_results
            except Exception as e:
                print(f"处理文件 {file_path} 时出错: {str(e)}")
                continue
        
        if as_dataframe:
            return pd.concat(results, names=['file', 'index'])
        return results