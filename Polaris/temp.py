from graphviz import Digraph

def create_project_structure():
    dot = Digraph(comment='Polaris Project Structure')
    # 设置图形、节点、边的属性
    dot.attr(fontname="Times New Room")
    dot.attr('node', fontname="Times New Room", fontsize='20', shape='none', height='0.25')
    dot.attr('edge', fontname="Times New Room", fontsize='20')
    dot.attr(rankdir='LR', size='8.27,11.69', ratio='fill')  # 调整为A4纸尺寸，方向为TB（从上到下）
    dot.attr(rankdir='LR', splines='false')

    # Polaris项目根目录
    dot.node('Polaris', 'Polaris/')

    # 根目录文件
    root_files = ['uwsgi.ini', '.env', 'manage.py', 'uwsgi.pid', 'uwsgi.log', 'django.log']
    for file in root_files:
        dot.node(file, file)
        dot.edge('Polaris', file)

    # Polaris/Polaris目录
    dot.node('InnerPolaris', 'Polaris/Polaris/')
    dot.edge('Polaris', 'InnerPolaris')

    # Polaris/Polaris目录下的文件
    polaris_files = ['urls.py', 'polaris.sql', 'wsgi.py', 'asgi.py', 'settings.py']
    for file in polaris_files:
        dot.node('P_'+file, file)
        dot.edge('InnerPolaris', 'P_'+file)

    # app01目录
    dot.node('app01', 'app01/')
    dot.edge('Polaris', 'app01')

    # app01目录下的文件
    app01_files = ['urls.py', 'views.py']
    for file in app01_files:
        dot.node('A_'+file, file)
        dot.edge('app01', 'A_'+file)

    # app01子目录
    app01_subdirs = ['data', 'middleware', 'utils', 'static', 'templates']
    for subdir in app01_subdirs:
        dot.node(subdir, subdir+'/')
        dot.edge('app01', subdir)

    # middleware目录下的文件
    middleware_files = ['openai_api.py', 'baidu_api.py', 'SQLConn.py']
    for file in middleware_files:
        dot.node('M_'+file, file)
        dot.edge('middleware', 'M_'+file)

    # utils目录下的子目录
    utils_subdirs = ['notes_data', 'data_miner', 'polaris_ai']
    for subdir in utils_subdirs:
        dot.node(subdir, subdir+'/')
        dot.edge('utils', subdir)
        
        # 假设每个子目录下有几个示例文件
        example_files = ['example1.py', 'example2.py']
        for file in example_files:
            dot.node(subdir+'_'+file, file)
            dot.edge(subdir, subdir+'_'+file)

    # static目录下的文件
    static_files = ['my_space.css', 'polaris.css', 'note_template.js', 'my_space.js', 'write_note.js', 'example.js', 'note_template.css', 'example.css']
    for file in static_files:
        dot.node('S_'+file, file)
        dot.edge('static', 'S_'+file)

    # static/img子目录
    dot.node('img', 'img/')
    dot.edge('static', 'img')

    # templates目录下的文件
    templates_files = ['example.html', 'polaris.html', 'dashboard.html', 'my_space.html', 'note_template.html', 'write_note.html']
    for file in templates_files:
        dot.node('T_'+file, file)
        dot.edge('templates', 'T_'+file)

    # 渲染图形到文件
    dot.render('polaris_project_structure_detailed', format='png', view=True)

if __name__ == '__main__':
    create_project_structure()
