import csv

columns = ['Company Name', 'Amount of Users Affected']
US_Columns = ['Year', 'Data Compromises', 'Number of records exposed in millions',
              'Amount of Users Affected in millions']
Country_Columns = ['Year', 'Amount of Users Affected in millions']

with open("CompanyData.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, columns, delimiter=",")
    writer.writeheader()

    writer.writerow({"Company Name": "Uber Breach", "Amount of Users Affected": 57e6})
    writer.writerow({"Company Name": "Imperva", "Amount of Users Affected": 30e6})
    writer.writerow({"Company Name": "Chegg", "Amount of Users Affected": 40e6})
    writer.writerow({"Company Name": "Cisco WebEx", "Amount of Users Affected": 45e6})
    writer.writerow({"Company Name": "Microsoft", "Amount of Users Affected": 100e6})

# Data plotting for United States Cyber Crime
with open("US_Data.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, US_Columns, delimiter=",")
    writer.writeheader()

    writer.writerow({"Year": 2013, "Data Compromises": 614,
                     "Number of records exposed in millions": 91.98,
                    "Amount of Users Affected in millions": 0})
    writer.writerow({"Year": 2014, "Data Compromises": 783,
                     "Number of records exposed in millions": 85.61,
                     "Amount of Users Affected in millions": 0})
    writer.writerow({"Year": 2015, "Data Compromises": 785,
                     "Number of records exposed in millions": 169.1,
                     "Amount of Users Affected in millions": 318.28})
    writer.writerow({"Year": 2016, "Data Compromises": 1099,
                     "Number of records exposed in millions": 36.6,
                     "Amount of Users Affected in millions": 2541.07})
    writer.writerow({"Year": 2017, "Data Compromises": 1506,
                     "Number of records exposed in millions": 198,
                     "Amount of Users Affected in millions": 1825.41})
    writer.writerow({"Year": 2018, "Data Compromises": 1175,
                     "Number of records exposed in millions": 471.23,
                     "Amount of Users Affected in millions": 2227.85})
    writer.writerow({"Year": 2019, "Data Compromises": 883.56,
                     "Number of records exposed in millions": 164.68,
                     "Amount of Users Affected in millions": 883.56})
    writer.writerow({"Year": 2020, "Data Compromises": 1108,
                     "Number of records exposed in millions": 222.5,
                     "Amount of Users Affected in millions": 310.12})
    writer.writerow({"Year": 2021, "Data Compromises": 1862,
                     "Number of records exposed in millions": 127.7,
                     "Amount of Users Affected in millions": 298.08})
    writer.writerow({"Year": 2022, "Data Compromises": 1802,
                     "Number of records exposed in millions": 22.9,
                     "Amount of Users Affected in millions": 422.14})
    writer.writerow({"Year": 2023, "Data Compromises": 3205,
                     "Number of records exposed in millions": 169.1,
                     "Amount of Users Affected in millions": 353.02})

with open("RussiaData.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, Country_Columns, delimiter=",")
    writer.writeheader()
    writer.writerow({"Year": "2013", "Amount of Users Affected in millions": 3.3e6})
    writer.writerow({"Year": "2014", "Amount of Users Affected in millions": 34.5e6})
    writer.writerow({"Year": "2015", "Amount of Users Affected in millions": 34.1e6})
    writer.writerow({"Year": "2016", "Amount of Users Affected in millions": 129.1e6})
    writer.writerow({"Year": "2017", "Amount of Users Affected in millions": 5.8e6})
    writer.writerow({"Year": "2018", "Amount of Users Affected in millions": 28.3e6})
    writer.writerow({"Year": "2019", "Amount of Users Affected in millions": 279.9e6})
    writer.writerow({"Year": "2020", "Amount of Users Affected in millions": 191.2e6})
    writer.writerow({"Year": "2021", "Amount of Users Affected in millions": 250.4e6})
    writer.writerow({"Year": "2022", "Amount of Users Affected in millions": 702.2e6})
    writer.writerow({"Year": "2023", "Amount of Users Affected in millions": 1121.3e6})

with open("ChinaData.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, Country_Columns, delimiter=",")
    writer.writeheader()
    writer.writerow({"Year": "2013", "Amount of Users Affected in millions": 6.55e6})
    writer.writerow({"Year": "2014", "Amount of Users Affected in millions": 6.6e6})
    writer.writerow({"Year": "2015", "Amount of Users Affected in millions": 6.54e6})
    writer.writerow({"Year": "2016", "Amount of Users Affected in millions": 7.17e6})
    writer.writerow({"Year": "2017", "Amount of Users Affected in millions": 6.43e6})
    writer.writerow({"Year": "2018", "Amount of Users Affected in millions": 5.48e6})
    writer.writerow({"Year": "2019", "Amount of Users Affected in millions": 5.07e6})
    writer.writerow({"Year": "2020", "Amount of Users Affected in millions": 4.86e6})
    writer.writerow({"Year": "2021", "Amount of Users Affected in millions": 4.78e6})
    writer.writerow({"Year": "2022", "Amount of Users Affected in millions": 5.03e6})
    writer.writerow({"Year": "2023", "Amount of Users Affected in millions": 4.42e6})


with open("UK_Data.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, Country_Columns, delimiter=",")
    writer.writeheader()
    writer.writerow({"Year": "2013", "Amount of Users Affected in millions": 8.98e6})
    writer.writerow({"Year": "2014", "Amount of Users Affected in millions": 7.3e6})
    writer.writerow({"Year": "2015", "Amount of Users Affected in millions": 1.34e6})
    writer.writerow({"Year": "2016", "Amount of Users Affected in millions": 14.84e6})
    writer.writerow({"Year": "2017", "Amount of Users Affected in millions": 5.11e6})
    writer.writerow({"Year": "2018", "Amount of Users Affected in millions": 10.21e6})
    writer.writerow({"Year": "2019", "Amount of Users Affected in millions": 6.21e6})
    writer.writerow({"Year": "2020", "Amount of Users Affected in millions": 0.64e6})
    writer.writerow({"Year": "2021", "Amount of Users Affected in millions": 0.48e6})
    writer.writerow({"Year": "2022", "Amount of Users Affected in millions": 1.2e6})
    writer.writerow({"Year": "2023", "Amount of Users Affected in millions": 1.05e6})


