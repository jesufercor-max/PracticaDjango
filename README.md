# 🐾🎬 Práctica Django: Gestión de Datos mediante Aplicaciones Web

## 📌 Descripción del proyecto

Esta práctica consiste en el desarrollo de aplicaciones web utilizando **Django**, un framework de Python que permite crear aplicaciones dinámicas conectadas a una base de datos.

El objetivo principal es aprender a estructurar un proyecto web mediante modelos, vistas, rutas y plantillas HTML, permitiendo consultar y mostrar información almacenada en una base de datos de forma organizada.

La práctica se divide en dos proyectos temáticos:

- **Sistema de Gestión de Protectoras y Animales:** aplicación orientada al registro y consulta de animales resguardados, organizaciones protectoras y personal colaborador.
- **Sistema de Gestión de Animes y Plataformas:** aplicación destinada a la consulta de información sobre animes, plataformas de streaming y disponibilidad de sus contenidos.

Ambos proyectos comparten una estructura similar y permiten poner en práctica los principales conceptos del desarrollo web con Django.

---

## 🎯 Objetivos de la práctica

Los objetivos principales de esta práctica son:

- Comprender la estructura y el funcionamiento de un proyecto Django.
- Crear modelos de datos mediante `models.py` para representar diferentes entidades.
- Definir rutas en `urls.py` para facilitar la navegación entre las distintas páginas.
- Desarrollar vistas en `views.py` para consultar información de la base de datos.
- Utilizar el sistema de plantillas de Django para mostrar los datos dinámicamente mediante HTML.
- Aplicar estilos CSS para mejorar la presentación y la experiencia visual de las aplicaciones.
- Aprender a relacionar la lógica de la aplicación con la información almacenada en la base de datos.
- Organizar el código en diferentes archivos para facilitar su mantenimiento y comprensión.
- Familiarizarse con el uso de Git y GitHub para organizar y gestionar el desarrollo del proyecto mediante ramas.

---

## 🐾 Proyecto 1: Gestión de Protectoras y Animales

### Descripción

Este proyecto está orientado a la administración y consulta de información relacionada con animales, protectoras y colaboradores.

Permite representar diferentes entidades mediante modelos de Django y mostrar sus registros en páginas web utilizando plantillas HTML.

### Modelos de datos

Se definen los siguientes modelos en `models.py`:

- **Animal:** almacena el nombre del animal, su tipo y el cuidador asociado. El tipo se selecciona entre diferentes categorías, como anfibios, felinos y reptiles.
- **Protectora:** contiene información sobre las organizaciones protectoras, incluyendo su nombre, descripción y fecha de creación.
- **Colaborador:** registra los datos del personal colaborador, como su nombre, cargo y fecha de incorporación a la protectora.

### Funcionalidades

La aplicación dispone de las siguientes vistas:

- **Inicio:** página principal desde la que se puede acceder a las diferentes secciones.
- **Animales:** muestra los animales registrados en la base de datos.
- **Protectoras:** presenta la información de las organizaciones protectoras.
- **Colaboradores:** muestra los nombres y cargos del personal colaborador.

### Presentación visual

Las plantillas HTML permiten representar la información mediante tablas dinámicas.

Se utilizan estilos CSS para mejorar la legibilidad de los datos, incorporando colores, espaciado, bordes y elementos visuales que facilitan la navegación.

---

## 🎬 Proyecto 2: Gestión de Animes y Plataformas

### Descripción

Este proyecto está destinado a la consulta y presentación de información sobre series de anime y plataformas de streaming.

Su finalidad es aplicar los conocimientos adquiridos con Django mediante una temática diferente, utilizando modelos, vistas, rutas y plantillas para organizar y mostrar la información.

### Modelos de datos

Se definen los siguientes modelos en `models.py`:

- **Anime:** almacena información sobre las series, incluyendo título, título original, sinopsis, año de estreno, número de episodios, tipo, estado e imagen.
- **Plataforma:** contiene los datos de las plataformas de streaming, como nombre, descripción, página web, logotipo y estado de actividad.
- **Disponibilidad:** registra información sobre la disponibilidad de los contenidos, incluyendo idioma del audio, subtítulos, doblaje, fechas de inicio y finalización, y estado de actividad.

