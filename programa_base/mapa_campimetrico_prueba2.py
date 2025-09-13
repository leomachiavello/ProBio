import numpy as np
import matplotlib.pyplot as plt
import json
from matplotlib.backends.backend_pdf import PdfPages

def leer_datos_json(archivo):
    """Lee los datos de un archivo JSON y devuelve una matriz de 8x9 con los valores de Total Deviation"""
    with open(archivo, 'r') as f:
        json_data = json.load(f)
    
    matriz = np.zeros((8, 9))  # Matriz de 8x9 (filas Y, columnas X), inicialmente con ceros
    
    # Recorrer los datos y llenar la matriz
    for y in range(8):
        for x in range(9):
            valor = json_data['td'][y][x]
            
            # Asignar NaN a las zonas fuera del rango (100.0)
            if valor == 100.0:
                matriz[y, x] = np.nan  # Marcar como NaN (fuera de rango)
            else:
                matriz[y, x] = valor  # Colocamos el valor de dB en la matriz

    return matriz

def graficar_mapa_color(matriz):
    """Genera un mapa de calor basado en la matriz de Total Deviation con ciertos recuadros en blanco"""
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('white')  # Establecer el fondo blanco
    
    # Usamos el colormap 'coolwarm' y configuramos NaN para ser blanco
    cmap = plt.get_cmap('coolwarm')
    cmap.set_bad('white')  # Los valores NaN (fuera de rango) serán blancos
    
    # Crear el gráfico con el colormap y mostrar los valores NaN en blanco
    cax = ax.imshow(matriz, cmap=cmap, interpolation='nearest', aspect='auto', vmin=-35, vmax=5)
    
    # Añadir colorbar
    cbar = fig.colorbar(cax)
    cbar.set_label("Total Deviation (dB)", rotation=270, labelpad=15)
    
    # Títulos y etiquetas
    ax.set_title("Mapa Campimétrico - Total Deviation")
    ax.set_xlabel("Coordenada X (0-8)")
    ax.set_ylabel("Coordenada Y (0-7)")
    
    # Configurar los ticks para que coincidan con las coordenadas
    ax.set_xticks(np.arange(-0.5, 9, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=0.5)
    ax.set_xticks(np.arange(0, 9))
    ax.set_yticks(np.arange(0, 8))
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
    
    return fig

def graficar_mapa_numeros_L(matriz):
    """Genera un mapa de la matriz con los valores numéricos en cada celda, con fondo blanco"""
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('white')  # Establecer el fondo blanco
    
    # Crear una matriz de fondo blanco
    ax.imshow(np.ones_like(matriz), cmap='gray', interpolation='nearest', aspect='auto', vmin=0, vmax=1)
    
    # Colocar los números en cada celda
    for y in range(8):
        for x in range(9):
            # Si el valor es NaN (fuera de rango), no colocar texto
            if not np.isnan(matriz[y, x]):
                ax.text(x, y, f'{matriz[y, x]:.2f}', ha='center', va='center', color='black', fontsize=12)
    
    # Títulos y etiquetas
    ax.set_title("Mapa Campimétrico - Total Deviation")
    ax.set_xlabel("Coordenada X (0-8)")
    ax.set_ylabel("Coordenada Y (0-7)")
    
    # Configurar los ticks para que coincidan con las coordenadas
    ax.set_xticks(np.arange(0, 9))
    ax.set_yticks(np.arange(0, 8))

    # Línea horizontal en el medio
    ax.axhline(y=3.5, color='black', linewidth=1)

    # Línea vertical en el medio
    ax.axvline(x=4.5, color='black', linewidth=1)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
    
    return fig

def graficar_mapa_numeros_R(matriz):
    """Genera un mapa de la matriz con los valores numéricos en cada celda, con fondo blanco"""
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('white')  # Establecer el fondo blanco
    
    # Crear una matriz de fondo blanco
    ax.imshow(np.ones_like(matriz), cmap='gray', interpolation='nearest', aspect='auto', vmin=0, vmax=1)
    
    # Colocar los números en cada celda
    for y in range(8):
        for x in range(9):
            # Si el valor es NaN (fuera de rango), no colocar texto
            if not np.isnan(matriz[y, x]):
                ax.text(x, y, f'{matriz[y, x]:.2f}', ha='center', va='center', color='black', fontsize=12)
    
    # Títulos y etiquetas
    ax.set_title("Mapa Campimétrico - Total Deviation")
    ax.set_xlabel("Coordenada X (0-8)")
    ax.set_ylabel("Coordenada Y (0-7)")
    
    # Configurar los ticks para que coincidan con las coordenadas
    ax.set_xticks(np.arange(0, 9))
    ax.set_yticks(np.arange(0, 8))

    # Línea horizontal en el medio
    ax.axhline(y=3.5, color='black', linewidth=1)

    # Línea vertical en el medio
    ax.axvline(x=3.5, color='black', linewidth=1)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
    
    return fig

def main():
    archivo = 'datos.json'  # Nombre del archivo
    matriz = leer_datos_json(archivo)  # Lee los datos del JSON
    
    # Crear un archivo PDF para guardar todos los gráficos
    with PdfPages('mapas_campimetricos_resultados.pdf') as pdf:
        # Habilitar el modo interactivo para que ambas ventanas se abran simultáneamente
        plt.ion()  # Modo interactivo
        
        # Graficar y guardar el mapa de color
        fig_color = graficar_mapa_color(matriz)
        pdf.savefig(fig_color)
        #plt.close(fig_color)
        
        # Graficar y guardar el mapa numérico para ojo izquierdo
        fig_numeros_L = graficar_mapa_numeros_L(matriz)
        pdf.savefig(fig_numeros_L)
        #plt.close(fig_numeros_L)
        
        # Deshabilitar el modo interactivo si es necesario
        plt.ioff()  # Modo interactivo desactivado
    
    print("Los gráficos se han guardado en 'mapas_campimetricos.pdf'")

if __name__ == "__main__":
    main()
