import pandas as pd;


#Класс получает на вход: датафрейм для деления, класс с параметрами, а также текущие оставшиеся  параметры
class Tree:
    def __init__(self, df, parameters, currency_filters):
        self.df = df;
        self.parameters = parameters;
        self.filters = currency_filters;
        self.leafs = [];

    #Функция создает внутри несколько объектов собственного класса,
    # если есть параметры для деления то заносит их в список leafs.
    # В противном случае возвращает количество строк в дата фрейме (чатай итоговое количество людей в заданной группе)
    def __separate_by_parametres(self):
        #Получили параметр, по которому мы планируем делать разделение
        key_for_separate = self.filters[0];
        #Создаем новые параметры, исключив тот фильтр, который мы использовали
        new_filters = self.filters[1:];
        #Добавляем в leafs листья, деленные по параметру
        for value in self.parameters.filters[key_for_separate]:
            leaf = Tree(self.df.loc[self.df[key_for_separate] == value], self.parameters, new_filters);
            self.leafs.append(leaf);

    def get_count_in_group(self):
        if not self.filters:
            return self.df.shape[0]
        nums = []
        self.__separate_by_parametres()
        for leaf in self.leafs:
            nums.append(leaf.get_count_in_group())
        return nums