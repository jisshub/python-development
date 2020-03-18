from csv import writer

with open("movies.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(['Name', 'Year'])
    csv_writer.writerow(['Ratchasan', 2018])
    csv_writer.writerow(['Vadachennai', 2018])
    csv_writer.writerow(['Naran', 2007])
