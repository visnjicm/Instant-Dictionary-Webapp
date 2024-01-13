import justpy as jp


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout, elevated=True, classes="bg-primary text-white")
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left", bordered=True, value=False)
        button = jp.QButton(a=toolbar, dense=True, flat=True, round=True, icon="menu",click=cls.move_drawer,
                            drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")
        page_container = jp.QPageContainer(a=layout)

        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text='Home', href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictionary', href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href="/about", classes=a_classes)
        jp.Br(a=qlist)

        jp.Div(a=page_container, text="HELLLLOOOOOOOO")

        return wp

    @staticmethod
    def move_drawer(widget, msg):
        widget.drawer.value = not widget.drawer.value
