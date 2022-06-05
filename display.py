import pygal

# Initialise container
temp = []

# Load data
file = open('weather.txt', 'r')

# Add data to container
for line in file.read().splitlines():
    if line:
        temp.append(float(line))
file.close()

# Create a line graph
weather = pygal.Line()

# Populate the graph with data
weather.add('temp', temp)

# Chart title
weather.title = "Weather"

# Define x axis
weather.x_labels = range(1, len(temp) + 1)

# Render the graph
weather.render()
