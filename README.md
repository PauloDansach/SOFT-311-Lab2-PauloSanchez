Casos de Prueba: Home

TC-001: Carga y Renderizado de la pagina principal:

Objetivo: Verificar que el homepage carga completamente todos sus elementos visuales y contenido disponibles para el usuario.
Pasos:
1.	Abrir el navegador y navegar a https://storedemo.testdino.com/
2.	Esperar a que el DOM esté completamente cargado (networkidle)
3.	Verificar que el título del documento contiene 'TestDino'
4.	Verificar que el logo del sitio es visible en el encabezado
5.	Verificar que existe al menos un producto visible en la sección principal
Resultado:
La página carga en menos de 3 segundos, el logo es visible, el título es correcto y al menos un producto está renderizado en pantalla.

TC-002: Navegación desde home a categorías de productos
Objetivo: Confirmar que los enlaces de categorías del menú o banner redirigen al listado de productos correspondiente. 
Pasos:
1.	Navegar a https://storedemo.testdino.com/
2.	Localizar el menú de navegación o banner de categorías
3.	Hacer clic en una categoría disponible (ej. Laptops)
4.	Esperar la navegación o actualización de contenido
5.	Verificar que la URL o el título de sección refleja la categoría seleccionada
6.	Verificar que los productos listados pertenecen a dicha categoría
Resultado: El usuario es redirigido a la sección de categoría correcta y los productos mostrados corresponden a la categoría seleccionada.

TC-003: Búsqueda de producto desde el homepage
Objetivo: Validar que el searchbar retorna resultados relevantes según el término ingresado.
Paso:
1.	Navegar a https://storedemo.testdino.com/
2.	Localizar el campo de búsqueda en el encabezado
3.	Ingresar el término 'laptop'
4.	Enviar la búsqueda (tecla Enter o botón de buscar)
5.	Verificar que se muestran resultados en pantalla
6.	Verificar que los títulos de los productos contienen o están relacionados con 'laptop'
Resultado: Se muestran uno o más productos cuyos nombres o descripciones están relacionados con el término buscado. No se muestra página de error.

Casos de Prueba: Login
TC-004: Inicio de sesión con credenciales válidos
Objetivo: Confirmar que un usuario con credenciales correctas puede autenticarse y acceder a su sesión.
Pasos:
1.	Navegar al formulario de login del sitio
2.	Ingresar un email registrado válido (ej. user@test.com)
3.	Ingresar la contraseña correcta
4.	Hacer clic en el botón 'Login' o 'Sign In'
5.	Esperar redirección post-login
6.	Verificar que el nombre del usuario o indicador de sesión activa aparece en el encabezado
Resultado: El usuario es autenticado correctamente, es redirigido al homepage o perfil y se muestra un indicador de sesión activa (nombre, avatar o botón de logout).

TC-005: Login con credenciales inválidos
Objetivo: Verificar que el sistema rechaza credenciales incorrectas y notifica al usuario con un mensaje claro.
Pasos:
1.	Navegar al formulario de login
2.	Ingresar un email válido en formato (ej. user@test.com)
3.	Ingresar una contraseña incorrecta (ej. wrongpass123)
4.	Hacer clic en el botón 'Login'
5.	Esperar respuesta del sistema
6.	Verificar que aparece un mensaje de error en pantalla
7.	Verificar que el usuario no es redirigido a ninguna página protegida
Resultado: Se muestra un mensaje de error (ej. 'Credenciales inválidas') y el usuario permanece en la página de login sin acceso a ninguna sección autenticada.

TC-006: Campos requeridos vacíos bloquean el envío
Objetivo: Asegurar que el formulario de login no permite enviarse cuando los campos obligatorios están vacíos.
Pasos:
1.	Navegar al formulario de login
2.	Dejar ambos campos (email y contraseña) completamente vacíos
3.	Hacer clic en el botón 'Login'
4.	Observar el comportamiento del formulario
5.	Verificar que no se realiza ninguna petición de red al servidor
6.	Verificar que se muestran mensajes de validación en los campos
Resultado: El formulario no se envía, aparecen mensajes de validación en los campos vacíos y no se realiza ninguna petición HTTP al servidor.

Casos de Prueba: Sign Up
TC-007: Registro exitoso con datos válidos
Objetivo: Confirmar que un nuevo usuario puede crear una cuenta completando correctamente todos los campos requeridos.
Pasos:
1.	Navegar al formulario de registro (Sign Up)
2.	Ingresar un nombre completo (ej. Test User)
3.	Ingresar un email único no registrado (ej. newuser_123@test.com)
4.	Ingresar una contraseña válida que cumpla los requisitos
5.	Confirmar la contraseña si el campo existe
6.	Hacer clic en el botón de registro
7.	Verificar la respuesta del sistema
Resultado: El sistema crea la cuenta exitosamente, muestra un mensaje de confirmación o redirige al usuario al login/home con sesión iniciada.

