import matplotlib.pyplot as plt

def polygon_plot(creature_list):
    fig,ax = plt.subplots()
    for c in creature_list:
        ax.add_patch(c.polygon)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    plt.show()
