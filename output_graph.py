import pycoolplot


#水平方向の美しい棒グラフ
def make_graph(index, data,xlabel):
    #data = [1000, 2000, 1000]
    #index = ["A", "B", "C"]
    pycoolplot.horizontal_bar(index, data,xlabel=xlabel,rate_graph=True)
    pycoolplot.plt.show()
    return


# # 折れ線グラフ
# data2 = [[970, 1010, 1015, 1008],
#          [975, 1020, 1002, 1035],
#          [975, 985, 995, 999]]
# index2 = ['Toyota', 'VW', 'GM']
# columns = [2013, 2014, 2015, 2016]
# ylabel = "Number"
# xlabel = "Year"
# pycoolplot.line_graph(data2, index2, columns, xlabel,
#                       ylabel, xtick=1, ytick=25)
# pycoolplot.plt.show()

# # 折れ線グラフ強調
# data2 = [[970, 1010, 1015, 1008],
#         [975, 1020, 1002, 1035],
#         [975, 985, 995, 999]]
# index2 = ['Toyota', 'VW', 'GM']
# columns = [2013, 2014, 2015, 2016]
# ylabel = "Number"
# xlabel = "Year"
# focus_id = 1  # the index of focusing line, in this case Toyota=0, VW=1, GM=2
# pycoolplot.line_graph(data2, index2, columns, xlabel,
#                       ylabel, xtick=1, ytick=25, focus_id=focus_id)
# pycoolplot.plt.show()