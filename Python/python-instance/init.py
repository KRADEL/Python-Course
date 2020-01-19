class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

# GETTER METHOD Java
    # def get_client():
        # return self.client

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)
# print(google.formatter())

print(google.client)

# SETTER PROCESS
google.client = 'Yahoo'

print(google.client)
