from crewai import Task, Crew
from email_service import send_email
from excel_reader import read_excel
from llm_api import generate_email

def automation():
    df = read_excel("data.xlsx")

    for index, row in df.iterrows():
        try:
            email = row["Email"]
            company = row["Company Name"]
            person = row["Person Name"]
            about = row["About Person"]
            service = row["Service"]

            email_body = generate_email(company, person, about, service)
            task = Task(send_email, args=[email, "Collaboration Proposal", email_body])
            crew = Crew(tasks=[task])
            crew.kickoff()
        except KeyError as e:
            print(f"Missing column: {e}")