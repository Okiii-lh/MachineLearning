import matplotlib.pyplot as plt

def plot_data(x, y):
    # ===================== Your Code Here =====================
    # Instructions : Plot the training data into a figure using the matplotlib.pyplot
    #                using the "plt.scatter" function. Set the axis labels using
    #                "plt.xlabel" and "plt.ylabel". Assume the population and revenue data
    #                have been passed in as the x and y.

    # Hint : You can use the 'marker' parameter in the "plt.scatter" function to change the marker type (e.g. "x", "o").
    #        Furthermore, you can change the color of markers with 'c' parameter.

    # 设置图像大小
    plt.figure(figsize=(20, 8), dpi=80)

    plt.scatter(x, y, edgecolors='red')

    plt.xlabel("Profit in $ 10,000s")
    plt.ylabel("Population of City in 10,000s")

    # ===========================================================

    plt.show()
