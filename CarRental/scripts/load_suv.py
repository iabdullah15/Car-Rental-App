from CarRentalApp.models import Car, Category
import csv
import os

def run():

    path = "scripts/data/suv.csv"

    if os.path.exists(path):

        fhand = open(path)
        reader = csv.reader(fhand)

        # skip the first row of the csv file.
        next(reader)
        suv = Category.objects.get(category_name='SUV')

        for row in reader:
            # print(suv)   
            # print(row)
            car = Car(car_name = row[0], price = row[1], category = suv)
            car.save()
    else:

        print("Path does not exist")