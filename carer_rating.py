import csv
from typing import List, Dict


class Carer_Rating:
    """
    A class for loading and sorting carer data from a CSV file using a proposed scoring system.

    Attributes:
    -----------
    carers_file : str
        The name of the CSV file containing the carer data.

    Methods:
    --------
    load_carers_data()
        Loads the carer data from the CSV file and stores it as a list of dictionaries.

    sort_carers_by_score()
        Sorts the carers by their overall score, calculated using the proposed scoring system.

    write_sorted_carers_to_csv(filename)
        Writes the sorted carer data back to a CSV file.

    """

    def __init__(self, csv_file: str, test_carer=None):
        self.file = csv_file
        self.carers = []
        self.test_carer = test_carer

    def load_carers(self) -> List[Dict]:
        """
        Loads a list of carers from a CSV file.
        """
        with open(self.file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["num_reviews"] = int(row["num_reviews"])
                row["avg_review"] = float(row["avg_review"])
                row["img_problems"] = int(row["img_problems"])
                row["num_previous_clients"] = int(row["num_previous_clients"])
                row["days_since_login"] = int(row["days_since_login"])
                row["age"] = int(row["age"])
                row["years_experience"] = int(row["years_experience"])
                self.carers.append(row)
        return self.carers

    def calculate_weighted_review_score(self, num_reviews: int, avg_review: float, img_problems: int) -> float:
        """
        Calculates the weighted average review score for a carer, weighting it lower for carers with image problems.
        """
        weighted_review_score = ((8 - img_problems) / 8) * avg_review
        return weighted_review_score

    def calculate_type(self, carer_type: str) -> float:
        """
        scoring carers based on their career type with expert as highest.
        """
        if carer_type == "expert":
            type_bonus = 0.1
        elif carer_type == "advanced":
            type_bonus = 0.05
        else:
            type_bonus = 0
        return type_bonus

    def previous_clients(self, num_previous_clients: int) -> float:
        """
        Calculates the point based on the number of previous clients.
        """
        previous_client = (num_previous_clients /
                           (num_previous_clients + 5)) * 100
        return previous_client

    def calculate_login_bonus(self, days_since_login: int) -> float:
        """
        Calculates the bonus based on the number of days since the carer last logged in.
        """
        if days_since_login > 30:
            login_bonus = 0
        else:
            login_bonus = ((30 - days_since_login) / 30) * 100
        return login_bonus

    def calculate_experience(self, years_experience: int) -> float:
        """
        Calculates the point based on the years of experience.
        """
        experience_bonus = (years_experience / 10) * 100
        return experience_bonus

    def calculate_carer_score(self, carer: Dict) -> float:
        """
        Calculates the overall score for a carer using the proposed system.
        """
        weighted_review_score = self.calculate_weighted_review_score(
            carer["num_reviews"], carer["avg_review"], carer["img_problems"])
        type_bonus = self.calculate_type(carer["type"])
        previous_client_point = self.previous_clients(
            carer["num_previous_clients"])
        login_bonus = self.calculate_login_bonus(carer["days_since_login"])
        experience_bonus = self.calculate_experience(carer["years_experience"])
        carer_score = weighted_review_score + type_bonus + \
            login_bonus + experience_bonus - previous_client_point
        print(f'{carer["id"]}, {carer["first_name"]}, {carer_score}')
        return carer_score

    def write_carers_to_csv(self, filename: str, carers: List[Dict]) -> None:
        """
        Writes a list of carers to a CSV file.
        """
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["first_name", "last_name", "type", "num_reviews", "avg_review", "img_problems", "num_previous_clients",
                            "days_since_login", "age", "years_experience"])
            for carer in carers:
                writer.writerow([carer["first_name"], carer["last_name"], carer["type"], carer["num_reviews"], carer["avg_review"],
                                carer["img_problems"], carer["num_previous_clients"], carer["days_since_login"],
                                carer["age"], carer["years_experience"]])

    def sort_carers_by_score(self) -> List[Dict]:
        """
        Sorts a list of carers by their overall score in descending order.
        """
        sorted_carers = sorted(self.carers, key=lambda x: self.calculate_carer_score(x), reverse=True)
        self.write_carers_to_csv('sorted_carers.csv', sorted_carers)
        return sorted_carers
    
rating = Carer_Rating('data.csv')
rating.load_carers()
rating.sort_carers_by_score()
