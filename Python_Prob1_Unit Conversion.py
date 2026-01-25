def convert(value, from_unit, to_unit, category): #category can be 'length', 'weight', 'temperature'
    units = { #dictionary of conversion factors
        'length': {'m':1, #base unit is meter            
                   'cm':0.01, #centimeter to meter
                   'mm':0.001,
                   'km':1000,
                   'ft':0.3048,
                   'in':0.0254,
                   'yd':0.9144,
                   'mi':1609.34
                   },
        'weight': {'kg':1, #base unit is kilogram
                   'g':0.001,
                   'lb':0.453592
                  }
            }

    if category == "temperature":
      if from_unit == '°C' and to_unit == '°F':    
        return (value * 9/5) + 32 #C to F
      elif from_unit=='°F' and to_unit=='°C':
        return (value - 32) * 5/9 #F to C
      else:
        raise ValueError("Invalid units for temperature conversion")  
                       
    #Normal Conversion
    base_value = value * units[category][from_unit] 
    return base_value / units[category][to_unit]


def choose_category():
    categories = ['length', 'weight', 'temperature']
    print("Avalailable category:")
    for i, cat in enumerate(categories, start=1):
        print(f"- {i}: {cat}")
    return categories


def get_unit_options(category):
    if category == 'length':
        return ["m", "cm", "mm", "km", "ft", "in", "yd", "mi"]
    elif category == 'weight':
        return ["kg", "g", "lb"]
    elif category == 'temperature':
        return ["°C", "°F"]
   
    
def choose_unit(unit_list, label): #label can be 'from' or 'to'
    print(f"\nChoose {label} units:")
    for i, unit in enumerate(unit_list, start=1):
        print(f"- {i}: {unit}")

    choice= int(input("Enter number: "))
    return unit_list[choice - 1]




#________________________________MAIN PROGRAM___________________________#


if __name__ == "__main__":
    choose_category()
cat_choice= int(input("Enter the category number: "))
category = choose_category()[cat_choice - 1]

unit_list = get_unit_options(category)
from_unit = choose_unit(unit_list, "FROM")
to_unit = choose_unit(unit_list, "TO")

Value= float(input("Enter the value to convert: "))
result = convert(Value, from_unit, to_unit, category)
print(f"{Value} {from_unit} = {result:.2f} {to_unit}")
