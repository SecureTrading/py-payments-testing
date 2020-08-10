from enum import Enum


class ExamplePage(Enum):
    WITHOUT_SUBMIT_BUTTON = "noSubmitButton=true&"
    WITH_ADDITIONAL_BUTTON = "additionalButton=true&"
    WITH_UPDATE_JWT = "updateJwt=ToDo&"
    WITH_SPECIFIC_FORM_ID = "formId=test"
    WITH_CALLBACK = "todo"
    IN_IFRAME = "iframe.html?"