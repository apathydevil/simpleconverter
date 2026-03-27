
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }
    
    value_in_meters = value * conversion_factors[from_unit]
    
    converted_value = value_in_meters / conversion_factors[to_unit]
    
    return converted_value

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'gram': 1,
        'ton': 1e6,
        'kilogram': 1000,
        'milligram': 0.001,
        'pound': 453.592,
        'ounce': 28.3495
    }
    
    value_in_grams = value * conversion_factors[from_unit]
    
    converted_value = value_in_grams / conversion_factors[to_unit]
    
    return converted_value

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    
    raise ValueError("Invalid temperature units")