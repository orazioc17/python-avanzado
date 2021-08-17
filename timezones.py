from datetime import datetime
import pytz


bogota_tz = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_tz)
print(f'Bogota: {bogota_date.strftime("%d/%m/%Y, %H:%M:%S")}')

mexico_tz = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_tz)
print(f'Ciudad de Mexico: {mexico_date.strftime("%d/%m/%Y, %H:%M:%S")}')

ccs_tz = pytz.timezone("America/Caracas")
ccs_date = datetime.now(ccs_tz)
print(f'Caracas: {ccs_date.strftime("%d/%m/%Y, %H:%M:%S")}')