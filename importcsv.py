import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoBlog.settings")
django.setup()

# from single_pages.models import MSemi
# with open('MemorySemiconductor.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         MSemi.objects.create(
#             country = row[0],
#             share = row[1]
#         )
#         print(row)

# from single_pages.models import SSemi
# with open('SystemSemiconductor.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         SSemi.objects.create(
#             country = row[0],
#             share = row[1]
#         )
#         print(row)


# from single_pages.models import Fabless
# with open('Fabless.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         Fabless.objects.create(
#             country = row[0],
#             share = row[1]
#         )
#         print(row)



# from single_pages.models import KorSemiShare, SemiShare
# SemiShareData = {'KorSemiShare': KorSemiShare, 'SemiShare': SemiShare}
# for i in SemiShareData.items():
#     fileName=i[0]+'.csv'
#     with open(fileName) as csv_file_sub_categories:
#         rows = csv.reader(csv_file_sub_categories)
#         next(rows, None)
#         for row in rows:
#             i[1].objects.create(
#                 year = row[0],
#                 semi = row[1],
#                 Msemi = row[2],
#                 Ssemi = row[3]
#             )
#             print(row)

# from single_pages.models import Research
# with open('Research.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         Research.objects.create(
#             year = row[0],
#             researchFunds = row[1]
#         )
#         print(row)

# from single_pages.models import SemiExport
# with open('SemiExport.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         SemiExport.objects.create(
#             year = row[0],
#             semi = row[1],
#             oil = row[2],
#             car = row[3]
#         )
#         print(row)

# from single_pages.models import KorSemiExport
# with open('KorSemiExport.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         KorSemiExport.objects.create(
#             year = row[0],
#             all = row[1],
#             export = row[2],
#             share = row[3]
#         )
#         print(row)

# from single_pages.models import ChiSemiExport
# with open('ChiSemiExport.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         ChiSemiExport.objects.create(
#             year = row[0],
#             export = row[1],
#             Simport = row[2]
#         )
#         print(row)

# from single_pages.models import WorldSemiImExport
# with open('WorldSemiImExport.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         WorldSemiImExport.objects.create(
#             year = row[0],
#             export = row[1],
#             Simport = row[2],
#             both = row[3]
#         )
#         print(row)

# from single_pages.models import WorldSemiImport, ChinaSemiImport
# SemiShareData = {'WorldSemiImport': WorldSemiImport, 'ChinaSemiImport': ChinaSemiImport}
# for i in SemiShareData.items():
#     fileName=i[0]+'.csv'
#     with open(fileName) as csv_file_sub_categories:
#         rows = csv.reader(csv_file_sub_categories)
#         next(rows, None)
#         for row in rows:
#             i[1].objects.create(
#                 year = row[0],
#                 export = row[1]
#             )
#             print(row)


from single_pages.models import Topic2020, Topic2021, Topic2022
SemiShareData = {'Topic2020': Topic2020, 'Topic2021': Topic2021, 'Topic2022': Topic2022}
for i in SemiShareData.items():
    fileName=i[0]+'.csv'
    with open(fileName) as csv_file_sub_categories:
        rows = csv.reader(csv_file_sub_categories)
        next(rows, None)
        for row in rows:
            i[1].objects.create(
                info = row[0],
                status = row[1]
            )
            print(row)

from single_pages.models import TopicChange
with open('TopicChange.csv') as csv_file_sub_categories:
    rows = csv.reader(csv_file_sub_categories)
    next(rows, None)
    for row in rows:
        TopicChange.objects.create(
            year = row[0],
            economy = row[1],
            politics = row[2],
            culture = row[3],
            inter = row[4]
        )
        print(row)
