
class Tree:
    def __init__(self, user_parameters, date):
        self.user_parameters = user_parameters
        self.date = date

    def __get_leafs_count(self):
        leafs = []
        params = Parameters()
        for i in self.user_parameters:
            if self.user_parameters[i]:
                leafs.append({i : params.get_parameters()[i]})
        return leafs

    def separete_by_parametres(self):
        parameters_example = Parameters();
        positions = parameters_example.get_parameters_position()

        leafs_count = list(self.__get_leafs_count()[0].values())[0]
        separate_param = list(self.__get_leafs_count()[0].keys())[0]

        separate_id = positions[separate_param]






class Parameters:
    parameters = {
        'gender': 2,
        'age': 3,
        'district': 7,
        'hazard': 5
    }

    parameters_position = {
        'gender': 1,
        'age': 2,
        'district': 3,
        'hazard': 4
    }

    def __init__(self, param=parameters):
        self.parameters = param

    def get_parameters(self):
        return self.parameters;

    def get_parameters_position(self):
        return self.parameters_position;

class Leaf(Tree):
    pass

lists = [[0, 1, 36, 8, 3], [1, 0, 63, 2, 3], [2, 1, 47, 8, 4], [3, 0, 68, 7, 1], [4, 0, 42, 2, 4], [5, 0, 44, 3, 3],
         [6, 1, 27, 4, 1], [7, 0, 61, 8, 3], [8, 1, 38, 3, 2], [9, 1, 20, 5, 5], [10, 1, 64, 7, 2], [11, 1, 57, 1, 2],
         [12, 0, 33, 5, 4], [13, 1, 67, 5, 4], [14, 0, 58, 4, 1], [15, 0, 32, 3, 4], [16, 1, 38, 6, 2], [17, 1, 62, 8, 1],
         [18, 0, 42, 5, 3], [19, 0, 32, 4, 4], [20, 1, 29, 5, 3], [21, 1, 34, 4, 1], [22, 0, 50, 1, 4], [23, 0, 28, 1, 4],
         [24, 0, 38, 3, 1], [25, 1, 31, 4, 4], [26, 1, 49, 4, 5], [27, 0, 26, 6, 2], [28, 0, 68, 4, 4], [29, 0, 70, 2, 4],
         [30, 0, 46, 7, 3], [31, 0, 34, 7, 3], [32, 0, 56, 8, 5], [33, 0, 59, 7, 3], [34, 1, 68, 7, 3], [35, 1, 35, 3, 3],
         [36, 0, 65, 2, 1], [37, 1, 42, 3, 4], [38, 0, 22, 2, 4], [39, 0, 64, 6, 2], [40, 0, 21, 5, 4], [41, 0, 20, 2, 2],
         [42, 0, 20, 4, 5], [43, 1, 60, 1, 5], [44, 1, 56, 8, 5], [45, 0, 61, 8, 4], [46, 0, 42, 5, 2], [47, 0, 30, 1, 2],
         [48, 0, 40, 5, 4], [49, 1, 57, 3, 2], [50, 1, 35, 1, 1], [51, 1, 29, 7, 1], [52, 0, 55, 2, 2], [53, 1, 30, 6, 3],
         [54, 1, 59, 5, 1], [55, 1, 34, 4, 2], [56, 0, 30, 4, 1], [57, 0, 28, 6, 5], [58, 0, 59, 1, 3], [59, 0, 65, 5, 3],
         [60, 0, 29, 5, 3], [61, 0, 66, 3, 5], [62, 1, 61, 7, 1], [63, 1, 54, 8, 2], [64, 0, 38, 1, 2], [65, 1, 69, 3, 3],
         [66, 1, 69, 5, 5], [67, 1, 49, 8, 1], [68, 0, 34, 1, 2], [69, 1, 29, 6, 4], [70, 1, 32, 3, 3], [71, 1, 24, 6, 5],
         [72, 0, 30, 5, 2], [73, 0, 33, 5, 3], [74, 0, 65, 2, 4], [75, 0, 37, 3, 1], [76, 1, 54, 5, 5], [77, 1, 69, 7, 5],
         [78, 0, 37, 6, 1], [79, 0, 63, 6, 3], [80, 1, 34, 4, 4], [81, 1, 45, 7, 2], [82, 1, 70, 2, 1], [83, 1, 39, 8, 5],
         [84, 0, 57, 5, 5], [85, 1, 62, 6, 5], [86, 0, 62, 2, 1], [87, 0, 27, 3, 3], [88, 1, 44, 2, 4], [89, 0, 41, 8, 5],
         [90, 1, 42, 7, 5], [91, 0, 29, 3, 5], [92, 1, 60, 1, 4], [93, 0, 41, 6, 4], [94, 0, 22, 1, 2], [95, 1, 61, 6, 1],
         [96, 1, 54, 6, 5], [97, 1, 61, 1, 1], [98, 1, 35, 5, 2], [99, 1, 59, 8, 2]]

parameters = {
    'gender': 1,
    'age': 0,
    'district': 1,
    'hazard': 0
}

tr = Tree(parameters, lists)
tr.separete_by_parametres()

# 0 : М; 1 : Ж
# 0 : <=40; 1 : >40;
# Округа согласно Вики
# Хазард согласно цифрам