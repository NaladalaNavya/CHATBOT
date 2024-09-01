from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import random
import ssl
import uvicorn

app = FastAPI()


@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']

    intent_handler_dict = {
        'course.price': handle_course_price,
        'eligibility.age': handle_eligibiliy_age,
        'eligibility.background': handle_eligibility_background
    }

    return intent_handler_dict[intent](parameters)


def handle_course_price(parameters: dict):
    course_name = parameters["course-name"]
    country = parameters["geo-country"]

    price_dict = {
        "SQL": 900,
        "Power BI": 2400,
        "Python": 800,
        "Excel": 700,
        "Data Analytics Bootcamp": 4800
    }

    course_price = price_dict.get(course_name)

    response = {
        "fulfillmentText": f"The course price for {course_name} is : {course_price}"
    }

    return JSONResponse(content=response)

def handle_eligibiliy_age(parameters: dict):
    course_name = parameters["course-name"]
    age = parameters["age"]["amount"]

    if age>30:
        answer = random.choice([
            '''
            In short: we believe it is possible to learn data analytics at this age 
            ''',
            '''
            Also one great thing about data analyst career is it requires very less coding so it will not 
            be very difficult for you! So yes, you can learn data analysis at your age.
            '''
        ])

    else:
        answer ="Your age is less than 30 and you are too young to learn anything. Just do it my friend."

    if course_name:
        answer += " And yes you are eligible for " + "".join(course_name)

    return JSONResponse(content={
        "fulfillmentText": answer
    })


def handle_eligibility_background(parameters: dict):
    course_name = parameters["course-name"]
    background = parameters["degree-or-situation"]

    if background:
        if background == "Mechanical Engineer":
            answer = '''I know many Mechanical Engineers who have successfully become data analysts.You need to learn necessary skills
            such as Excel, Power BI, SQL etc.  
            '''
        elif background == "B.COM":
            answer = '''There are many B.COM graduates who have transitioned into data analytics industry. 
            '''
        elif background == "HR":
            answer = '''If you are an HR trying to transition to data industry then I would suggest you leverage your past
            experience. 
            '''
        else:
            answer = '''There are many folks who have breaked into a data analyst career despite irrelavant degree, 
            work experience or an older age.
            If they can do it, you can do it too. 
            '''
        if course_name:
            answer += " And yes you are eligible for " + "".join(course_name)
    else:
        answer = f"To understand if you are eligible for {course_name} or not, you can take this survey. 

    response = {
        "fulfillmentText": answer
    }

    return JSONResponse(content=response)
