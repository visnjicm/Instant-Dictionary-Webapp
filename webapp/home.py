import justpy as jp

class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 "
                                   "h-screen")
        jp.Div(a=div, text="This is the about page!",
               classes="text-4xl m-2")
        jp.Div(a=div, text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec fermentum sapien sem, "
                            "et semper dolor commodo porta. Sed ante tortor, consequat vitae tempor quis, interdum id "
                            "elit. Cras accumsan justo at dui iaculis, eget placerat massa aliquet. Pellentesque et "
                            "semper nulla, sodales lacinia ante. Aliquam efficitur nulla at porta lobortis. Nunc nunc "
                            "ipsum, blandit ac urna sit amet, imperdiet dapibus ipsum. Pellentesque habitant morbi "
                            "tristique senectus et netus et malesuada fames ac turpis egestas. Proin id ornare elit.\n"
                            ), classes="text-lg")
        return wp

