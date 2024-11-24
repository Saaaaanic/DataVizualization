import pandas as pd
import random
from faker import Faker
import pycountry


class DataSimulator:
    def __init__(self, num_records=100):
        self.num_records = num_records
        self.faker = Faker()

    def generate_data(self):
        data = []
        for _ in range(self.num_records):
            latitude, longitude, city, country_code, timezone = self.faker.location_on_land()
            avatar = f"https://i.pravatar.cc/150?img={random.randint(1, 70)}"
            data.append({
                'Country': pycountry.countries.get(alpha_2=country_code).name,
                'City': city,
                'Avatar': avatar,
                'Latitude': latitude,
                'Longitude': longitude
            })

        return pd.DataFrame(data)
