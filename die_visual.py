# $$
import pygal

from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

frequecies = []
max_result = die_1.num_sides+die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequecies.append(frequency)

hist = pygal.Bar()

hist.title = 'Results of rolling two D6 100,000 times'

hist.x_labels = []

for value in range(2, max_result + 1):
    hist.x_labels += [str(value)]

hist.x_title = 'Result'
hist.y_title = "Frequency of Result"

hist.add('2 D6', frequecies)
hist.render_to_file('die_visual.svg')

print(frequecies)
