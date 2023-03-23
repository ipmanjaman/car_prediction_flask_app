class Customers():
    columns = ['id','age','annual_salary', 'credit_card_debit', 'net_worth']
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
