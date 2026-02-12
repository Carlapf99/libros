# Web oficial de autor · Django

Proyecto completo base para una web editorial minimalista y profesional con Django.

## Incluye

- Inicio con frase destacada editable y sección de novedad.
- Catálogo de libros + detalle por libro.
- Sobre mí con biografía y foto.
- Blog con detalle de post.
- Comentarios con **moderación manual** obligatoria.
- Contacto con envío real por SMTP (sin publicar email).
- Admin de Django para gestión integral.
- Diseño responsive con HTML + CSS propio (sin Bootstrap).


## Documentación completa

Consulta la guía extendida en `docs/PROJECT_DOCUMENTATION.md`.

Además, la propuesta formal del proyecto está en `docs/WEB_DEVELOPMENT_PROPOSAL.md`.

## Estructura

```text
config/                 # settings, urls globales, wsgi/asgi
apps/core/              # inicio, sobre mí, contacto, perfil autor
apps/books/             # catálogo y detalle de libros
apps/blog/              # posts + comentarios moderados
templates/              # base + includes + login
static/css/             # base/layout/components/pages
media/                  # portadas y foto del autor
```

## Instalación local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/base.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py bootstrap_content
python manage.py runserver
```

## Uso del panel administrador

1. Accede a `/admin/` con tu superusuario.
2. Crea/edita el **Perfil del autor** (nombre, frase destacada y biografía).
3. Crea libros en **Books** (puedes dejar portada vacía y subirla después).
4. Crea artículos en **Blog > Posts** y publícalos.
5. Modera comentarios en **Blog > Comments** usando acciones masivas.

> En navegación pública verás acceso directo a `Admin` cuando inicies sesión como staff.

## Variables de entorno

Configura `.env` con credenciales SMTP:

- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
- `DEFAULT_FROM_EMAIL`
- `CONTACT_RECIPIENT_EMAIL`

Para Gmail usa App Password. Para producción se recomienda SendGrid.

## URLs principales

- `/` Inicio
- `/libros/` catálogo
- `/libros/<slug>/` detalle
- `/sobre-mi/` biografía
- `/blog/` listado de artículos
- `/blog/<slug>/` detalle + comentarios
- `/contacto/` formulario de contacto
- `/admin/` administración
- `/robots.txt` directivas para bots
- `/sitemap.xml` sitemap SEO

## Comentarios y anti-spam

- Todos los comentarios se guardan con `is_approved=False`.
- Solo se muestran comentarios aprobados.
- Honeypot oculto + límite temporal básico de envío.

## Producción (recomendado)

- `DJANGO_SETTINGS_MODULE=config.settings.production`
- `DEBUG=False`, `ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS` configurados.
- PostgreSQL + WhiteNoise/CDN + HTTPS.
- `python manage.py check --deploy`


## Calidad y pruebas

```bash
python manage.py test
```

Incluye pruebas mínimas de páginas públicas, `robots.txt`, `sitemap.xml` y moderación de comentarios.
