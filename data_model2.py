import matplotlib.pyplot as plt

x_data = ["September", "October", "November", "December", "January", "February"]
y1_data = [5280000, 5501000, 5469000, 5480000, 5533000, 5554000]
y2_data = [55280000, 5500000, 5729000, 5968000, 56217000, 6476000]

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
plt.pie(y1_data, labels=x_data, colors=colors, startangle=90)
plt.pie(y2_data, labels=x_data, colors=colors, startangle=90)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (KRW)")

plt.legend()

plt.show()
