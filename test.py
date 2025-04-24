import pandas as pd
import plotly.express as px
import plotly.io as pio

# 设置 Plotly 在浏览器中打开
pio.renderers.default = 'browser'

# 读取数据
df = pd.read_csv("Results_21Mar2022.csv")

# 分组聚合
treemap_data = df.groupby(['diet_group', 'sex', 'age_group']).agg({
    'mean_ghgs': 'mean',
    'mean_land': 'mean',
    'mean_watscar': 'mean',
    'mean_eut': 'mean',
    'mean_bio': 'mean',
    'mean_watuse': 'mean'
}).reset_index()

# 添加可读性强的标签（可选）
treemap_data['label'] = treemap_data['diet_group'] + ' | ' + treemap_data['sex'] + ' | ' + treemap_data['age_group']

# 绘制 Treemap
fig = px.treemap(
    treemap_data,
    path=['diet_group', 'sex', 'age_group'],
    values='mean_ghgs',
    color='mean_ghgs',
    color_continuous_scale='RdBu',
    title='Treemap: Average Greenhouse Gas Emissions by Diet, Gender and Age'
)

fig.show()
