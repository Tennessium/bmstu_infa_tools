from django.shortcuts import render
from json import loads
import os


def load_modules():
    module_names = os.listdir('modules')
    _modules = []

    for module_name in module_names:
        try:
            with open('modules/' + module_name + '/description.json', 'r') as file_read:
                description = loads(file_read.read())
            description['id'] = module_name
            with open('modules/' + module_name + '/' + module_name + '.html', 'r') as page_file:
                description['content'] = page_file.read()
            _modules.append(description)
        except:
            pass

    if 'create' in module_names:
        for module, i in zip(_modules, range(0, len(_modules))):
            if module['id'] == 'create':
                _modules.append(_modules.pop(i))
                break

    return _modules


modules = load_modules()


def get_module(_id):
    global modules
    for module in modules:
        if module['id'] == _id:
            return module
    return None


def main_page(request):
    data = dict()
    data['modules'] = modules
    return render(request, 'main_page.html', data)


def module_page(request):
    global modules
    modules = load_modules()
    module = get_module(request.path[1:])
    return render(request, 'module_template.html', module)
