import matplotlib.pyplot as plt

# 定义颜色循环，使用RGB值表示
colors = [(1, 0, 0),   # 红色
          (0, 1, 0),   # 绿色
          (0, 0, 1),   # 蓝色
          (1, 1, 0)]   # 黄色

# 使用颜色循环绘制多条曲线
x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [20, 30, 40, 50]
y3 = [30, 40, 50, 60]

fig, ax = plt.subplots()
ax.set_prop_cycle('color', colors)

ax.plot(x, y1)
ax.plot(x, y2)
ax.plot(x, y3)

plt.show()