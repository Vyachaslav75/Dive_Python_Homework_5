def path_name(path):
    path_file = path[:path.rfind('\\')]
    file_name, ext = path[path.rfind('\\')+1:].split('.')
    return path_file, file_name, ext
    
    
#path = 'H:\VirtualMashina\VirtBox\Tranzit\!!!GB!!!\Погружение в Python\Sem5\HW\Task2.py'
path = input('Введите путь: ')
path=r'%s' % path
print(path_name(path))