import pyecharts
import pyecharts.options as opts
from pytrends.request import TrendReq

# Query Google Trends for interested keywords.
pytrend = TrendReq()
project_list = ['Apache Hadoop', 'Apache Hive', 'Apache Spark', 'Apache Hbase',
        'Apache Flink']

# Query for data of the last 30 days.
pytrend.build_payload(kw_list=project_list, cat=0, timeframe='today 1-m', geo='', gprop='')
df = pytrend.interest_over_time()

# Perform normalization to the data.
df = df.drop(['isPartial'], axis=1)
df = df.div(df.max(axis=1), axis=0)
df = df * 100

# Draw chart using pyecharts.
line = pyecharts.charts.Line(init_opts=opts.InitOpts(width='1100px'))
xaxis = [i.strftime("%b-%d-%Y") for i in df[project_list[0]].keys()]
line.add_xaxis(xaxis)

for project in project_list:
    yaxis = [int_value for int_value in map(int, df[project].values.tolist())]
    line.add_yaxis(project, yaxis, is_smooth=True,
            linestyle_opts=opts.LineStyleOpts(width=2), label_opts=opts.LabelOpts(is_show=False),
            symbol_size=8)

line.set_global_opts(title_opts=opts.TitleOpts(
        title="Normalized Google trends for famous OpenSource BigData prjects over last 30 days"),
        tooltip_opts=opts.TooltipOpts(trigger='axis'),
        legend_opts=opts.LegendOpts(pos_left='right', pos_top='middle',  orient="vertical"),
    )

line.render("google_trends.html")
