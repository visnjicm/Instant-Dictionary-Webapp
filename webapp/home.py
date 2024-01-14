import justpy as jp
import webapp.navbar as navbar


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        page = navbar.Navbar(wp)
        page_container = page.return_page_container()

        jp.Div(a=page_container, text="This is the home page!", classes="text-4xl m-2")

        return wp
