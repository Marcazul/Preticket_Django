# Preticket_Django
Aplicacion de Django

¡Bienvenido/a a mi aplicación desarrollada con Django!

Usuarios:

1. Acceso a Usuarios:
   - Botón "Usuarios" en la barra lateral izquierda o avatar en la esquina superior derecha.
   - Estos son los puntos de acceso para las funciones relacionadas con los usuarios.

2. Gestión de Usuarios:
   - Crear nuevos usuarios: Permite crear perfiles de usuario en el programa.
   - Iniciar sesión (Sign In): Permite a los usuarios autenticarse en el programa.
   - Cerrar sesión (Sign Out): Permite a los usuarios finalizar su sesión actual.
   - Ver lista de usuarios: Muestra una lista de todos los usuarios registrados.
   - Propiedades de la cuenta de cada usuario: Permite ver y administrar la configuración de cada cuenta de usuario.

3. Perfil de Usuario:
   - "Mi perfil": Permite acceder al perfil del usuario activo.
   - Enlace a LinkedIn: En el perfil del usuario activo, se muestra un enlace a su página de LinkedIn.
   - Si no hay usuarios registrados, se muestra la opción "Guest" en lugar del nombre del usuario.

4. Avatares de Usuario:
   - Cada usuario puede elegir un avatar para personalizar su cuenta.
   - El avatar seleccionado por cada usuario se muestra junto a su nombre en diferentes secciones del programa.

Clientes:

1. Listado de Clientes:
   - Muestra una lista de todos los clientes registrados.
   - Dentro del listado, se pueden realizar las siguientes acciones:
     - Editar datos (Update): Permite modificar la información del cliente.
     - Borrar (Delete): Permite eliminar el cliente de la lista.
   - Al hacer clic en el nombre del cliente, se muestra la siguiente información adicional:
     - Datos del cliente: Muestra los detalles del cliente, como nombre, dirección, contacto, etc.
     - Detalle de servicios y ventas: Muestra una lista de los servicios y ventas realizadas para ese cliente en particular.

2. Total de Ventas, Servicios y Ganancias:
   - Al final del listado de clientes, se muestra el total de ventas realizadas, el total de servicios proporcionados y la ganancia total generada a partir de esas transacciones.

3. Crear Cliente:
   - Permite crear nuevos clientes en el programa.
   - Al seleccionar esta opción, se abre un formulario donde se pueden ingresar los datos del nuevo cliente, como nombre, dirección, contacto, etc.

Ventas & Servicios:

1. Cargar Nuevos Servicios:
   - Permite registrar servicios realizados para un cliente específico.
   - Al seleccionar esta opción, se abrirá un formulario donde podrás ingresar los detalles del servicio, como nombre del servicio, fecha, duración, costo, etc.
   - Después de completar el formulario, podrás guardar la información del servicio y asociarlo al cliente correspondiente.

2. Cargar Nuevas Ventas:
   - Permite registrar ventas realizadas para un cliente en particular.
   - Al elegir esta opción, se abrirá un formulario donde podrás ingresar los detalles de la venta, como producto/servicio vendido, fecha, precio, cantidad, etc.
   - Después de completar el formulario, podrás guardar la información de la venta y vincularla al cliente correspondiente.

Productos:

1. Listado de Productos:
   - Muestra un listado de todos los productos disponibles.
   - Cada producto se muestra con su imagen, precio y categoría.
   - Se incluye un botón "Ver" que permite ver más detalles sobre cada producto.

2. Detalle de Producto:
   - Al hacer clic en el botón "Ver" de un producto, se muestra una vista detallada del mismo.
   - En esta vista, se pueden visualizar más detalles del producto, como nombre, descripción, precio y categoría.
   - Si no hay usuarios registrados (modo "Guest"), la opción de editar no estará disponible, solo se podrá ver la información del producto.

3. Edición de Producto:
   - Dentro de la vista detallada del producto, se brinda la posibilidad de editar sus datos.
   - Esta funcionalidad permite modificar el nombre, descripción, precio, categoría e imagen asociada al producto.

4. Filtrado de Productos por Categoría:
   - En el listado de productos, se proporciona la opción de filtrar los productos por categoría.
   - Esto permite al usuario visualizar únicamente los productos que pertenecen a una categoría específica seleccionada.

5. Crear Nuevos Productos:
   - Existe la opción de crear nuevos productos dentro del programa.
   - Al seleccionar esta opción, se abre un formulario donde se pueden ingresar los detalles del nuevo producto, como nombre, descripción, precio, categoría e imagen.

Estas funcionalidades permiten gestionar de manera efectiva los productos, incluyendo la visualización, edición, filtrado y creación de nuevos productos. 

Categorías:

1. Listado de Categorías:
   - Muestra un listado de todas las categorías existentes.
   - Cada categoría se muestra con su nombre y la cantidad de productos asociados a ella.

2. Edición de Categorías:
   - Permite editar las categorías existentes.
   - Al seleccionar esta opción, podrás modificar el nombre de la categoría y realizar los cambios necesarios.

3. Eliminación de Categorías:
   - Permite eliminar categorías.
   - Al seleccionar esta opción, se borrará la categoría seleccionada y se eliminará cualquier relación con los productos asociados a ella.

4. Crear Nueva Categoría:
   - Existe la opción de crear nuevas categorías dentro del programa.
   - Al seleccionar esta opción, se abrirá un formulario donde podrás ingresar el nombre de la nueva categoría.
   - Después de completar el formulario, podrás guardar la información y crear la nueva categoría.

Estas funcionalidades permiten gestionar de manera efectiva las categorías del programa, incluyendo la visualización, edición, eliminación y creación de nuevas categorías. 