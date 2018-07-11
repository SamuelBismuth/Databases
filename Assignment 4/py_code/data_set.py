from input_file import text_file, text_file_feature
import enum


class DataLine:

    # Salary = B0 + B1(gender) + B2(rank) + B3(years) + B4(degree) + error
    def __init__(self, salary, gender, rank, years, degree, university='0', nationality='0'):
        self.salary = salary
        self.gender = gender
        self.rank = rank
        self.years = years
        self.degree = degree
        self.university = university
        self.nationality = nationality

    def to_string(self):
        print("salary: ", self.salary,
              ", gender: ", self.gender,
              ", rank: ", self.rank,
              ", years: ", self.years,
              ", degree: ", self.degree,
              ", university: ", self.university,
              ", nationality: ", self.nationality)


'''
Assumption:
male=0, female=1
assistant=1, ‫‪associate‬‬‬‬=2, ‫‪full‬=3
master=0, doctorate=1

My features assumption:
ariel=1, ivrit=2, technion=3
russia=1, france=2, israel=3
'''


class Gender(enum.Enum):
    male = 0
    female = 1


class Rank(enum.Enum):
    assistant = 1
    associate = 2
    full = 3


class Degree(enum.Enum):
    masters = 0
    doctorate = 1


class University(enum.Enum):
    ariel = 1
    ivrit = 2
    technion = 3


class Nationality(enum.Enum):
    russia = 1
    france = 2
    israel = 3


data_line = text_file.flatMap(lambda line:
                              list(w for w in line.split())).collect()

data_line_feature = text_file_feature.flatMap(lambda line:
                                              list(w for w in line.split())).collect()

data_line_computational = [
    DataLine(
        data_line[4 + i],  # Salary.
        str(Gender[data_line[0 + i]].value),  # Gender.
        str(Rank[data_line[1 + i]].value),  # Rank.
        data_line[2 + i],  # Years.
        str(Degree[data_line[3 + i]].value)  # Degree.
    ) for i in range(0, 5 * int((len(data_line) / 5) * 0.7), 5)
]

data_line_verify = [
    DataLine(
        data_line[4 + i],  # Salary.
        str(Gender[data_line[0 + i]].value),  # Gender.
        str(Rank[data_line[1 + i]].value),  # Rank.
        data_line[2 + i],  # Years.
        str(Degree[data_line[3 + i]].value)  # Degree.
    ) for i in range(5 * int((len(data_line) / 5) * 0.7), len(data_line) - 5, 5)
]

data_line_computational_feature = [
    DataLine(
        data_line_feature[4 + i],  # Salary.
        str(Gender[data_line_feature[0 + i]].value),  # Gender.
        str(Rank[data_line_feature[1 + i]].value),  # Rank.
        data_line_feature[2 + i],  # Years.
        str(Degree[data_line_feature[3 + i]].value),  # Degree.
        str(University[data_line_feature[5 + i]].value),  # University.
        str(Nationality[data_line_feature[6 + i]].value)  # Nationality.
    ) for i in range(0, 7 * int((len(data_line_feature) / 7) * 0.7), 7)
]

data_line_verify_feature = [
    DataLine(
        data_line_feature[4 + i],  # Salary.
        str(Gender[data_line_feature[0 + i]].value),  # Gender.
        str(Rank[data_line_feature[1 + i]].value),  # Rank.
        data_line_feature[2 + i],  # Years.
        str(Degree[data_line_feature[3 + i]].value),  # Degree.
        str(University[data_line_feature[5 + i]].value),  # University.
        str(Nationality[data_line_feature[6 + i]].value)  # Nationality.
    ) for i in range(7 * int((len(data_line_feature) / 7) * 0.7), len(data_line_feature) - 7, 7)
]