TC-008: Registro con email ya existente muestra error
Objetivo: Verificar que el sistema detecta emails duplicados y notifica al usuario sin crear una cuenta repetida.
Pasos: 
1.	Navegar al formulario de registro
2.	Ingresar el nombre del usuario
3.	Ingresar un email que ya esté registrado en el sistema
4.	Ingresar una contraseña válida
5.	Hacer clic en el botón de registro
6.	Verificar la respuesta del sistema
Resultado: El sistema muestra un mensaje de error indicando que el email ya está en uso (ej. 'Este correo ya está registrado') y no crea una cuenta duplicada.

TC-009: Formato de email inválido bloquea el registro
Objetivo: Asegurar que el campo de email valida el formato correcto antes de permitir el envío del formulario.
Pasos: 
1.	Navegar al formulario de registro
2.	Ingresar un nombre válido
3.	Ingresar un email con formato incorrecto (ej. usuariotest.com o usuario@)
4.	Ingresar una contraseña válida
5.	Hacer clic en el botón de registro
6.	Observar el comportamiento del campo de email
Resultado: El formulario no se envía, el campo de email muestra un mensaje de validación de formato (ej. 'Ingresa un email válido') y no se crea ninguna cuenta.

Casos de Prueba: Cart
TC-010: Agregar un producto al carrito
Objetivo: Confirmar que el botón 'Add to cart' agrega correctamente un producto al carrito y actualiza el contador.
Pasos:
1.	Navegar a la home o listado de productos
2.	Seleccionar un producto disponible
3.	Hacer clic en el botón 'Add to cart'
4.	Verificar que el contador del ícono de carrito en el encabezado aumenta en 1
5.	Navegar a la vista del carrito
6.	Verificar que el producto agregado aparece en la lista con nombre y precio correcto
Resultados: El producto aparece en el carrito con el nombre, imagen y precio correctos. El contador del encabezado refleja la cantidad actualizada.

TC-011: Eliminar un producto del carrito
Objetivo: Verificar que al eliminar un producto del carrito este desaparece de la lista y el total se recalcula correctamente.
Pasos: 
1.	Agregar al menos un producto al carrito
2.	Navegar a la vista del carrito
3.	Localizar el botón de eliminar (ícono de papelera o texto 'Remove') del producto
4.	Hacer clic en el botón de eliminar
5.	Verificar que el producto ya no aparece en la lista del carrito
6.	Verificar que el total del carrito se ha actualizado
Resultados: El producto eliminado desaparece del carrito, el contador del encabezado disminuye y el total monetario se recalcula correctamente.

TC-012: Total del carrito refleja cantidad y precio correctos
Objetivos: Validar que el cálculo del subtotal y total del carrito es matemáticamente correcto según los productos y cantidades ingresadas.
Pasos:
1.	Agregar dos o más productos distintos al carrito
2.	Navegar a la vista del carrito
3.	Anotar el precio unitario y cantidad de cada producto
4.	Calcular manualmente el total esperado (precio × cantidad por ítem, sumados)
5.	Comparar el total calculado con el total mostrado en pantalla
6.	Si existe campo de cantidad, modificar la cantidad de un producto y verificar que el total se actualiza
Resultados: El total mostrado en el carrito coincide exactamente con la suma de (precio × cantidad) de cada producto. La actualización de cantidades refleja cambios en tiempo real.

Caso de Pruebas: Favorites
TC-013: Agregar producto a favoritos
Objetivos: Confirmar que el usuario puede marcar un producto como favorito y que este queda guardado en su lista de favoritos.
Pasos:
1.	Iniciar sesión con un usuario válido
2.	Navegar a la home o listado de productos
3.	Localizar el ícono de corazón en un producto
4.	Hacer clic en el ícono de corazón
5.	Verificar que el ícono cambia de estado (de vacío a relleno o cambia de color)
6.	Navegar a la sección de Favorites
7.	Verificar que el producto marcado aparece en la lista
Resultados: El ícono del corazón cambia visualmente al estado activo y el producto aparece correctamente en la sección de Favorites del usuario.

TC-014: Eliminar producto de favoritos
Objetivos: Verificar que el usuario puede quitar un producto de su lista de favoritos y que este deja de aparecer en dicha sección.
Pasos:
1.	Iniciar sesión con un usuario que tenga al menos un favorito guardado
2.	Navegar a la sección de Favorites
3.	Localizar el producto a eliminar
4.	Hacer clic en el ícono de corazón activo o botón de eliminar
5.	Verificar que el ícono vuelve al estado inactivo
6.	Verificar que el producto ya no aparece en la lista de favoritos
Resultados: El producto es removido de la lista de favoritos, el ícono de corazón regresa a estado inactivo y la lista de Favorites se actualiza sin recargar la página.

TC-015: Favoritos requieren sesión active
Objetivo: Verificar que un usuario no autenticado no puede agregar favoritos y es redirigido al flujo de autenticación.
Pasos:
1.	Asegurar que no existe sesión activa (cerrar sesión si aplica)
2.	Navegar a la home o listado de productos
3.	Localizar el ícono de corazón de cualquier producto
4.	Intentar hacer clic en el ícono de corazón
5.	Observar el comportamiento del sistema
6.	Verificar si aparece un modal de login, una redirección o un mensaje de aviso
Resultados: El sistema no agrega el producto a favoritos; en su lugar muestra un mensaje solicitando autenticación, un modal de login o redirige al usuario a la página de login.