### Funcionalidades

La aplicación dispone de las siguientes vistas:

- **Inicio:** página principal de navegación.
- **Animes:** muestra el catálogo de series registradas, incluyendo su título, número de episodios e imagen.
- **Plataformas:** presenta las plataformas de streaming disponibles, sus páginas web y sus logotipos.
- **Disponibilidad:** permite consultar información sobre los idiomas, el doblaje y el estado de disponibilidad de los contenidos.

### Presentación visual

La información se muestra mediante tablas HTML dinámicas que utilizan el sistema de plantillas de Django.

Se incorporan estilos CSS para mejorar la presentación de los datos y facilitar la consulta de la información.

Además, se utilizan campos de tipo `ImageField` para almacenar las imágenes de los animes y los logotipos de las plataformas.

---

## 🛠️ Tecnologías utilizadas

Las principales tecnologías y herramientas utilizadas en esta práctica son:

- **Python:** lenguaje de programación empleado para desarrollar la lógica de las aplicaciones.
- **Django:** framework web utilizado para gestionar modelos, vistas, rutas y plantillas.
- **HTML5:** lenguaje de marcado empleado para estructurar las páginas web.
- **CSS3:** utilizado para personalizar la apariencia visual de las aplicaciones.
- **Base de datos:** permite almacenar y consultar la información gestionada por los modelos de Django.
- **Git:** sistema de control de versiones utilizado para gestionar los cambios del proyecto.
- **GitHub:** plataforma para alojar el repositorio y facilitar el trabajo con ramas.
- **Visual Studio Code:** editor utilizado para desarrollar y organizar el código.

---

## 📂 Estructura general del proyecto

Los archivos principales de cada aplicación Django se organizan de la siguiente manera:

proyecto/ │ ├── models.py ├── urls.py ├── views.py ├── templates/ │ ├── index.html │ ├── postanimales.html │ ├── postprotectoras.html │ ├── postcolaboradores.html │ ├── postanimes.html │ ├── postplataformas.html │ └── postdisponibilidad.html │ └── README.md


Esta estructura es orientativa y reúne las plantillas de ambos proyectos. En una implementación real, cada aplicación puede tener su propia carpeta `templates` y sus propios archivos.

### Descripción de los archivos principales

- **`models.py`:** define los modelos y los campos que representan las entidades de la base de datos.
- **`urls.py`:** establece las rutas que permiten acceder a las diferentes páginas.
- **`views.py`:** contiene las funciones que consultan los datos y seleccionan las plantillas que deben mostrarse.
- **`templates/`:** contiene las plantillas HTML encargadas de representar la información.
- **`README.md`:** documenta el propósito, la estructura y los objetivos de la práctica.

---

## ⚙️ Funcionamiento general

El funcionamiento de las aplicaciones sigue el patrón habitual de Django:

1. El usuario accede a una URL de la aplicación.
2. Django identifica la ruta correspondiente definida en `urls.py`.
3. La ruta ejecuta la función asociada en `views.py`.
4. La vista consulta los registros almacenados mediante los modelos definidos en `models.py`.
5. Los datos obtenidos se envían al contexto de una plantilla HTML.
6. Django procesa la plantilla y genera la página que se muestra al usuario.

Este flujo permite separar la gestión de los datos, la lógica de la aplicación y la presentación visual.

---

## 📚 Aprendizajes adquiridos

Con el desarrollo de esta práctica se pretende consolidar los siguientes conocimientos:

- Creación y configuración de modelos en Django.
- Definición de campos y tipos de datos.
- Uso del ORM de Django para consultar registros mediante `objects.all()`.
- Configuración de rutas y asociación con vistas.
- Envío de información a las plantillas mediante el contexto.
- Utilización de etiquetas del sistema de plantillas, como `{% for %}` y `{{ variable }}`.
- Creación de tablas HTML para presentar información procedente de la base de datos.
- Aplicación de estilos CSS para mejorar la interfaz.
- Gestión de imágenes mediante campos `ImageField`.
- Organización del código y documentación de proyectos.
- Uso de Git y GitHub para el control de versiones y la gestión de ramas.
