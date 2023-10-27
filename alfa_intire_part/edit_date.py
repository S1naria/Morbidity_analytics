import pandas as pd
from parameters import Parameters
from tree import Tree
from decoder import Decoder
from graph import Graphic


#Класс датафрейм
class Dataset:
    def __init__(self, child_file_path: str, parent_file_path : str, columns_to_find: list = None):
        #Принимает путь до файла первым параметром
        #Принимает колонки, по которым нужно искать дубликаты, чтобы удалить повторы
        #В итоге получаем чистый датафрейм, без дубликатов
        try:
            self.df_child = pd.read_excel(child_file_path)
            if columns_to_find:
                self.df_child.drop_duplicates(subset=columns_to_find, inplace=True)
        except Exception as e:
            raise ValueError(f"Failed to load data from {child_file_path}: {str(e)}")
        
        try:
            self.df_parents = pd.read_excel(parent_file_path)
        except Exception as e:
            raise ValueError(f"Failed to load data from {parent_file_path}: {str(e)}")
        

    #Создается класс параметров, по которым произойдет деление
    def __create_parameters(self, columns_for_separate: list):
        columns_id = self.__get_columns_id(columns_for_separate);
        unique_values = self.__get_unique_values(columns_for_separate);
        return Parameters(unique_values, columns_id)

    # Получаем id колонок (словарь)
    def __get_unique_values(self, columns_name):
        unique_values = {};
        for column in columns_name:
            unique_values[column] = self.df_child[column].unique().tolist(); 
        return unique_values;

    # Получаем уникальные значения по каждой колонке (словарь)
    def __get_columns_id(self, columns_name):
        columns_id = {};
        for column in columns_name:
            columns_id[column] = self.df_child.columns.get_loc(column);
        return columns_id;

    def __get_trees(self, columns_for_separate: list):
        settings = self.__create_parameters(columns_for_separate);
        tree_child = Tree(self.df_child, settings, columns_for_separate);
        tree_parents = Tree(self.df_parents, settings, columns_for_separate[1:]);
        return (tree_child, tree_parents);

    def get_graphics_with_parametres(self, columns_for_separate):
        first_tree, second_tree = self.__get_trees(columns_for_separate)
        dc = Decoder(first_tree.get_count_in_group(), second_tree.get_count_in_group(), first_tree.parameters)
        data = dc.get_morbidity()
        gr = Graphic(data)
        gr.create_graphic()
