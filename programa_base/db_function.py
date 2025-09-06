import math

I_0 = 1e-6 # intensidad de referencia

def alpha_to_db(alpha):
    if alpha < 0: alpha = 0
    if alpha > 255: alpha = 255
    
    # Calcular la intensidad luminosa a partir de alfa
    intensity = alpha / 255  # Intensidad entre 0 y 1
    
    # Usamos un valor mínimo de intensidad para evitar log(0)
    intensity = max(intensity, I_0)  # Aseguramos que la intensidad no sea 0
    
    # Calcular los decibelios
    db = 10 * math.log10(intensity / I_0)
    return db

def db_to_alpha(db):
    
    # Calcular la intensidad luminosa a partir de los decibelios
    intensity = I_0 * 10 ** (db / 10)
    
    # Convertir la intensidad luminosa a alfa (opacidad entre 0 y 255)
    alpha = round(intensity * 255)
    
    # Asegurarse de que el valor de alpha esté en el rango 0-255
    alpha = max(0, min(alpha, 255))
    
    return alpha

print(alpha_to_db(0))
print(alpha_to_db(100))
print(alpha_to_db(255))
print()
print(db_to_alpha(30))
print(db_to_alpha(55.934))
print(db_to_alpha(60))