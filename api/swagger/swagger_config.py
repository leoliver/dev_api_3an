from . import api

from swagger.namespaces.aluno_namespace import alunos_ns


def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(alunos_ns, path="/alunos")
    api.mask_swagger = False