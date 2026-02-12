# Documentación del proyecto: Web oficial de autor (Django)

Esta documentación explica cómo está construido el proyecto, cómo arrancarlo, cómo usar el panel de administración y cómo mantenerlo en producción.

## 1) Objetivo del proyecto

Sitio web oficial de autor con estas secciones públicas:

- Inicio
- Libros
- Sobre mí
- Blog
- Contacto

Y con un panel de administración para gestionar contenido sin tocar código:

- Perfil del autor
- Libros
- Artículos del blog
- Comentarios con moderación manual

---

## 2) Arquitectura y estructura

```text
libros/
├── apps/
│   ├── core/      # Home, Sobre mí, Contacto, perfil de autor
│   ├── books/     # Catálogo y detalle de libros
│   └── blog/      # Posts y comentarios
├── config/        # Settings, URLs globales, ASGI/WSGI
├── templates/     # base e includes compartidos
├── static/        # CSS propio por capas
├── requirements/  # Dependencias base y producción
├── manage.py
└── README.md
```

### Responsabilidades por app

- `apps/core`: páginas institucionales + formulario de contacto + modelo `AuthorProfile`.
- `apps/books`: listado y detalle de libros + modelo `Book`.
- `apps/blog`: listado y detalle de artículos + comentarios moderados (`Post`, `Comment`).

---

## 3) Modelos de datos

## `AuthorProfile` (`apps/core/models.py`)

- `full_name`: nombre visible del autor.
- `hero_quote`: frase destacada para la home.
- `biography`: biografía para sección “Sobre mí”.
- `photo`: foto del autor (opcional).
- `updated_at`: fecha de actualización.

> Restricción: solo puede existir un perfil (singleton lógico) validado en `clean()` y reforzado en admin.

## `Book` (`apps/books/models.py`)

- `title`, `slug`
- `cover` (opcional)
- `synopsis`
- `price`
- `purchase_url`
- `is_featured` (controla “Novedad” en inicio)
- `published_date`, `created_at`

## `Post` y `Comment` (`apps/blog/models.py`)

- `Post`: título, slug, extracto, contenido, flags de publicación.
- `Comment`: ligado a `Post`, autor/email/contenido, `is_approved` para moderación.

---

## 4) Flujo de contenido en frontend

### Inicio (`/`)

- Muestra nombre/frase de `AuthorProfile`.
- Muestra el último `Book` con `is_featured=True`.
- Si faltan datos, muestra placeholders y mensajes guiados.

### Libros (`/libros/`, `/libros/<slug>/`)

- Catálogo visual de libros.
- Detalle con sinopsis, precio y enlace de compra externo.

### Sobre mí (`/sobre-mi/`)

- Biografía y foto del autor.

### Blog (`/blog/`, `/blog/<slug>/`)

- Lista de artículos publicados.
- Detalle de artículo con comentarios aprobados.
- Formulario de comentarios con moderación manual (nombre + texto).

### Contacto (`/contacto/`)

- Formulario que envía correo SMTP al destinatario privado configurado en `.env`.

---

## 5) Administración (cómo usarla)

Accede en `/admin/` con superusuario.

### Orden recomendado al iniciar

1. Crear/editar **Perfil del autor**.
2. Cargar **Libros** (marcar uno como destacado para que salga en “Novedad”).
3. Cargar **Posts** y publicarlos.
4. Revisar **Comments** y aprobar los válidos.

### Funciones útiles ya preparadas

- `BookAdmin`: edición rápida de `is_featured` y `price`, filtros y búsqueda.
- `PostAdmin`: acciones masivas de publicar/despublicar.
- `CommentAdmin`: acciones de aprobar/dejar pendiente.
- `AuthorProfileAdmin`: estructura clara por secciones.

---

## 6) Arranque local paso a paso

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

Luego abre: `http://127.0.0.1:8000`

### ¿Qué hace `bootstrap_content`?

Genera contenido mínimo de demostración:

- 1 perfil de autor
- 10 libros
- 5 posts publicados

Esto sirve para no ver el sitio vacío la primera vez.

---

## 7) Variables de entorno

En `.env` define como mínimo:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `EMAIL_USE_TLS`
- `DEFAULT_FROM_EMAIL`
- `CONTACT_RECIPIENT_EMAIL`

Nunca subas `.env` al repositorio.

---

## 8) Seguridad y moderación

- Comentarios nuevos se guardan con `is_approved=False`.
- Solo se muestran comentarios aprobados.
- Formulario de comentarios incluye honeypot + límite temporal básico.
- En producción usar `config.settings.production` y HTTPS.

---

## 9) Estilos y diseño

El CSS está dividido para mantenimiento:

- `static/css/base.css` → tipografía, variables globales.
- `static/css/layout.css` → estructura de layout y navegación.
- `static/css/components.css` → botones/cards/forms/placeholders.
- `static/css/pages.css` → estilos específicos por página.

Diseño: editorial, minimalista, responsive, sin Bootstrap.

---

## 10) Despliegue recomendado (resumen)

- Backend: Gunicorn + Django
- Reverse proxy: Nginx (o plataforma gestionada)
- DB producción: PostgreSQL
- Estáticos: WhiteNoise o CDN
- Ajustes:
  - `DJANGO_SETTINGS_MODULE=config.settings.production`
  - `DEBUG=False`
  - `ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS`

Comando de verificación:

```bash
python manage.py check --deploy
```

---

## 11) Problemas frecuentes

1. **No carga la web en local**
   - Verifica que el venv está activado.
   - Verifica que Django está instalado.

2. **No aparecen imágenes**
   - Revisa `MEDIA_ROOT/MEDIA_URL`.
   - Asegura que cargas imágenes desde admin.

3. **No llegan correos**
   - Revisa credenciales SMTP.
   - Para Gmail usa App Password.

4. **Blog sin comentarios**
   - Revisa en admin si están aprobados.



---

## 12) SEO y páginas de error

El proyecto incluye:

- Metadatos base (`title`, `description`, OpenGraph) en `templates/base.html`.
- `robots.txt` en `/robots.txt`.
- `sitemap.xml` en `/sitemap.xml` con páginas estáticas, libros y posts publicados.
- Páginas personalizadas de error `404` y `500`.

---

## 13) Testing mínimo incluido

Se añadieron pruebas base para:

- Carga de páginas públicas (`home`, `about`, `contact`).
- Disponibilidad de `robots.txt` y `sitemap.xml`.
- Verificación de que comentarios nuevos quedan pendientes de aprobación.
