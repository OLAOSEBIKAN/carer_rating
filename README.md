# carer_rating
Scoring System: The proposed scoring system consists of five factors that are combined to calculate the final score for each carer. These factors include:

Weighted Average Review Score: This factor considers the review scores provided by previous clients. The scores are weighted lower for carers with image problems, and the weighted score is calculated by subtracting the number of image problems from 8 and dividing by 8.

Carer Type: Carers are categorized into three types: basic, advanced, and expert. Each type gets a different score; expert carers get a 10%, advanced carers get a 5%, and basic carers get no score.

Previous Clients: This factor considers the number of previous clients a carer has had. The score is calculated as (number of previous clients / (number of previous clients + 5)) * 100. This penalizes carers who have had a lot of previous clients, as they may not have as much availability.

Login Score: This factor considers the number of days since a carer last logged in. Carers who have logged in more recently are more likely to be available and responsive to new clients. The bonus is calculated as (30 - days since login) / 30 * 100. If the carer has not logged in for more than 30 days, the score is 0.

Experience Score: This factor considers the years of experience a carer has. More experienced carers may be more knowledgeable and better equipped to handle a variety of situations. The score is calculated as (years of experience / 10) * 100.
