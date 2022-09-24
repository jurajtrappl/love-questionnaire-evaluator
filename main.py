from dotenv import load_dotenv
import os

from forms import GoogleFormsService
from google_form import GoogleForm
from response import ResponsesEvaluator
from writer import SheetWriter

load_dotenv()

# Connect and get the Google Forms API service.
KEY_FILE_LOCATION = "client_secrets.json"
SCOPES = ["https://www.googleapis.com/auth/forms.body.readonly",
          "https://www.googleapis.com/auth/forms.responses.readonly"]
forms_service = GoogleFormsService(KEY_FILE_LOCATION, SCOPES).get_service()

# Set up a connection to the Google Form.
form = GoogleForm(os.environ.get('FORM_ID'), forms_service)

"""
Sternberg's triangular love scale answer ranges are downscaled from the original 1-9 to 1-7. Scaling helps users to differentiate between answers.
"""
ORIGINAL_SCALE = 9
SCALE_USED = 7
stls_scale_factor = ORIGINAL_SCALE / SCALE_USED

# Process, evaluates and write the results to the sheet with formatting.
response_evaluator = ResponsesEvaluator(
    form.get_questions_in_order(), stls_scale_factor)
results = response_evaluator.evaluate(form.retrieve_form_responses())
SheetWriter(stls_scale_factor).write(results)
