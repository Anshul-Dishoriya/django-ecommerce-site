# Data Cleaning Function
class K_Nearest_Neighbor():
    def __init__(self):
        self.target = 0
        self.output = []

    def clean_data(self, data):
        all_categories = {
            "sports": 0,
            "gaming": 0,
            "cosmetics": 0,
            "food": 0,
            "electronic": 0,
            "mobile": 0,
            "cloths": 0,
        }
        for i in data.split():
            if all_categories.get(i)==0:
                all_categories[i] = 1
        return all_categories.values()

    def fit(self, data):
        x = 0
        for i in data:
            x = self.clean_data(i[1])
            x = sum(x)
        self.target = x/len(data)

    # machine learning model
    def predict(self, data):
        for i in data:
            x = self.clean_data(i[1])
            self.output.append([i[0] , sum(x)])

        for i in self.output:
            i = [ i[0] , abs(i[1]-self.target) ]


        self.output.sort(key=lambda x : x[1])
        return self.output[:5]
