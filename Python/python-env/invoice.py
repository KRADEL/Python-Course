class Invoice:
# Self References the particular instance
    def greeting(self):
        return 'Hi There'


# Instantiation
inv_one = Invoice()
print(inv_one.greeting())