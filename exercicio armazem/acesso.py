from encodings.idna import ace_prefix


class acess_:
    def __init__(self, name, position, adm=False):
        self.name = name
        self.position = position
        self.adm = adm




stable_user = acess_("john Doe", "attendant")
adm_user = acess_("Jane Doe", "Manager", adm=True)
