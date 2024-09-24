from django.shortcuts import redirect

class UsuariosRegistrados:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        rutas_protegidas = ['/ver_post/', '/escribir_post/', '/eliminar_post/']

        if not request.user.is_authenticated and request.path in rutas_protegidas:
            return redirect('login')  

        response = self.get_response(request)
        return response