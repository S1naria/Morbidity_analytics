import matplotlib.pyplot as plt

class Graphic:
    def __init__(self, data):
        self.data = data;

    def create_graphic(self):
        for graph_name, graph_data in self.data.items():
            plt.figure()
            plt.title(graph_name)
            
            columns = list(graph_data.keys())
            values = list(graph_data.values())
            
            for i in range(len(columns)):
                plt.bar(columns[i], values[i], label=columns[i])
                plt.text(columns[i], values[i], str(values[i]), ha='center', va='bottom')
            plt.xlabel('Параметры')  
            plt.ylabel('Заболеваемость')  
            plt.legend()
            plt.grid(True)
        plt.show()