import state_demographics
list_of_report = state_demographics.get_all_states()

list = []

list_two = []






for x in range(len(list_of_report)):
    list.append(list_of_report[x]["State"])
    list_two.append(list_of_report[x]["Education"]["High School or Higher"])



import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


y_pos = np.arange(len(list))

plt.bar(y_pos, list_two, align='center', alpha=0.5,)
plt.xticks(y_pos,list, fontsize= 10, rotation = (90))
plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
plt.ylabel('education')
plt.title('state')

plt.show()
