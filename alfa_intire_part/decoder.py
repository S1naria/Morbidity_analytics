import numpy as np


class Decoder():
    def __init__(self, disease_count, staff_count, parametres):
        self.disease_count = self.__separate_by_disease(disease_count, parametres);
        self.staff_count = staff_count;
        self.parametres = parametres;
        self.result = {}


    def __separate_by_disease(self, disease_count, parametres):
        result = {};
        column_name = list(parametres.filters.keys())[0];
        for i in range(len(disease_count)):
            result[parametres.filters[column_name][i]] = disease_count[i];
        return result;

    
    def __create_category(self):
        self.staff_count = self.__flatten_array(self.staff_count)
        for i in self.disease_count:
            self.disease_count[i] = self.__flatten_array(self.disease_count[i])
            self.disease_count[i] = [round(a / b*1000) if b != 0 else 0 for a, b in zip(self.disease_count[i], self.staff_count)]
        
    def get_morbidity(self):
        self.__create_category()
        array = list(self.parametres.filters.values())[1:]
        combinations = self.generate_combinations(array)
        for i in self.disease_count:
            self.disease_count[i] = dict(zip(combinations, self.disease_count[i]))
        return self.disease_count

    def generate_combinations(self, arrays, current_combination=[], index=0, result=[]):
        if index == len(arrays):
            result.append(' '.join(map(str, current_combination)))
        else:
            for item in arrays[index]:
                self.generate_combinations(arrays, current_combination + [item], index + 1, result)
        return result

    def __flatten_array(self, arr):
        flat_list = []
        for element in arr:
            if isinstance(element, list):
                flat_list.extend(self.__flatten_array(element))
            else:
                flat_list.append(element)
        return flat_list
    
    