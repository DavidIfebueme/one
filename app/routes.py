from flask import Blueprint, request, Response, json
import requests
from app.utils import is_prime, is_perfect, is_armstrong, get_digit_sum, get_number_properties

number_blueprint = Blueprint("number", __name__)

@number_blueprint.route('/classify-number', methods=['GET'])
def classify_number():
    number_parameter = request.args.get('number')  
    
    if not number_parameter or not number_parameter.lstrip("-").isdigit():
        response_data = {"number": "alphabet", "error": True}
        response = Response(response=json.dumps(response_data, indent=2, sort_keys=False), mimetype='application/json')
        return response, 400
    
    number = int(number_parameter)
    
    fun_fact = get_fun_fact(number) # if the integer is negative, the numbers api will have no fun fact for it sooooo no be my fault
    properties = get_number_properties(abs(number)) #have to get abs value negative armstrong numbers do not exist soooo once again no be my fault 
    
    response_data = {
        "number": number,
        "is_prime": is_prime(number) if number > 1 else False,
        "is_perfect": is_perfect(number) if number > 0 else False,
        "properties": properties,
        "digit_sum": get_digit_sum(abs(number)),
        "fun_fact": fun_fact
    }
    response = Response(response=json.dumps(response_data, indent=2, sort_keys=False), mimetype='application/json')
    return response, 200

def get_fun_fact(number):
    try:
        url = f"http://numbersapi.com/{number}/math"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return "No fun fact available."
    except requests.RequestException:
        return "Could not fetch fun fact."
