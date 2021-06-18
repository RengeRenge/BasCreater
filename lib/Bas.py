import uuid
import re
import collections
import xml.etree.ElementTree as ET

types = []
quotation_marks_keys = ["content", "fontFamily", "d"]

uuidChars = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

def mkdir(path):
    import os
    path = path.strip().rstrip("\\")
    if not os.path.exists(path):
        os.makedirs(path)


def short_uuid():
    uid = str(uuid.uuid4()).replace('-', '')
    result = ''
    for i in range(0, 8):
        sub = uid[i * 4: i * 4 + 4]
        x = int(sub, 16)
        result += uuidChars[x % 0x34]
    return result


def string_of_attribute(attribute, tab="", sep='\n'):
    res = []
    if attribute is None:
        attribute = {}
    for key in attribute:
        attribute_text = ''
        attribute_text += tab
        attribute_text += key
        attribute_text += " = "
        attribute_text += f'"{attribute[key]}"' if key in quotation_marks_keys else f'{attribute[key]}'
        res.append(attribute_text)
    return sep.join(res)


def get_type(name):
    for type in types:
        if type["name"] == name:
            return type
    return None


def set_string(id, duration=0, attribute=None):
    tab = "    "
    return f'set {id} {{\n{string_of_attribute(attribute, tab=tab)}\n}} {duration}s'


def read_bas():
    f.seek(0)
    return f.read()


class BasType:
    def __init__(self, attribute=None, obj_type="text", name=None, attributes=None) -> None:
        if attribute is None:
            attribute = {}
        if name is None:
            name = short_uuid()
        if 'alpha' not in attribute:
            attribute["alpha"] = 0
        self.name = name
        self.attribute = attribute
        self.attributes = attributes
        types.append(self)

        if attributes is not None:
            for index, attr in enumerate(attributes):
                self.__write(name + '_' + str(index), attr, obj_type)
        else:
            self.__write(name, attribute, obj_type)

    def __write(self, name, attribute, obj_type):
        def_text = f'def {obj_type} {name} {{\n{string_of_attribute(attribute, tab="    ")}\n}}\n'
        f.write(def_text)
        print(def_text)

    @classmethod
    def parseXML(self, file, name=None):
        tree = ET.parse(file)
        root = tree.getroot()
        attributes = []
        for path in root:
            if path.tag.endswith('path') and 'd' in path.attrib:
                attribute = {'d': path.attrib["d"], "alpha": 0}
                if 'fill' in path.attrib and len(path.attrib['fill']) > 0:
                    fill = path.attrib['fill'].replace('#', '0x')
                    attribute['fillColor'] = fill
                attributes.append(attribute)
        return BasType(name=name, obj_type='path', attributes=attributes)


class BasObject:
    def __init__(self, type: BasType, attribute, id=None) -> None:
        if id is None:
            id = short_uuid()
        if attribute is None:
            attribute = {}
        self.type = type
        self.attribute = attribute
        self.id = id
        self.ids = []

        if type.attributes is not None:
            for index, attr in enumerate(type.attributes):
                id = short_uuid()
                self.ids.append(id)

                name = type.name + '_' + str(index)
                self.__write(id, name, attribute)
        else:
            self.__write(id, type.name, attribute)

    def __write(self, id, name, attribute):
        data = f'let {id} = {name}{{{string_of_attribute(attribute, sep=", ")}}}\n'
        f.write(data)
        print(data)

    def get_int(self, key):
        number = self.attribute[key]
        if isinstance(number, str):
            n = re.findall(r'-?\d+\.?\d*', number)
            if len(n) > 0:
                n = n[0]
                return int(n)
        return int(number)

    def get_float(self, key):
        number = self.attribute[key]
        print(number)
        if isinstance(number, str):
            n = re.findall(r'-?\d+\.?\d*', number)
            if len(n) > 0:
                n = n[0]
                print(n)
                return float(n)
        return float(number)


class BasGroup:
    def __init__(self, objs, attribute=None) -> None:
        if attribute is None:
            attribute = {}
        self.attribute = attribute
        self.objs = objs


class BasAnimate:
    def __init__(self, type: BasType = None, delay=0, duration=0, attribute=None) -> None:
        self.count = 0
        self.attribute = {}

        self.obj = None
        self.group = None

        self.actions = collections.OrderedDict()

        if type is not None:
            obj = BasObject(type)
            self.animate(obj, delay=delay, duration=duration,
                         attribute=attribute)

    def animate(self, obj: BasObject, delay=0, duration=0, attribute=None):
        self.count += 1
        self.obj = obj
        self.__animate_many(obj, delay, duration, attribute)
        if attribute is not None:
            self.attribute.update(attribute)
            obj.attribute.update(attribute)
        return self

    def animate_g(self, group: BasGroup, delay=0, duration=0, attribute=None):
        self.count += 1
        self.group = group

        for obj in group.objs:
            self.__animate_many(obj, delay, duration, attribute)

        if attribute is not None:
            self.attribute.update(attribute)
            group.attribute.update(attribute)
        return self

    def __animate_many(self, obj: BasObject, delay=0, duration=0, attribute=None):
        if obj.ids is not None and len(obj.ids) > 0:
            for id in obj.ids:
                self.__animate(id, delay, duration, attribute)
        else:
            self.__animate(obj.id, delay, duration, attribute)

    def __animate(self, id: str, delay=0, duration=0, attribute=None):
        actions = self.actions
        if id not in actions:
            actions[id] = []
        if delay > 0:
            actions[id].append(set_string(id, delay, {}))
        actions[id].append(set_string(id, duration, attribute))

    def finish(self):
        for id, value in self.actions.items():
            data = f'{" then ".join(value)}\n'
            f.write(data)
            print(data)
        self.actions.clear()
        self.attribute.clear()
        self.count = 0

path = './out'
mkdir(path)
f = open(path + '/bas.txt', 'w+')
