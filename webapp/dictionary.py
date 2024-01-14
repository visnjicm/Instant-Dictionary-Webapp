import justpy as jp
import definition
import webapp.navbar as navbar


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        page = navbar.Navbar(div)
        page_container = page.return_page_container()

        jp.Div(a=page_container, text="Instant English Dictionary", classes="text-4xl m-2")

        jp.Div(a=page_container, text="Get the definition of any English""word instantly as you type.",
               classes="text-lg")

        input_div = jp.Div(a=page_container, classes="grid grid-cols-2")

        output_div = jp.Div(a=page_container, classes="m-2 p-2 text-lg border-2 ""border-gray-300 h-40")

        input_box = jp.Input(a=page_container, placeholder="Type in a word here...",
                             classes="m-2 bg-gray-100 border-2 border-gray-200", outputdiv=output_div)

        input_box.on('input', cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
