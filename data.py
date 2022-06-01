from faker import Faker
fake = Faker()

def get_register_data():
    return {
        "name":fake.name(),
        "address":fake.address(),
        "created_at":fake.year()
    }

if __name__ == "__main__":
    print(get_register_data())