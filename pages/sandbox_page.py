from selenium.webdriver.common.by import By
from .base_page import BasePage
import pytest

class SandboxPage(BasePage):
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")

    DYNAMIC_ID_BUTTON = (
        By.XPATH, "//button[contains(text(), 'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]"
        )

    TEXTO_OCULTO = (
        By.XPATH, "//p[contains(text(), 'OMG, aparezco después de 3 segundos de haber hecho click en el botón')]"
        )

    DEPORTE_DROPDOWN = (
        By.ID, "formBasicSelect"
    )
    

    MOSTRAR_POPUP_BOTTON = (
        By.XPATH, "//button[@type='button' and contains(@class, 'btn-primary') and contains(text(), 'Mostrar popup')]"


    )


    POPUP_TITLE = (
        By.ID, "contained-modal-title-vcenter"
    )


#esto es una tupla, conviene mas usar un fstring y despues en el llamado de los tests pasarle el nobmre de la variable
    """CHECKBOX_BUTTON = (
        By.XPATH, "//label[contains(., 'Hamburguesa')]/preceding-sibling::input[@type='checkbox']"
    )"""

    def navigate_sandbox(self):
        self.navigate_to("https://thefreerangetester.github.io/sandbox-automation-testing/")
    
    def click_enviar(self):
        self.click(self.ENVIAR_BUTTON)


    def click_boton_id_dinamico(self):
        self.click(self.DYNAMIC_ID_BUTTON)

    def hover_over_dynamic_id_button(self):
        self.hover_over_element(self.DYNAMIC_ID_BUTTON)



#El f string sirve para poder pasarle el texto que yo quiera desde test_sandbox.
#si lo hago con "//label[contains(., 'Hamburguesa')]/preceding-sibling::input[@type='checkbox']" sería una tupla y por tanto es inmutable
#por eso es ideal hacerlo dentro de esta funcion.
    def select_checkbox_with_label(self, label_text):
        assert label_text in ["Pizza", "Hamburguesa", "Pasta", "Helado", "Torta"], "La opcion no existe."
        checkbox_locator = (
                By.XPATH,
                f"//label[contains(., '{label_text}')]/preceding-sibling::input[@type='checkbox']"
        )
        self.select_element(checkbox_locator)


    def is_checkbox_selected(self, label_text):
        assert label_text in ["Pizza", "Hamburguesa", "Pasta", "Helado", "Torta"], "La opcion no existe."
        checkbox_locator = (
                By.XPATH,
                f"//label[contains(., '{label_text}')]/preceding-sibling::input[@type='checkbox']"
        )
        self.select_element(checkbox_locator)

        checkbox_element = self.driver.find_element(*checkbox_locator)
        return checkbox_element.is_selected()




    def select_radio_button(self, option):
        assert option in ["Si", "No"], "La opcion tiene que ser Si o No"
        radio_button_checkbox = (
            By.XPATH, f"//label[@class='form-check-label' and contains(text(), '{option}')]"
        )
        self.select_element(radio_button_checkbox)

    

    #SELECCIONANDO DEPORTE DEL DROWDOWN.
    def select_deporte(self, deporte):
        #SE ESTA REUTILIZANDO CODIGO, MUY IMPORTANTE
        self.select_from_dropdown_by_visible_text(self.DEPORTE_DROPDOWN, deporte)



    def get_deporte_dropdown_options(self):
        return self.get_select_options(self.DEPORTE_DROPDOWN)
    
 
    def click_boton_popup(self):
        #primero hace el hover, dsp lo clickea
        self.hover_over_element(self.MOSTRAR_POPUP_BOTTON)
        self.click(self.MOSTRAR_POPUP_BOTTON)

    def get_popup_title_text(self):
        return self.wait_for_element(self.POPUP_TITLE).text
    


    def get_celda_valor(self,fila,columna):
        # Trabajamos con los valores de las celdas que cambian cuando refresca la pagina.
        celda_xpath = f"(//table[@class='table table-striped table-bordered table-hover']/tbody/tr)[{fila}]/td[{columna}]"

        celda = self.wait_for_element((By.XPATH, celda_xpath))

        return celda.text if celda else None
    
    def get_celda_estatica_valor(self,fila,columna):
        # Trabajamos con los valores de las celdas que cambian cuando refresca la pagina.
        celda_xpath = f"(//h2[normalize-space()='Tabla estática']/following-sibling::table/tbody/tr)[{fila}]/td[{columna}]"
 
        celda = self.wait_for_element((By.XPATH, celda_xpath))

        return celda.text if celda else None

