import openpyxl
from openpyxl import Workbook

# Create a new Excel workbook and sheet
workbook = Workbook()
sheet = workbook.active
sheet.title = 'LoginTest'

# Add the header row
header = ['Test ID', 'Username', 'Password', 'Date', 'Time of Test', 'Name of Tester', 'Test Result']
sheet.append(header)

# Add sample data (5 rows for testing)
data = [
    ['1', 'Admin', 'admin123', '2024-07-29', '10:00', 'Tester1', ''],
    ['2', 'invalidUser1', 'invalidPass1', '2024-07-29', '10:05', 'Tester1', ''],
    ['3', 'invalidUser2', 'invalidPass2', '2024-07-29', '10:10', 'Tester1', ''],
    ['4', 'invalidUser3', 'invalidPass3', '2024-07-29', '10:15', 'Tester1', ''],
    ['5', 'Admin', 'admin123', '2024-07-29', '10:20', 'Tester1', '']
]

for row in data:
    sheet.append(row)

# Save the workbook
workbook.save('login_tests.xlsx')
