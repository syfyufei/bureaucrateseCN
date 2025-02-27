from typing import List, Dict, Union
from .analyzer import BureaucrateseAnalyzer
from .bert_analyzer import BertBureaucrateseAnalyzer

class BureaucrateseAPI:
    def __init__(self, use_bert: bool = True, custom_dict_path: str = None):
        """初始化官方话语分析API

        Args:
            use_bert (bool): 是否使用BERT模型进行语义分析
            custom_dict_path (str): 自定义词典路径
        """
        self.analyzer = BureaucrateseAnalyzer(custom_dict_path=custom_dict_path)
        self.bert_analyzer = BertBureaucrateseAnalyzer(custom_dict_path=custom_dict_path) if use_bert else None

    def analyze_text(self, text: str, method: str = 'basic') -> Dict:
        """分析单个文本的官方话语浓度

        Args:
            text (str): 待分析的文本
            method (str): 分析方法，可选值：
                - 'basic': 基础密度分析
                - 'weighted': 加权密度分析
                - 'semantic': BERT语义分析

        Returns:
            Dict: 分析结果
        """
        if method == 'semantic':
            if not self.bert_analyzer:
                raise ValueError('BERT分析器未初始化，请在初始化API时设置use_bert=True')
            return self.bert_analyzer.calculate_semantic_density(text)
        elif method == 'weighted':
            return self.analyzer.analyze_text_weighted(text)
        else:
            return self.analyzer.analyze_text(text)

    def analyze_texts(self, texts: List[str], method: str = 'basic') -> List[Dict]:
        """批量分析多个文本的官方话语浓度

        Args:
            texts (List[str]): 待分析的文本列表
            method (str): 分析方法，可选值同analyze_text

        Returns:
            List[Dict]: 分析结果列表
        """
        return [self.analyze_text(text, method) for text in texts]

    def analyze_text_all(self, text: str) -> Dict[str, Dict]:
        """使用所有可用方法分析文本

        Args:
            text (str): 待分析的文本

        Returns:
            Dict[str, Dict]: 包含所有分析方法结果的字典
        """
        results = {
            'basic': self.analyzer.analyze_text(text),
            'weighted': self.analyzer.analyze_text_weighted(text)
        }
        
        if self.bert_analyzer:
            results['semantic'] = self.bert_analyzer.calculate_semantic_density(text)
        
        return results