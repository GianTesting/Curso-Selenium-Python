# Curso de Automatización de Pruebas con Selenium

Este repositorio contiene el código desarrollado durante el curso de automatización de pruebas con Selenium. En este curso, hemos aprendido a utilizar Selenium con Python y Pytest para automatizar pruebas en aplicaciones web, aplicando el modelo de Page Object y generando reportes con Allure.

## Contenido

- [Páginas](#páginas)
- [Tests](#tests)
- [Configuración](#configuración)
- [Reportes](#reportes)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Ejecución de Pruebas](#ejecución-de-pruebas)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Páginas

- **base_page.py**: Contiene la clase BasePage, que proporciona métodos para interactuar con elementos comunes de una página web.
- **sandbox_page.py**: Contiene la clase SandboxPage, que representa la página de pruebas utilizada en el curso.

## Tests

- **test_sandbox.py**: Archivo que contiene los casos de prueba desarrollados durante el curso, utilizando Pytest y Allure para generar reportes detallados.

## Configuración

- **conftest.py**: Archivo de configuración de Pytest, donde se definen fixtures y opciones de línea de comandos para ejecutar las pruebas.

## Reportes

- La carpeta **reports/** contiene los reportes generados por Allure después de ejecutar las pruebas.

## Requisitos

- Python 3.x
- Selenium
- Pytest
- Allure-Pytest
- WebDriver Manager

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone <(https://github.com/GianTesting/Curso-Selenium-Python/)>


2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt


## Ejecución de Pruebas

Puedes ejecutar las pruebas utilizando Pytest. Asegúrate de tener configurado el navegador que deseas utilizar en el archivo conftest.py. Por defecto, se utilizará Chrome.


Para generar reportes detallados con Allure, ejecuta:
pytest --alluredir=reports





