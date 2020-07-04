import xlsxwriter, sys
workbook = xlsxwriter.Workbook('Nafantano report.xlsx')
worksheet = workbook.add_worksheet('Expenses Nafantano')

lines_of_file = open(sys.argv[1], 'r', encoding='utf-8').read().split('\n')[1:-1] # array of all lines of file

lines_by_tokens = []
for line in lines_of_file:
    lines_by_tokens.append(line.split(",")) # lines are divided by ','

for i, line in enumerate(lines_by_tokens):
    for j, token in enumerate(line):
        if token == '':
            del lines_by_tokens[i][j]

date = []
account = []
category = []
amount = []
description = []
for line in lines_by_tokens:
    date.append(line[0])
    account.append(line[1])
    category.append(line[2])
    amount.append(line[3])
    if not line[-1] == "AZN":
        description.append(line[-1])
    else:
        description.append("No description")

del lines_of_file, lines_by_tokens

all_records = []

for i in range(0, len(date)):
    record = {}
    record.update(date = date[i], account = account[i], category = category[i], amount = amount[i], description = description[i])
    all_records.append(record)

del date, account, category, amount, description

nafantano_records = []
for record in all_records:
    if not record['account'] == "Me" and not record['category'] == 'Last month remainder':
        nafantano_records.append(record)


del all_records

for i, record in enumerate(nafantano_records):
    worksheet.write(i, 0, record['date'])
    worksheet.write(i, 1, record['category'])
    worksheet.write(i, 2, float(record['amount']))
    worksheet.write(i, 3, record['description'])

all_income_and_expences = []

for record in nafantano_records:
    amount = str(record['amount'])
    if amount[0] == "-":
        all_income_and_expences.append(amount)
    else:
        all_income_and_expences.append("+" + amount)


worksheet.write(len(nafantano_records) + 1, 0, "Money left:")
worksheet.write(len(nafantano_records) + 1, 1, eval(" ".join(all_income_and_expences)))

workbook.close()
