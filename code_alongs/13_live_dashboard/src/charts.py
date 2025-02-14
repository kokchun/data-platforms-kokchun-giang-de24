import matplotlib.pyplot as plt


def line_chart(x, y, **options):
    fig, ax = plt.subplots(1)

    ax.plot(x, y, **options)

    ax.set(**options)

    fig.tight_layout()
    
    return fig