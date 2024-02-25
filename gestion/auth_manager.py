from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido_paterno, apellido_materno, tipoUsuario, password):
        if not correo:
            raise ValueError("El usuario no proporciono el correo")
        correo_normalizado = self.normalize_email(correo)
        nuevo_usuario = self.model(correo=correo_normalizado, nombre=nombre, apellido_paterno=apellido_paterno,
                                   apellido_materno=apellido_materno, tipoUsuario=tipoUsuario)
        # generamos el hash de la contraseña
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()
