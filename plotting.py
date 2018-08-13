import matplotlib.pyplot as plt

def polygon_plot(creature_list):
    fig,ax = plt.subplots()
    for c in creature_list:
        ax.add_patch(c.polygon)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    plt.show()


def xy_plot(creature_list, x_attr, y_attr):
    x_vals = [c.x_attr for c in creature_list]
    y_vals = [c.y_attr for c in creature_list]
    colors = [c.plot_color for c in creature_list]
    plt.scatter(x_vals, y_vals, c=colors)
    plt.show()

def xy_plot2(creature_list):
    x_vals = []
    for c in creature_list:
        diags = c.find_diagonals()
        diag_product = diags[1]*diags[0]
        x_vals.append(diag_product)
    y_vals = [c.lead for c in creature_list]
    colors = [c.plot_color for c in creature_list]
    plt.scatter(x_vals, y_vals, c=colors, s=3)
    plt.show()
