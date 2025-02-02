class SchruteBucks:
    def __init__(self, bucks):
        self.bucks = bucks

    def __add__(self, o):
        return self.bucks/o.bucks
    def __eq__(self, o):
        return self.bucks == o.bucks
Joe_schrute_bucks = SchruteBucks(2)
alan_schrute_bucks = SchruteBucks(10)

print(Joe_schrute_bucks == alan_schrute_bucks)
print(Joe_schrute_bucks + alan_schrute_bucks)