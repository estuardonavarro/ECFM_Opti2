"""
Universidad de San Carlos de Guatemala
Escuela de Ciencias Físicas y Matemáticas
Licenciatura en Matemática Aplicada

(ME21) Optimización 2
Profesor: Lic. William Gutiérrez
Autor: Javier Navarro

----------------------------------------- Tarea lección 7 -------------------------------------
A continuación se muestra el desarrollo del método de la secante.

"""


def secante(g, a: float, b: float, e: float):
    """
    Este método aproxima la solución de g(x)=0 en el intervalo [a,b] utilizando el método de la secante.

    Parameters
    ----------
    g : función
        La función de la cual se desea aproximar su raíz g(x)=0.
    a,b : numbers
        El intervalo en el que se buscará la solución. Si no existe cambio de signo
        se devolverá None.
    e : epsilon>0
        Constante que forma parte del criterio para deterner el método

    Returns
    -------
    x_n : number
        El intercepto en x  de la recta secante
            x_n = a_n - g(a_n)*(b_n - a_n)/(g(b_n) - g(a_n))
        El intervalo inicial es [a_0,b_0] el cual coincide con [a,b]. If g(m_n) == 0
        for some intercept m_n then the function returns this solution.
        If all signs of values g(a_n), g(b_n) and g(m_n) are the same at any
        iterations, the secant method fails and return None.


    """
    # if g(a) * g(b) >= 0:
    #     print("El método falló pues no hay cambio de signo.")
    #     return None
    a_n = a
    b_n = b
    continuar = True
    while continuar:
        x_n = a_n - g(a_n) * (b_n - a_n) / (g(b_n) - g(a_n))
        g_x_n = g(x_n)
        if g(a_n) * g_x_n < 0:
            a_n = a_n
            b_n = x_n
        elif g(b_n) * g_x_n < 0:
            a_n = x_n
            b_n = b_n
        elif g_x_n == 0:
            print("Se encontró una solución exacta.")
            return x_n
        x_n_1 = a_n - g(a_n) * (b_n - a_n) / (g(b_n) - g(a_n))
        if abs(x_n_1 - x_n) < (abs(x_n) * e):
            return x_n_1


def funcion(x):
    """
        Se define g(x)=(2x - 1)^2 + 4(4 - 1024x)^4, puede ser cualquiera.
    """
    return (2 * x - 1) ** 2 + 4 * (4 - 1024 * x) ** 4


# Este es el método principal
if __name__ == '__main__':
    raiz = secante(funcion, 0, 1, 0.00001)
    print("La solución es: ", raiz)
    print("La imagen de la solución es: ", funcion(raiz))
