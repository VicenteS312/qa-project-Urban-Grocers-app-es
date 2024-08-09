import data
import sender_stand_request

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = name
    return current_kit_body
def positive_assert_for_kit_body(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_body['name']

def negative_assert_code_400(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

#1 El número permitido de caracteres (1)
def test_numero_permitido_de_caracteres_1():
    kit_body = get_kit_body("a")
    positive_assert_for_kit_body(kit_body)


#2 El número permitido de caracteres (511)
def test_numero_permitido_de_caracteres_511():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert_for_kit_body(kit_body)

# 3 El número de caracteres es menor que la cantidad permitida (0)
def test_numero_de_caracteres_no_permitido_0():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)
# Resultado Esperado = 400 Resultado Actual = 201; Se permitio crear un kit nombre con un numero de caracteres menor de lo permitido

#4 El número de caracteres es mayor que la cantidad permitida (512)
def test_numero_de_caracteres_no_permitido_512():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)
# Resultado Esperado = 400 Resultado Actual = 201; Se permitio crear un kit nombre con un numero de caracteres mayor de lo permitido

#5 Se permiten caracteres especiales
def test_caracteres_especiales_kit_body_201():
    kit_body = get_kit_body("\"№%@\",")
    positive_assert_for_kit_body(kit_body)

#6 Se permiten espacios
def test_espacios_en_kit_nombre_201():
    kit_body = get_kit_body("A Aaa")
    positive_assert_for_kit_body(kit_body)

#7 Se permiten números
def test_numeros_en_kit_nombre_201():
    kit_body = get_kit_body("123")
    positive_assert_for_kit_body(kit_body)

#8 El parámetro no se pasa en la solicitud
def test_parametro_kit_name_ausente_400():
    kit_body = get_kit_body({})
    negative_assert_code_400(kit_body)
# Resultado Esperado = 400 Resultado Actual = 201; Se acepto la solicitud sin un parametro requerido

#9 Se ha pasado un tipo de parámetro diferente (número)
def test_parametro_no_valido_int_400():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
# Resultado Esperado = 400 Resultado Actual = 201; Se acepto un paramtero en forma de int y no de str