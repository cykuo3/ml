import random
import pandas as pd
import numpy
import matplotlib.pyplot as plt


def draw(times):
    data_arr = numpy.empty(times)
    weight_arr = numpy.empty(times)
    weight_arr.fill(1 / times)
    for i in range(0, times):
        data_arr[i] = random.randint(0, 1)
    print("data_arr=", data_arr)
    data_frame = pd.DataFrame(data_arr)
    data_frame.plot(kind="hist", legend=False, weights=weight_arr).set_ylabel("demo")
    plt.show()


if __name__ == "__main__":
    print("start...")
    draw(5)