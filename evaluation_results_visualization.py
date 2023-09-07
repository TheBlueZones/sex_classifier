import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
import os
from matplotlib import font_manager

#获取操作系统中可用的中文字体列表：
from matplotlib.font_manager import FontManager

def get_chinese_fonts():
    fonts = []
    fm = FontManager()
    for font in fm.ttflist:
        if "SimHei" in font.name or "Heiti" in font.name or "黑体" in font.name:
            fonts.append(font.name)
    return fonts

chinese_fonts = get_chinese_fonts()
print(chinese_fonts)


font_name = chinese_fonts[0]
plt.rcParams["font.family"] = font_name

# 读取CSV文件
data = pd.read_csv("evaluation_results.csv")

# 设置图表大小
plt.figure(figsize=(18, 6))  # 增加图表宽度

# 为每个性能指标绘制柱状图
bar_width = 0.15  # 减小柱状图宽度
x = data.index
plt.bar(x - bar_width, data['accuracy'], width=bar_width, label="准确率")
plt.bar(x, data['male_f1_score'], width=bar_width, label="男性F1分数")
plt.bar(x + bar_width, data['female_f1_score'], width=bar_width, label="女性F1分数")

# 在柱状图中直接显示得分
for i in range(len(x)):
    plt.text(x[i] - bar_width, data['accuracy'][i] + 0.01, f"{data['accuracy'][i]:.2f}", ha="center", fontsize=8)
    plt.text(x[i], data['male_f1_score'][i] + 0.01, f"{data['male_f1_score'][i]:.2f}", ha="center", fontsize=8)
    plt.text(x[i] + bar_width, data['female_f1_score'][i] + 0.01, f"{data['female_f1_score'][i]:.2f}", ha="center", fontsize=8)

# 设置x轴标签
xtick_labels = [f"{name}\n第{index+1}次模型\n预训练图像数: {pre_img}\n训练轮数: {epochs}\n数据量: {data_cnt}\n模型参数: {params}" for index, (name, pre_img, epochs, data_cnt, params) in enumerate(data[['model_name', 'pretraining_image_count', 'training_epochs', 'data_count', 'model_parameters']].values)]
plt.xticks(x, xtick_labels, fontsize=8)

# 设置y轴标签和范围
plt.ylabel("得分")
plt.ylim(0, 1.2)

# 添加图例
plt.legend()

# 保存图表为SVG文件
plt.savefig("model_performance_cn_matplotlib.svg", format='svg', bbox_inches="tight")

# 将SVG图像嵌入到HTML文件中
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>模型性能评估</title>
</head>
<body>
    <div>
        <img src="model_performance_cn_matplotlib.svg" alt="模型性能评估">
    </div>
</body>
</html>
"""

with open("model_performance_cn_matplotlib.html", "w", encoding="utf-8") as f:
    f.write(html_template)

# 在浏览器中打开HTML文件
webbrowser.open_new_tab("file://" + os.path.abspath("model_performance_cn_matplotlib.html"))
