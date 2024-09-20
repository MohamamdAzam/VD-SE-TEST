import pandas as pd
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def clean_user_data(input_file, output_file):
    df = pd.read_csv(input_file)

    df = df.drop_duplicates(subset='user_id')

    df = df[df['email'].apply(is_valid_email)]

    df.to_csv(output_file, index=False)

    return f"Successfully cleaned data and saved to {output_file}"


input_file = 'ques_2_input_output_files/user_data.csv'
output_file = 'ques_2_input_output_files/cleaned_user_data.csv'


success_message = clean_user_data(input_file, output_file)
print(success_message)
