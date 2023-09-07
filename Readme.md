# 男女分类器

## 分类器实施

`classification_of_men_and_women.py` 是一个用于将原始数据集中的男性和女性图片分别放入两个文件夹中的脚本，这样可以方便后续的训练和分类。

## 性别分类器

`sex_classifier.ipynb` 是一个具体实施性别分类的 notebook 文件。其中，`sex_classifier_mobilenet` 使用 MobileNet 模型进行分类，如果要使用 VGG16 模型，只需将训练模型部分的代码改为 VGG16 文件中的内容即可。

## Mobilenet 超参数搜索

`sex_classifier_mobilenet_hyperparameter_search.ipynb` 是针对 MobileNet 模型的超参数搜索的 notebook 文件。

## 评估结果

`evaluation_results.ipynb` 包含了模型的评估结果。

## 评估结果可视化

`evaluation_results_visualization.ipynb` 是用于将评估结果可视化的 notebook 文件。
