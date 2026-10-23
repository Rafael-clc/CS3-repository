class Patient:
    name: str
    bill_amount: float
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_bill_amount(self):
        return self._bill_amount

    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount

    def calculate_bill(self):
        return self._bill_amount


class SeniorPatient(Patient):
    calculate_bill: float
    def calculate_bill(self):
        return self._bill_amount * 0.80


class PhilHealthPatient(Patient):
    calculate_bill: float
    def calculate_bill(self):
        return self._bill_amount * 0.85
