import uuid

types = []
objs = {}
quotation_marks_keys = ["content", "fontFamily", "d"]

uuidChars = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")


class BasAnimate:
    actions = []
    count = 0
    attribute = {}

    def __init__(self) -> None:
        self.actions = []

    def animate(self, obj, delay=0, duration=0, attribute=None):
        self.count += 1
        if delay > 0:
            self.actions.append(set_string(
                obj=obj, duration=delay, attribute={}))
        self.actions.append(set_string(
            obj=obj, duration=duration, attribute=attribute))
        if attribute is not None:
            self.attribute.update(attribute)
        return self

    def finish(self):
        print(f'{" then ".join(self.actions)}')


def short_uuid():
    uid = str(uuid.uuid4()).replace('-', '')
    result = ''
    for i in range(0, 8):
        sub = uid[i * 4: i * 4 + 4]
        x = int(sub, 16)
        result += uuidChars[x % 0x34]
    return result


def new_type(type_name, attribute, obj_type="text"):
    attribute["alpha"] = 0
    new_type = {
        "type_name": type_name,
        "attribute": attribute
    }
    types.append(new_type)
    def_text = f'def {obj_type} {type_name} {{\n{string_of_attribute(attribute, tab="    ")}\n}}'
    print(def_text)
    return new_type


def string_of_attribute(attribute, tab="", sep='\n'):
    res = []
    for key in attribute:
        attribute_text = ''
        attribute_text += tab
        attribute_text += key
        attribute_text += " = "
        attribute_text += f'"{attribute[key]}"' if key in quotation_marks_keys else f'{attribute[key]}'
        res.append(attribute_text)
    return sep.join(res)


def get_type(type_name):
    for type in types:
        if type["type_name"] == type_name:
            return type
    return None


def create_obj(type, attribute=None, id=None):
    if id is None:
        id = short_uuid()
    if attribute is None:
        attribute = {}
    obj = {
        "attribute": attribute,
        "id": id,
        "type": type
    }
    objs[id] = obj
    print(
        f'let {id} = {type["type_name"]}{{{string_of_attribute(attribute, sep=", ")}}}')
    return obj


def set_string(obj, duration=0, attribute=None):
    id = obj['id']
    tab = "    "
    return f'set {id} {{\n{string_of_attribute(attribute, tab=tab)}\n}} {duration}s'
