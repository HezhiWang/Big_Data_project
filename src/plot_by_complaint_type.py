import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import random

f1 = open('../output/count_5.out','r')
complaint_type = []
count_number = []
for line in f1.readlines():
	line = line.split('\t')
	complaint_type.append(line[0])
	count_number.append(int(line[1]))

count_percentage = [i/sum(count_number) for i in count_number]
top10_count_number = count_percentage[:10]
top10_count_complaint_type = complaint_type[:10]
y_pos = np.arange(len(top10_count_complaint_type))

plt.figure(figsize = (36, 18))
plt.barh(y_pos, top10_count_number, align='center', color = 'b', alpha = 0.5)
plt.yticks(y_pos, top10_count_complaint_type, size='xx-large')
plt.xlabel('Rate of Complaint Type', size = 'xx-large')
plt.ylabel('Complaint Type Count percentage', size = 'xx-large')
plt.title('Percentage of Top 10 Complaint Type Count', size = 'xx-large')
plt.savefig('../plots/top_10_complaint_type.png')

f1.close()
