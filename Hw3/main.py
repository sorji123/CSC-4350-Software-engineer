import time
import csv
import tempfile


# number 1
def fizz():
    list2 = range(1, 100)
    for i in range(1, 101):
        print(i)
        if (i % 3 == 0 and i % 5 == 0):
            print(i, "FizzBuzz")
        elif (i % 3 == 0):
            print(i, "fizz")
        elif (i % 5 == 0):
            print(i, "bizz")


p1 = fizz()
print(p1)

# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))


# number 2
def volume():
    r = int(input("enter a number:  "))
    r1 = r*r*r
    v = r1*3.14*4/3
    return(v)


p2 = volume()
print(p2)


# 3
def csv_to_dict():

    with open('Books.CSV') as file:
        for i in csv.DictReader(file):
            print(dict(i))
    print("csv converted to worked")


print(csv_to_dict())

# number 4


# number 4


with open('Books.CSV', mode='r') as infile:
    reader = csv.reader(infile)
    with open('Books.CSV', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = dict((rows[0], rows[1]) for rows in reader)


def csv_writer():
    colums = ['Title', 'Author', 'ISBN13', 'Pages']
    mydict = {
        "Title": ["1984", "Animal Farm", "Brave New World", "Fahrenheit 451", "Jane Eyre", "Wuthering Heights", "Agnes Grey", "Walden", "Walden Two", "Eats, Shoots, & Leaves"], "Author": ["George Orwell", "George Orwell", "Aldous Huxley", "Ray Bradbury", "Charlotte Brontë", "Emily Brontë", "Anne Brontë", "David Thoreau", "B. F. Skinner", "Lynne Truss"], "ISBN13": ["978-0451524935", "978-0451526342", "978-0060929879", "978-0345342966", "978-0142437209", "978-0141439556", "978-1593083236", "978-1420922615", "978-0872207783", "978-1592400874"], "Pages": ["268", "144", "288", "208", "532", "416", "256", "156", "301", "209"]
    }
    csv_file = "Books.CSV"
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=colums)
            writer.writeheader()
            for key in mydict:
                writer.writerow(key)
    except IOError:
        print("I/O error")

    # number 5


def test_write_csv():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as csvfile:
        csv_writer()
    with open(csvfile.name) as csvfile:
        reader = csv.DictReader(csvfile)
