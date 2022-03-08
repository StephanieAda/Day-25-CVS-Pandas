import pandas

# Practising with a week's weather csv
# data = pandas.read_csv("2.1 weather_data.csv")
#
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(data['temp'].max())
#
# # Get data in Columns
# print(data['condition'])
# print(data.condition)

# Get data in rows
# print(data[data.day == 'Monday'])
# max = data['temp'].max()
# print(max)
# print(data[data.temp == max] )

# monday = data[data.day == 'Monday']
# mon_temp = monday.temp
# cal = (mon_temp * (9/5)) + 32
# print(cal)

# Create Dataframe from scratch
# data_dict = {
#     "students": ["Stephanie", "Kachi", "Angel"],
#     "scores": [89, 88, 99]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# Trying to create a csv file containing only the fur color count of the squirrels from the Great Squirrel Census 2018

squirrel_data = pandas.read_csv('4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color = squirrel_data['Primary Fur Color']
fur_color_count = color.value_counts()
# print(fur_color_count)

squirrel_color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [fur_color_count.Gray, fur_color_count.Cinnamon, fur_color_count.Black]
}
# print(squirrel_color_dict)
squirrel_color_data = pandas.DataFrame(squirrel_color_dict)
# print(squirrel_color_data)
squirrel_color_data.to_csv("squirrel_color_count.csv")
