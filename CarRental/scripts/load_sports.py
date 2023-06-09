from CarRentalApp.models import Car, Category
import csv
import os

def run():

    path = "scripts/data/sports.csv"

    if os.path.exists(path):

        fhand = open(path)
        reader = csv.reader(fhand)

        # skip the first row of the csv file.
        next(reader)
        sports = Category.objects.get(category_name='Sports')

        for row in reader:
            # print(sports)   
            # print(row)
            car = Car(car_name = row[0], price = row[1], category = sports)
            car.save()
    else:

        print("Path does not exist")

