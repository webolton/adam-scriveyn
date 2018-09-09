from ipywidgets import Text, Layout, Button, Box, Dropdown, Label, IntText
from lib import ImageProcessor
from lib.ImageProcessor import rename_images_in_directory

def render_image_input_form():
    form_item_layout = Layout(
        display='flex',
        flex_flow='row',
        justify_content='space-between'
    )

    FOLIO_SIDES = ('r', 'v')

    input_dir, out_dir, first_fol_ind, first_fol_side, start_fol, siglum = \
        Text(value='images/input_N'), Text(value='images/output_N'), IntText(value=0), Dropdown(options=FOLIO_SIDES), IntText(value=1), Text()

    submit_button = Button(description='Submit', disabled=False, button_style='success', layout=form_item_layout)

    form_items = [
        Box([Label(value='Image Directory'), input_dir], layout=form_item_layout),
        Box([Label(value='Output Directory'), out_dir], layout=form_item_layout),
        Box([Label(value='Index of first folio'), first_fol_ind], layout=form_item_layout),
        Box([Label(value='Side of first folio'), first_fol_side], layout=form_item_layout),
        Box([Label(value='Start of foliation'), start_fol], layout=form_item_layout),
        Box([Label(value='MS siglum'), siglum], layout=form_item_layout),
        submit_button
    ]

    image_input_form = Box(form_items, layout=Layout(
        display='flex',
        flex_flow='column',
        border='solid 2px',
        align_items='stretch',
        width='50%'
    ))

    submit_button.on_click(handle_submit)
    return image_input_form

def validate_image_input_form(input_dir, out_dir, siglum):
    valid = None
    for input in [input_dir, out_dir, siglum]:
        if input.value == '':
            print('You must provide a value for each item in form')
            valid = False
        else:
            valid = True
    return valid

def format_page_data(first_fol_ind, first_fol_side, start_fol):
    return { 'start_index': first_fol_ind, 'start_side': first_fol_side, 'start_folio':  start_fol }

def handle_submit(submit_button):
    if validate_image_input_form(input_dir.value, out_dir.value, siglum.value):
        page_data = format_page_data(first_fol_ind.value, first_fol_side.value, start_fol.value)
        rename_images_in_directory(input_dir.value, out_dir.value, siglum.value, page_data)

# submit_button.on_click(handle_submit)
# image_input_form
