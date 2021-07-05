import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import random
import statistics

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()

population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)

print(f"population_mean: {population_mean}")
print(f"population_stdev: {population_stdev}")

def random_set_of_mean():
    datalist = []
    for i in range(0, 100):
        num = random.randint(0, len(data)-1)
        random_value = data[num]
        datalist.append(random_value)
    mean = statistics.mean(datalist)
    return mean

mean_list = []
for i in range(0, 1000):
    sample_mean = random_set_of_mean()
    mean_list.append(sample_mean)

fig = ff.create_distplot([mean_list], ["temp"], show_hist = False)
fig.show()

sampling_list_mean = statistics.mean(mean_list)
sampling_list_stdev = statistics.stdev(mean_list)

print(f"sampling_list_mean: {sampling_list_mean}")
print(f"sampling_list_stdev: {sampling_list_stdev}")