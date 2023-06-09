from CarRentalApp.models import Car, Category
import csv
import os

def run():

    path = "scripts/data/luxury.csv"

    if os.path.exists(path):

        fhand = open(path)
        reader = csv.reader(fhand)

        # skip the first row of the csv file.
        next(reader)
        luxury = Category.objects.get(category_name='Luxury')

        for row in reader:
            
            car = Car(car_name = row[0], price = row[1], category = luxury)
            car.save()
    else:

        print("Path does not exist")