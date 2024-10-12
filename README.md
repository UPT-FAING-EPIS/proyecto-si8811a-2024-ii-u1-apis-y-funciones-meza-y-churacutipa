# Flujo de Autenticación con Azure AD, Flask y MongoDB

Esta aplicación web Flask integra Azure Active Directory (Azure AD) para la autenticación de usuarios y MongoDB para almacenar perfiles y roles de usuarios. A continuación, se incluye una breve descripción general de cómo funciona el sistema:

## 1. Autenticación de Usuario

- Cuando un usuario accede a la aplicación, el sistema verifica si está autenticado.
- Si no está autenticado, el usuario se redirige a la página de inicio de sesión de Azure AD, configurada en el portal de Azure.

## 2. Intercambio de Tokens

- Después de iniciar sesión correctamente, Azure devuelve un código de autorización.
- La aplicación intercambia este código por un token de acceso utilizando MSAL (Biblioteca de Autenticación de Microsoft).
- El token de acceso permite que la aplicación recupere la información y los roles del perfil del usuario.

## 3. Almacenamiento de Datos del Usuario

- El correo electrónico, el nombre y los roles del usuario se guardan o actualizan en MongoDB.
- Esto garantiza que la información del usuario se almacene para el control de acceso basado en roles.

## 4. Control de Acceso Basado en Roles

- Según el rol del usuario:
  - Los usuarios con el rol de `admin` pueden acceder al Área de Administración.
  - Los usuarios con el rol de `user` pueden acceder al Área de Usuario.
- Si un usuario intenta acceder a un área sin el rol adecuado, se le denegará el acceso.

## 5. Cerrar Sesión

- El usuario puede cerrar sesión, lo que borra su sesión y lo redirige a la página de cierre de sesión de Azure AD.



## Objetivos del Proyecto con Enfoque en Azure

1. **Autenticación con Azure AD**: 
   Implementar un sistema de inicio de sesión utilizando Microsoft Azure Active Directory (Azure AD), permitiendo solo el acceso a correos electrónicos autorizados de la organización.

2. **Control de Acceso Basado en Roles**: 
   Implementar un control de acceso que limite el acceso a diferentes partes de la aplicación según los roles de usuario asignados en Azure AD (por ejemplo, `admin`, `user`).

3. **Seguridad Mejorada**: 
   Proteger información sensible utilizando conexiones seguras y validación de tokens de Azure AD.


## Tecnologías Utilizadas

 - **Flask**: Un micro framework web para construir el backend de la aplicación.
 - **Azure Active Directory (Azure AD)**: Para gestionar la autenticación y la autorización de usuarios, permitiendo el inicio de sesión con cuentas de Microsoft.
 - **MSAL (Microsoft Authentication Library)**: Biblioteca utilizada para obtener tokens de autenticación de Azure Active Directory.
 - **MongoDB**: Base de datos NoSQL para almacenar información y roles de perfiles de usuario.
 - **dotenv**: Para manejar variables de entorno desde un archivo `.env`.
 - **certifi**: Para asegurar las conexiones TLS a MongoDB.

