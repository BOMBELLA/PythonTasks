def convert_temperature(temperature_value, unit):
       unit = unit.upper()
       if unit == F:
              C = (F-32) * 5/9
              return C
       if unit == C
              F = (C*9/5) + 32 
              return F

def get_advisory(temperature_value, unit, threshold_temperature):
       temperature = convert_temperature(temperature_value, unit)
       threshold_value = convert_temperature(threshold_temperature)
       if temperature < threshold_value:
              return "Cold Advisory"
       if temperature > threshold_value:
              return "Heat Alert"
