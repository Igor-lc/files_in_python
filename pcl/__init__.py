class Auto:
    def __init__(self, mark, model, year, power):
        self.mark = mark
        self.model = model
        self.year = year
        self.power = power

    def __str__(self):
        return "Автомобиль {} {}, {} г. Мощность {} лс.".format(
            self.mark, self.model, self.year, self.power
        )


